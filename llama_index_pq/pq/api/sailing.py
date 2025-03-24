import re
import globals
from post_process.summary import extractive_summary
from llm_fw import llm_interface_qdrant
import shared
import json
import os
import time

out_dir = 'api_out'
out_dir_t2t = os.path.join(out_dir, 'txt2txt')


class api_sail:

    def __init__(self):
        self.g = globals.get_globals()
        self.interface = llm_interface_qdrant.get_interface()
        self.last_api_sail_query = None
        self.api_sail_depth_start = 0
        self.api_sail_depth = 0
        self.api_sail_count = 0
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        self.file_name = f'api_sail_log_{timestamp}.txt'
        self.query_file_name = f'api_sail_query_log_{timestamp}.txt'

    def shorten_string(self, text, max_bytes=1000):
        """Shortens a string to a maximum of 1000 bytes.

        Args:
          text: The string to shorten.
          max_bytes: The maximum number of bytes allowed (default: 1000).

        Returns:
          The shortened string, truncated at the last whole word before reaching
          max_bytes.
        """
        if len(text) <= max_bytes:
            return text

        # Encode the text as UTF-8 to get byte length
        encoded_text = text.encode('utf-8')

        # Truncate the string while staying under the byte limit
        while len(encoded_text) > max_bytes:
            # Split text by words on space
            words = text.rsplit()
            # Remove the last word and try again
            text = ' '.join(words[:-1])
            encoded_text = text.encode('utf-8')

        return text

    def get_next_target(self, nodes):

        if len(nodes) < self.api_sail_depth:
            self.api_sail_depth = self.api_sail_depth_start + len(self.g.api_sail_history)

        if len(nodes) > 0:

            if self.g.settings_data['sailing']['sail_target']:
                node = nodes[len(nodes) - 1]
                payload = json.loads(node.payload['_node_content'])
                out = payload['text']
                self.g.api_sail_history.append(out)
                return out
            else:
                node = nodes[0]
                payload = json.loads(node.payload['_node_content'])
                out = payload['text']
                self.g.api_sail_history.append(out)
                return out
        else:
            return -1

    def log(self, logfile, text):
        f = open(logfile, 'a')
        try:
            f.write(f"{text} \n")
        except:
            pass
        f.close()

	def run_api_sail(self, data):

		if data['reset_journey'] is True:
			self.last_api_sail_query = None
			self.api_sail_depth_start = 0
			self.g.api_sail_history = []
			self.api_sail_count = 0
			self.g.settings_data['sailing']['sail_text'] = data['query']
			timestamp = time.strftime("%Y%m%d-%H%M%S")
			self.file_name = f'api_sail_log_{timestamp}.txt'
			self.query_file_name = f'api_sail_query_log_{timestamp}.txt'

		if self.last_api_sail_query is None:
			self.last_api_sail_query = data['query']

		if self.api_sail_depth_start == 0:
			self.api_sail_depth_start = data['distance']
			self.api_sail_depth = data['distance']
			
		# Add sinus wave modification to depth if enabled
		if 'sinus_enabled' in data and data['sinus_enabled'] is True:
			# Apply sinus wave to depth based on count
			sinus_freq = data.get('sinus_freq', 1.0)  # Default to 1.0 if not provided
			sinus_range = data.get('sinus_range', 50)  # Default to 50 if not provided
			import math
			# Calculate sinus value based on current count and frequency
			sinus_value = math.sin(self.api_sail_count * sinus_freq)
			# Apply the range multiplier to get the actual offset
			depth_offset = int(sinus_value * sinus_range)
			# Apply offset to depth
			self.api_sail_depth = self.api_sail_depth_start + depth_offset
			# Log the sinus adjustment for debugging
			self.log(os.path.join(out_dir_t2t, self.file_name), 
					 f'Applied sinus wave: base={self.api_sail_depth_start}, '
					 f'offset={depth_offset}, result={self.api_sail_depth}\n')

		query = self.last_api_sail_query

		if 'use_all_trip' in data:
			if data['use_all_trip']:
				query = data['query']

		# Handle silent translation
		if 'translate' in data and data['translate'] is True:
			try:
				# Log the original query before translation (only in server logs)
				self.log(os.path.join(out_dir_t2t, self.file_name), 
						 f'Silently translating query: {query}\n')
				
				# Translate the query using the interface method
				query = self.interface.translate(query)
				
				# Log the translated query (only in server logs)
				self.log(os.path.join(out_dir_t2t, self.file_name), 
						 f'Translated query: {query}\n')
			except Exception as e:
				# Log error but continue with original query
				self.log(os.path.join(out_dir_t2t, self.file_name), 
						 f'Translation error: {str(e)}\n')

		try:
			if 'unload_llm' in data:
				if data['unload_llm'] is True:
					self.g.settings_data['unload_llm'] = True

			if data['add_search'] is True:
				query = f'{data["search"]}, {query}'

			if len(query) > 1000:
				query = extractive_summary(query, num_sentences=2)
				if len(query) > 1000:
					query = self.shorten_string(query)

			prompt = self.interface.retrieve_llm_completion(query)

			prompt = shared.clean_llm_artefacts(prompt)
			self.log(os.path.join(out_dir_t2t, self.query_file_name), f'{query}\n')
			self.log(os.path.join(out_dir_t2t, self.file_name), f'{prompt}\n')

			if data['summary'] is True:
				prompt = extractive_summary(prompt)

			if data['rephrase'] is True:
				prompt = self.interface.rephrase(prompt, data['rephrase_prompt'])

			if data['add_style'] is True:
				prompt = f'{data["style"]}, {prompt}'

			nodes = self.interface.direct_search(self.g.settings_data['sailing']['sail_text'],
												 self.api_sail_depth,
												 self.api_sail_count)
			self.api_sail_count += 1

			self.last_api_sail_query = self.get_next_target(nodes)

			negative_out = shared.get_negative_prompt()

			if query == -1:
				out_dict = {
					"prompt": f'sail is finished early due to rotating context',
					"neg_prompt": ''
				}
				return out_dict
			else:
				out_dict = {
					"prompt": prompt,
					"neg_prompt": negative_out
				}
				return out_dict
		except Exception as e:
			out_dict = {
				"prompt": 'some error happened: ' + str(e),
				"neg_prompt": ''
			}
			return out_dict

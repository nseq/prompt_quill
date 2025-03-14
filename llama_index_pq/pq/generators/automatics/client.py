# Copyright 2023 osiworx

# Licensed under the Apache License, Version 2.0 (the "License"); you
# may not use this file except in compliance with the License.  You
# may obtain a copy of the License at

# http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.  See the License for the specific language governing
# permissions and limitations under the License.

from datetime import datetime
import urllib.request
import base64
import json
import time
import os
import globals
from enhancer.prompts import PromptEnhance



webui_server_url = 'http://192.168.0.127:7860'

out_dir = 'api_out'
out_dir_t2i = os.path.join(out_dir, 'txt2img')
out_dir_i2i = os.path.join(out_dir, 'img2img')
os.makedirs(out_dir_t2i, exist_ok=True)
#os.makedirs(out_dir_i2i, exist_ok=True)



class automa_client:

    def __init__(self):
        self.webui_server_url = 'http://localhost:7860'
        self.g = globals.get_globals()
        self.prompt_enhancer = PromptEnhance()


    def timestamp(self):
        return datetime.fromtimestamp(time.time()).strftime("%Y%m%d-%H%M%S")


    def encode_file_to_base64(self,path):
        with open(path, 'rb') as file:
            return base64.b64encode(file.read()).decode('utf-8')


    def decode_and_save_base64(self,base64_str, save_path):
        with open(save_path, "wb") as file:
            file.write(base64.b64decode(base64_str))


    def call_api(self,api_endpoint, **payload):
        data = json.dumps(payload).encode('utf-8')
        request = urllib.request.Request(
            f'{self.webui_server_url}/{api_endpoint}',
            headers={'Content-Type': 'application/json'},
            data=data,
            method='POST'
        )
        try:
            response = urllib.request.urlopen(request)
            return json.loads(response.read().decode('utf-8'))
        except Exception as e:
            print(e)
            return ''

    def call_txt2img_api(self,**payload):
        response = self.call_api('sdapi/v1/txt2img', **payload)

        if response != '':
            return response
        else:
            return ''


    def call_img2img_api(self,**payload):
        response = self.call_api('sdapi/v1/img2img', **payload)
        for index, image in enumerate(response.get('images')):
            save_path = os.path.join(out_dir_i2i, f'img2img-{self.timestamp()}-{index}.png')
            self.decode_and_save_base64(image, save_path)


    def call_interrogation_api(self,**payload):
        response = self.call_api('sdapi/v1/interrogate', **payload)
        return response['caption']


    def get_ad_args(self, number, settings_data, prompt):

        ad_prompt = settings_data['automa'][f'automa_ad_prompt_{number}']
        if "face" in settings_data['automa'][f'automa_ad_model_{number}']:
            ad_prompt = self.prompt_enhancer.enhance_faces(ad_prompt, prompt, settings_data['automa'][f'automa_ad_model_{number}'])
        ad_prompt = self.prompt_enhancer.process_wildcards(ad_prompt)

        print(f'adetailer_{number} used this adetailer prompt: {ad_prompt}')

        args = {
            'ad_model': settings_data['automa'][f'automa_ad_model_{number}'],
            "ad_model_classes": "",
            "ad_tab_enable": True,
            "ad_prompt": ad_prompt,
            "ad_negative_prompt": settings_data['automa'][f'automa_ad_negative_prompt_{number}'],
            'ad_use_inpaint_width_height': settings_data['automa'][f'automa_ad_use_inpaint_width_height_{number}'],
            'ad_denoising_strength': settings_data['automa'][f'automa_ad_denoising_strength_{number}'],
            "ad_use_clip_skip": True,
            "ad_clip_skip": settings_data['automa'][f'automa_ad_clip_skip_{number}'],
            "ad_confidence": settings_data['automa'][f'automa_ad_confidence_{number}'],
            "ad_use_checkpoint": True,
            "ad_checkpoint": self.g.settings_data['automa'][f'automa_ad_checkpoint_{number}'],
            "ad_mask_blur": 8,
            "ad_inpaint_only_masked": True,
            "ad_inpaint_only_masked_padding": 32,
            "ad_mask_merge_invert": "None",
            "ad_restore_face": True

        #"ad_restore_face": settings_data['automa'][f'automa_ad_restore_face_{number}'],
            #"ad_use_steps": False,
            #"ad_steps": settings_data['automa'][f'automa_ad_steps_{number}']
        }

        #if settings_data['automa'][f'automa_ad_checkpoint_{number}'] != 'Same':
        #    args['ad_use_checkpoint'] = True
        #    args['ad_checkpoint'] = settings_data['automa'][f'automa_ad_checkpoint_{number}']
        #else:
        #    args['ad_use_checkpoint'] = False

        return args

    def get_adetailer(self, settings_data, prompt):
        ADetailer = {}

        number = 1
        while number <= 4:
            if settings_data['automa'][f'automa_adetailer_enable_{number}']:
                if not 'args' in ADetailer:
                    ADetailer['args'] = [True, False]
                ADetailer['args'].append(self.get_ad_args(number, settings_data, prompt))
            number += 1

        return ADetailer

    def request_generation(self,prompt, negative_prompt, settings_data):
        self.webui_server_url= settings_data['automa']["automa_url"]
        self.save = settings_data['automa']["automa_save"]

        ADetailer = self.get_adetailer(settings_data, prompt)
        alwayson_scripts = {}

        LayerDiffuse = {}
        if settings_data['automa']['automa_layerdiffuse_enable']:
            LayerDiffuse["args"] = [
                    {
                        #   "(SDXL) Only Generate Transparent Image (Attention Injection)"
                        "method": 5, # this number is the order the models are presented
                        "weight": 1.0,
                        "stop_at": 1.0,
                        "resize_mode": "Crop and Resize",
                        "blending": None,
                        "output_mat_for_i2i": False,
                        "fg_prompt": "",
                        "bg_prompt": "",
                        "blended_prompt": ""
                    }
                ]


        if 'args' in ADetailer and len(ADetailer['args']) > 2:
            alwayson_scripts["ADetailer"] = ADetailer

        if len(LayerDiffuse) > 0:
            alwayson_scripts["layerdiffuse"] = LayerDiffuse

        if type(prompt) == str:
            prompt = (str(prompt).encode('utf-8')).decode('utf-8')
        elif type(prompt) == bytes:
            prompt = prompt.decode('utf-8')

        if type(negative_prompt) == str:
            negative_prompt = (str(negative_prompt).encode('utf-8')).decode('utf-8')
        elif type(negative_prompt) == bytes:
            negative_prompt = negative_prompt.decode('utf-8')

        override_settings= {}

        if settings_data['automa']['automa_checkpoint'] != '' and settings_data['automa']['automa_checkpoint'] != 'None':
            override_settings["sd_model_checkpoint"] = settings_data['automa']['automa_checkpoint']

        if settings_data['automa']['automa_vae'] != '' and settings_data['automa']['automa_vae'] != 'None':
            override_settings["sd_vae"] = settings_data['automa']['automa_vae']

        if settings_data['automa']['automa_clip_skip'] > 0:
            override_settings["CLIP_stop_at_last_layers"] = settings_data['automa']['automa_clip_skip']

        payload = {
            "alwayson_scripts": alwayson_scripts,
            "prompt": prompt,  # extra networks also in prompts
            "negative_prompt": negative_prompt,
            "seed": settings_data['automa']["automa_seed"],
            "steps": settings_data['automa']["automa_steps"],
            "width": settings_data['automa']["automa_width"],
            "height": settings_data['automa']["automa_height"],
            "cfg_scale": settings_data['automa']["automa_cfg_scale"],
            "n_iter": settings_data['automa']["automa_n_iter"],
            "batch_size": settings_data['automa']["automa_batch"],
            "save_images":settings_data['automa']["automa_save_on_api_host"],
            "override_settings_restore_afterwards": settings_data['sailing']['sail_override_settings_restore'],

        }

        if settings_data['automa']['automa_sampler'] != 'None':
            payload["sampler_name"] = settings_data['automa']['automa_sampler']

        if override_settings != {}:
            payload["override_settings"] = override_settings

        # here we manage to set additional payloads for the new Forges API version
        if self.g.settings_data['automa']['automa_new_forge']:
            payload["scheduler"] = self.g.settings_data['automa']['automa_scheduler']


        return self.call_txt2img_api(**payload)



    def request_interrogation(self, image,url):
        self.webui_server_url=url
        payload = {
            "image": image,
            "model": "clip"
        }
        return self.call_interrogation_api(**payload)


    def get_api_endpoint(self,api_endpoint):
        request = urllib.request.Request(
            f'{self.webui_server_url}/{api_endpoint}',
            headers={'Content-Type': 'application/json'}
        )

        try:
            response = urllib.request.urlopen(request)
            return json.loads(response.read().decode('utf-8'))
        except Exception as e:
            print(e)
            return ''


    def post_api_endpoint(self,api_endpoint):
        endpoint = f"{self.webui_server_url}/{api_endpoint}"  # Assuming webui_server_url exists
        request = urllib.request.Request(
            endpoint,
            data=b'{}',  # Empty JSON payload—forces POST
            headers={'Content-Type': 'application/json'},
            method='POST'  # Explicit POST
        )
        try:
            response = urllib.request.urlopen(request)
        except Exception as e:
            print(e)
            return ''



    def get_samplers(self, url):
        self.webui_server_url = url
        samplers = self.get_api_endpoint('sdapi/v1/samplers')
        if samplers != '':
            sampler_array = ['None']
            for sampler in samplers:
                sampler_array.append(sampler['name'])

            return sampler_array
        else:
            return ["None"]


    def get_schedulers(self, url):
        self.webui_server_url = url
        schedulers = self.get_api_endpoint('sdapi/v1/schedulers')
        if schedulers != '':
            schedulers_array = []
            for schedulers in schedulers:
                schedulers_array.append(schedulers['label'])

            return schedulers_array
        else:
            return ["None"]

    def get_checkpoints(self, url):
        self.webui_server_url = url
        models = self.get_api_endpoint('sdapi/v1/sd-models')
        if models != '':
            model_array = ['None']
            for model in models:
                model_array.append(model['model_name'])

            return model_array
        else:
            return ["None"]

    def get_vaes(self, url):
        self.webui_server_url = url
        if self.g.settings_data['automa']['automa_new_forge']:
            vaes = self.get_api_endpoint('sdapi/v1/sd-modules')
        else:
            vaes = self.get_api_endpoint('sdapi/v1/sd-vae')
        if vaes != '':
            vae_array = ['None', 'Automatic']
            for model in vaes:
                vae_array.append(model['model_name'])

            return vae_array
        else:
            return ["None"]

    def get_loras(self, url):
        self.webui_server_url = url
        loras = self.get_api_endpoint('sdapi/v1/loras')
        if loras != '':
            loras_array = ['None']
            for lora in loras:
                loras_array.append(lora['name'])
            return loras_array
        else:
            return ["None"]

    def get_embeddings(self, url):
        self.webui_server_url = url
        embeddings = self.get_api_endpoint('sdapi/v1/embeddings')
        if embeddings != '':
            embeddings_array = ['None']
            for embedding in embeddings['loaded'].keys():
                embeddings_array.append(embedding)
            return embeddings_array
        else:
            return ["None"]

    def check_avail(self, url):
        self.webui_server_url = url
        if self.g.settings_data['automa']['automa_new_forge']:
            vaes = self.get_api_endpoint('sdapi/v1/sd-modules')
        else:
            vaes = self.get_api_endpoint('sdapi/v1/sd-vae')
        if vaes != '':
            return 'API OK'
        else:
            return 'API NOT OK'

    def unload_checkpoint(self):
        self.post_api_endpoint('sdapi/v1/unload-checkpoint')

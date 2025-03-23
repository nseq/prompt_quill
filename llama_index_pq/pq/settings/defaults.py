default = {
    "translate": False,
    "batch": False,
    "summary": False,
    "Temperature": 0.0,
    "Context Length": 3900,
    "GPU Layers": 50,
    "max output Tokens": 200,
    "top_k": 5,
    "max_top_k": 50,
    "Instruct Model": False,
    "unload_llm": False,
    "collection": "prompts_ng_gte",
    "collections_list": ["prompts_ng_gte"],


    "llm_settings": {
        "top_p": 1.0,
        "min_p": 0.05,
        "typical_p": 1.0,
        "frequency_penalty": 0.0,
        "presence_penalty": 0.0,
        "repeat_penalty": 1.0,
        "top_k": 0  # Overrides the earlier top_k=5 to match your completion_chunks
    },


    "rephrase_instruction": """create a text to image prompt based on the context and the query,
You mix a new prompt based on the context and the query. The query is just adding a detail to the original context""",

    "preset_list": [],
    "selected_preset": "",

    "horde": {
        "horde_api_key": "0000000000",
        "horde_model": "Deliberate 3.0",
        "horde_sampler": "k_dpmpp_2s_a",
        "horde_steps": 20,
        "horde_cfg_scale": 7,
        "horde_width": 768,
        "horde_height": 512,
        "horde_clipskip": 2,
    },

    "automa": {
        "automa_sampler": "DPM++ 2M Karras",
        "automa_seed": -1,
        "automa_checkpoint": "",
        "automa_vae": "",
        "automa_alt_vae": "",
        "automa_steps": 20,
        "automa_cfg_scale": 7,
        "automa_clip_skip": 0,
        "automa_width": 768,
        "automa_height": 512,
        "automa_url": "http://localhost:7860",
        "automa_save": True,
        "automa_batch": 1,
        "automa_n_iter": 1,
        "automa_save_on_api_host": False,
        "automa_adetailer_enable": False,
        "automa_adetailer_render_both": False,
        "automa_new_forge": False,
        "automa_checkpoints": [],
        "automa_samplers": [],
        "automa_schedulers": [],
        "automa_loras":[],
        "automa_embeddings":[],
        "automa_scheduler": 'Automatic',
        "automa_vaes": [],
        "automa_layerdiffuse_enable": False,

        "automa_ad_use_inpaint_width_height_1": False,
        "automa_ad_model_1": "",
        "automa_ad_denoising_strength_1": 0.2,
        "automa_ad_clip_skip_1": 2,
        "automa_ad_confidence_1": 0.6,
        "automa_ad_checkpoint_1": None,
        "automa_adetailer_enable_1": False,
        "automa_ad_prompt_1": "",
        "automa_ad_negative_prompt_1": "",
        "automa_ad_mask_blur_1": 8,
        "automa_ad_inpaint_only_masked_1": True,
        "automa_ad_inpaint_only_masked_padding_1": 64,
        "automa_ad_mask_merge_invert_1": "None",
        "automa_ad_restore_face_1": True,
        "automa_ad_sep_prompt_1": "",

        "automa_ad_use_inpaint_width_height_2": False,
        "automa_ad_model_2": "",
        "automa_ad_denoising_strength_2": 0.2,
        "automa_ad_clip_skip_2": 2,
        "automa_ad_confidence_2": 0.6,
        "automa_ad_checkpoint_2": None,
        "automa_adetailer_enable_2": False,
        "automa_ad_prompt_2": "",
        "automa_ad_negative_prompt_2": "",
        "automa_ad_mask_blur_2": 8,
        "automa_ad_inpaint_only_masked_2": True,
        "automa_ad_inpaint_only_masked_padding_2": 64,
        "automa_ad_mask_merge_invert_2": "None",
        "automa_ad_restore_face_2": True,
        "automa_ad_sep_prompt_2": "",

        "automa_ad_use_inpaint_width_height_3": False,
        "automa_ad_model_3": "",
        "automa_ad_denoising_strength_3": 0.2,
        "automa_ad_clip_skip_3": 2,
        "automa_ad_confidence_3": 0.6,
        "automa_ad_checkpoint_3": None,
        "automa_adetailer_enable_3": False,
        "automa_ad_prompt_3": "",
        "automa_ad_negative_prompt_3": "",
        "automa_ad_mask_blur_3": 8,
        "automa_ad_inpaint_only_masked_3": True,
        "automa_ad_inpaint_only_masked_padding_3": 64,
        "automa_ad_mask_merge_invert_3": "None",
        "automa_ad_restore_face_3": True,
        "automa_ad_sep_prompt_3": "",

        "automa_ad_use_inpaint_width_height_4": False,
        "automa_ad_model_4": "",
        "automa_ad_denoising_strength_4": 0.2,
        "automa_ad_clip_skip_4": 2,
        "automa_ad_confidence_4": 0.6,
        "automa_ad_checkpoint_4": None,
        "automa_adetailer_enable_4": False,
        "automa_ad_prompt_4": "",
        "automa_ad_negative_prompt_4": "",
        "automa_ad_mask_blur_4": 8,
        "automa_ad_inpaint_only_masked_4": True,
        "automa_ad_inpaint_only_masked_padding_4": 64,
        "automa_ad_mask_merge_invert_4": "None",
        "automa_ad_restore_face_4": True,
        "automa_ad_sep_prompt_4": "",

    },

    "sailing": {
        "sail_text": "",
        "sail_keep_text": False,
        "sail_width": 10,
        "sail_depth": 10,
        "sail_generate": False,
        "sail_target": True,
        "sail_sinus": False,
        "sail_sinus_freq": 0.1,
        "sail_sinus_range": 10,
        "sail_add_style": False,
        "sail_style": "",
        "sail_add_search": False,
        "sail_search": "",
        "sail_max_gallery_size": 6,
        "sail_summary": False,
        "sail_rephrase_prompt": "",
        "sail_rephrase": False,
        "sail_gen_rephrase": False,
        "sail_dyn_neg": False,
        "sail_add_neg": False,
        "sail_neg_prompt": "",
        "sail_filter_text": "",
        "sail_filter_not_text": "",
        "sail_filter_context": False,
        "sail_filter_prompt": False,
        "sail_neg_filter_text": "",
        "sail_neg_filter_not_text": "",
        "sail_neg_filter_context": False,
        "sail_checkpoint": [],
        "sail_sampler": [],
        "sail_vae": [],
        "sail_scheduler": ['Automatic'],
        "sail_dimensions": ["1024,1024"],
        "sail_gen_any_combination": False,
        "sail_gen_type": "Linear",
        "sail_gen_steps": 10,
        "sail_gen_enabled": False,
        "sail_override_settings_restore": False,
        "sail_store_folders": False,
        "sail_depth_preset": 1,
        "sail_unload_llm": False,
        "sail_neg_embed": "",
        "sail_pos_embed": "",
        "sail_quality": "",
        "reset_model": True,
        "sail_wildcards_only": True
    },

    "model_test": {
        "model_test_steps": [20, 25, 30],
        "model_test_cfg": [5, 6, 7],
        "model_test_dimensions": ["720,1440", "1024,1024", "1024,1536"],
        "model_test_steps_list": [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65],
        "model_test_cfg_list": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "model_test_dimensions_list": ["512,512", "768,512", "512,768", "640,1600", "1600,640", "720,1440", "1440,720",
                                       "816,1280", "1280,816", "864,1200", "1200,864", "928,1120", "1120,928", "1024,1024",
                                       "1536,1024", "1024,1536"],

        "model_test_list": "Character",
        "model_test_type": "Largest List",
        "model_test_gen_type": "Largest List",
        "model_test_setup": {
            "Character": ["man"],
            "Air Creatures": ["phoenix"],
            "Land Creatures": ["dog"],
            "Sea Creatures": ["shark"],
            "Character Objects": ["knife"],
            "Character Adjectives": ["armored"],
            "Air Vehicle": ["fighter jet"],
            "Land Vehicle": ["tank"],
            "Sea Vehicle": ["ship"],
            "Space Vehicle": ["spaceship"],
            "Moving relation": ["docking with a"],
            "Still relation": ["near a"],
            "Object Adjectives": ["futuristic"],
            "Visual Adjectives": ["pretty"],
            "Visual Qualities": ["realistic"],
            "Setup": ["street"],
            "Colors": ["purple"],
            "Styles": ["Food Photography"],
            "Artists": ["Alvar Aalto"],
            "Things": ["Ball"],
            "Celebrities": ["Albert Einstein"]
        },
    },

    "interrogate": {

        "moon_low_mem": False,

        "story_teller_enabled": False,
        "story_teller_seconds_step_enabled": False,
        "image_description_model": "llava:7b-v1.6-vicuna-q2_K (Q2_K, 3.2GB)",
        "image_description_system_context": "You are an assistant who describes the content and composition of images. Describe only what you see in the image, not what you think the image is about.Be factual and literal. Do not use metaphors or similes. Be concise.",
        "image_description_prompt": "Give a most detailed desciption of the image, describe any detail and also the mood the image is presenting, give a hint if the image is dramatic or funny or what ever matches the image best.",

        "story_teller_system_context": "You are an vibrant story teller, you tell fantastic detailed storys about a image description thats given.Be factual and literal. Do not use metaphors or similes. Be concise.",
        "story_teller_prompt": "Tell a vibrant, colorful told story about the following image description. Make it dramatic, funny or anyway matching the mood of the image. the image description follows here:",


        "story_teller_host": "http://localhost:11434",
        "story_teller_timeout": 300,
        "story_teller_temperature": 0.4,
        "story_teller_max_tokens": 300,
        "image_description_models": ["llava:7b-v1.6-vicuna-q2_K (Q2_K, 3.2GB)",
                                     "llava:7b-v1.6-mistral-q2_K (Q2_K, 3.3GB)",
                                     "llava:7b-v1.6 (Q4_0, 4.7GB)",
                                     "llava:13b-v1.6 (Q4_0, 8.0GB)",
                                     "llava:34b-v1.6 (Q4_0, 20.0GB)",
                                     "llava-llama3:8b (Q4_K_M, 5.5GB)",
                                     "llava-phi3:3.8b (Q4_K_M, 2.9GB)",
                                     "moondream:1.8b (Q4, 1.7GB)",
                                     "moondream:1.8b-v2-q6_K (Q6, 2.1GB)",
                                     "moondream:1.8b-v2-fp16 (F16, 3.7GB)"],
        "story_teller_models": ["dolphin-llama3:8b",
                                "dolphin-phi"],
        "story_teller_model": "dolphin-llama3:8b",

        "molmo_max_new_tokens": 350,
        "molmo_temperature": 0.6,
        "molmo_top_k": 40,
        "molmo_top_p": 0.9,
        "molmo_unload_model_after_generation": False,
        "molmo_story_teller_enabled": False,
        "molmo_story_teller_prompt": "Tell a story about this",
        "molmo_file_renamer_prompt": "Create a filename no longer than 8 words from this",
        "molmo_path": "",
        "molmo_temperatur": 0.6,
        "molmo_folder_name": "",
        "molmo_source_folder_name":"",
        "molmo_destination_folder_name":"",
        "molmo_organize_prompt":"",
        "iti_folder_name": "",
        "iti_file_renamer_prompt": "",
        "iti_description_prompt": ""
    },

    "iti": {
        "enhance_prompt": False,
        "input_folder": "C:/Images/TannedModels",
        "output_dirs": {
            "good": "./good",
            "drafts": "./drafts"
        },
        "molmo": {
            "prompt_style": "Describe colors, style, and key elements for Stable Diffusion",
            "max_tokens": 100,
            "refine_max_tokens": 200,
            "negative_prompt": False,
            "custom_prompt": "",
            "refine_prompt": ""
        },
        "automa": {
            "negative_prompt": "",
            "image_count": 1
        },
        "scorers": {
            "clip": {"enabled": True, "weight": 0.3},
            "ssim": {"enabled": True, "weight": 0.15},
            "color": {"enabled": True, "weight": 0.1},
            "phash": {"enabled": True, "weight": 0.1},
            "aesthetic": {"enabled": True, "weight": 0.15},
            "detail": {"enabled": True, "weight": 0.15},
            "gen_clip": {"enabled": True, "weight": 0.15},
            "blur": {"enabled": True, "weight": 0.15},
            "artifacts": {"enabled": True, "weight": 0.15}

        },
        "scorers_single": {
            "aesthetic": {"enabled": True, "weight": 0.25},
            "detail": {"enabled": True, "weight": 0.20},
            "gen_clip": {"enabled": True, "weight": 0.25},
            "blur": {"enabled": True, "weight": 0.15},
            "artifacts": {"enabled": True, "weight": 0.15}
        },
        "refinement": {
            "max_iterations": 5,
            "target_score": 80,
            "llm_max_tokens": 50,
            "feedback_style": "detailed",
            "revert_on_drop": True,
            "early_stop_gain": 5,
            "improvement_threshold": 20,  # New!
            "combo_size": 20,
            "enable_model_cycle": False,
            "enhance_prompt": False,
            "cycle_enhance_prompt": False
        },
        "output": {
            "save_metadata": False,
            "log_file": "./iti_log.txt"
        },
        "meta_prompt": """{instruction_start}Context information is below.\n---------------------\n{context}\n---------------------\nYou are an expert in creating prompts for text-to-image generation models like Stable Diffusion.Your task is to refine the prompt to boost weak scores.Output ONLY a comma-separated list of 50+ tokens—short keywords or phrases for subject, details,style, mood, and quality. Focus on style, colors, composition. Order matters: start with image-specific tokens, end with quality/style. No explanations, no sentences.{user_pattern}USER: Refine the prompt now.{assistant_pattern}""",
        "prompt": {
            "pos_style": "",
            "pos_lora": "",
            "neg_style": "",
            "neg_lora": "",
        },
        "sailing": {
            "enable_sailing_step": False,
            "enable_sailing": False,
            "sail_enhance_prompt": False,
            "sail_steps": 5,
            "sail_sampler": "",
            "sail_scheduler": "",
            "sail_checkpoint": "",
            "sail_vae": "",
            "pos_sail_embedding": "",
            "neg_sail_embedding": "",
            "pos_sail_lora": "",
            "neg_sail_lora": ""
        },
        "research": {
            "prompts": [["", ""], ["", ""], ["", ""]]
        },
        "model_lists": {
            "models": ["artcore_v10", "rundiffusionXL_beta"],
            "loras": ["add_details_xl", "SDXLHighDetail_v5"]
        }
    },


    "embedding_model": "BAAI/bge-base-en-v1.5",
    "embedding_model_list": ["sentence-transformers/all-MiniLM-L12-v2", "BAAI/bge-base-en-v1.5"],
    "selected_template": "prompt_template_a",
    "LLM Model": "TheBloke/Panda-7B-v0.1-GGUF-Q4",
    "model_list": {
        "unsloth/DeepSeek-R1-Distill-Qwen-7B-GGUF-Q5":
            {
                "name": "unsloth/DeepSeek-R1-Distill-Qwen-7B-GGUF-Q5",
                "path": "https://huggingface.co/unsloth/DeepSeek-R1-Distill-Qwen-7B-GGUF/resolve/main/DeepSeek-R1-Distill-Qwen-7B-Q5_K_M.gguf",
                "instruction_start": "### Instruction:\n",
                "start_pattern": "",
                "user_pattern": "",
                "assistant_pattern": "ASSISTANT:",
                "context_window": 4096,
                "repo_id":"unsloth/DeepSeek-R1-Distill-Qwen-7B-GGUF",
                "filename":"DeepSeek-R1-Distill-Qwen-7B-Q5_K_M.gguf"
            },

        "TheBloke/Uncensored-Jordan-7B-GGUF-Q4":
            {
                "name": "TheBloke/Uncensored-Jordan-7B-GGUF-Q4",
                "path": "https://huggingface.co/TheBloke/Uncensored-Jordan-7B-GGUF/resolve/main/uncensored-jordan-7b.Q4_K_M.gguf",
                "instruction_start": "### Instruction:\n",
                "start_pattern": "",
                "user_pattern": "",
                "assistant_pattern": "ASSISTANT:",
                "context_window": 4096,
                "repo_id":"TheBloke/Uncensored-Jordan-7B-GGUF",
                "filename":"uncensored-jordan-7b.Q4_K_M.gguf"
            },
        "TheBloke/Uncensored-Jordan-7B-GGUF-Q5":
            {
                "name": "TheBloke/Uncensored-Jordan-7B-GGUF-Q5",
                "path": "https://huggingface.co/TheBloke/Uncensored-Jordan-7B-GGUF/resolve/main/uncensored-jordan-7b.Q5_K_M.gguf",
                "instruction_start": "### Instruction:\n",
                "start_pattern": "",
                "user_pattern": "",
                "assistant_pattern": "ASSISTANT:",
                "context_window": 4096
            },
        "TheBloke/Luna-AI-Llama2-Uncensored-GGUF-Q4":
            {
                "name": "TheBloke/Luna-AI-Llama2-Uncensored-GGUF-Q4",
                "path": "https://huggingface.co/TheBloke/Luna-AI-Llama2-Uncensored-GGUF/resolve/main/luna-ai-llama2-uncensored.Q4_K_M.gguf",
                "instruction_start": "### Instruction:\n",
                "start_pattern": "",
                "user_pattern": "",
                "assistant_pattern": "### Response:\nASSISTANT:",
                "context_window": 4096
            },
        "TheBloke/Luna-AI-Llama2-Uncensored-GGUF-Q5":
            {
                "name": "TheBloke/Luna-AI-Llama2-Uncensored-GGUF-Q5",
                "path": "https://huggingface.co/TheBloke/Luna-AI-Llama2-Uncensored-GGUF/resolve/main/luna-ai-llama2-uncensored.Q5_K_M.gguf",
                "instruction_start": "### Instruction:\n",
                "start_pattern": "",
                "user_pattern": "",
                "assistant_pattern": "### Response:\nASSISTANT:",
                "context_window": 4096
            },



        "TheBloke/Speechless-Llama2-Hermes-Orca-Platypus-WizardLM-13B-GGUF-Q4":
            {
                "name": "TheBloke/Speechless-Llama2-Hermes-Orca-Platypus-WizardLM-13B-GGUF-Q4",
                "path": "https://huggingface.co/TheBloke/Speechless-Llama2-Hermes-Orca-Platypus-WizardLM-13B-GGUF/resolve/main/speechless-llama2-hermes-orca-platypus-wizardlm-13b.Q4_K_M.gguf",
                "instruction_start": "### Instruction:\n",
                "start_pattern": "<START>\n",
                "user_pattern": "",
                "assistant_pattern": "### Response:\n ASSISTANT:",
                "context_window": 4096
            },
        "microsoft/Phi-3-mini-4k-instruct-gguf-Q4":
            {
                "name": "microsoft/Phi-3-mini-4k-instruct-gguf-Q4",
                "path": "https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-gguf/resolve/main/Phi-3-mini-4k-instruct-q4.gguf",
                "instruction_start": "<s>",
                "start_pattern": "<START>\n",
                "user_pattern": "<|user|>\n",
                "assistant_pattern": "<|end|>\n<|assistant|>\n",
                "context_window": 4096
            },
        "TheBloke/phi-2-GGUF-Q3":
            {
                "name": "TheBloke/phi-2-GGUF-Q3",
                "path": "https://huggingface.co/TheBloke/phi-2-GGUF/resolve/main/phi-2.Q3_K_M.gguf",
                "instruction_start": "",
                "start_pattern": "",
                "user_pattern": "Instruct:",
                "assistant_pattern": "Output:",
                "context_window": 2048
            },
        "TheBloke/phi-2-GGUF-Q5":
            {
                "name": "TheBloke/phi-2-GGUF-Q5",
                "path": "https://huggingface.co/TheBloke/phi-2-GGUF/resolve/main/phi-2.Q5_K_M.gguf",
                "instruction_start": "",
                "start_pattern": "",
                "user_pattern": "Instruct:",
                "assistant_pattern": "Output:",
                "context_window": 2048
            },

        "TheBloke/openchat-3.5-0106-GGUF-Q5":
            {
                "name": "TheBloke/openchat-3.5-0106-GGUF-Q5",
                "path": "https://huggingface.co/TheBloke/openchat-3.5-0106-GGUF/resolve/main/openchat-3.5-0106.Q5_K_M.gguf",
                "instruction_start": "GPT4 Correct User:",
                "start_pattern": "<START>\n",
                "user_pattern": "",
                "assistant_pattern": "<|end_of_turn|>GPT4 Correct Assistant: ASSISTANT:",
                "context_window": 8192
            },
        "TheBloke/openchat-3.5-0106-GGUF-Q3":
            {
                "name": "TheBloke/openchat-3.5-0106-GGUF-Q3",
                "path": "https://huggingface.co/TheBloke/openchat-3.5-0106-GGUF/resolve/main/openchat-3.5-0106.Q3_K_M.gguf",
                "instruction_start": "GPT4 Correct User:",
                "start_pattern": "<START>\n",
                "user_pattern": "",
                "assistant_pattern": "<|end_of_turn|>GPT4 Correct Assistant: ASSISTANT:",
                "context_window": 8192
            },
        "TheBloke/openchat-3.5-0106-GGUF-Q4":
            {
                "name": "TheBloke/openchat-3.5-0106-GGUF-Q4",
                "path": "https://huggingface.co/TheBloke/openchat-3.5-0106-GGUF/resolve/main/openchat-3.5-0106.Q4_K_M.gguf",
                "instruction_start": "GPT4 Correct User:",
                "start_pattern": "<START>\n",
                "user_pattern": "",
                "assistant_pattern": "<|end_of_turn|>GPT4 Correct Assistant: ASSISTANT:",
                "context_window": 8192
            },
        "TheBloke/Llama-2-13B-chat-GGUF-Q4":
            {
                "name": "TheBloke/Llama-2-13B-chat-GGUF-Q4",
                "path": "https://huggingface.co/TheBloke/Llama-2-13B-chat-GGUF/resolve/main/llama-2-13b-chat.Q4_K_M.gguf",
                "instruction_start": "### Instruction:\n",
                "start_pattern": "<START>\n",
                "user_pattern": "",
                "assistant_pattern": "### Response:\n ASSISTANT:",
                "context_window": 4096
            },
        "TheBloke/Llama-2-13B-chat-GGUF-Q3":
            {
                "name": "TheBloke/Llama-2-13B-chat-GGUF-Q3",
                "path": "https://huggingface.co/TheBloke/Llama-2-13B-chat-GGUF/resolve/main/llama-2-13b-chat.Q3_K_M.gguf",
                "instruction_start": "### Instruction:\n",
                "start_pattern": "<START>\n",
                "user_pattern": "",
                "assistant_pattern": "### Response:\n ASSISTANT:",
                "context_window": 4096
            },
        "TheBloke/WestLake-7B-v2-GGUF-Q4":
            {
                "name": "TheBloke/WestLake-7B-v2-GGUF-Q4",
                "path": "https://huggingface.co/TheBloke/WestLake-7B-v2-GGUF/resolve/main/westlake-7b-v2.Q4_K_M.gguf",
                "instruction_start": "### Instruction:\n",
                "start_pattern": "<START>\n",
                "user_pattern": "",
                "assistant_pattern": "### Response:\n ASSISTANT:",
                "context_window": 32768
            },
        "TheBloke/WestLake-7B-v2-GGUF-Q3":
            {
                "name": "TheBloke/WestLake-7B-v2-GGUF-Q3",
                "path": "https://huggingface.co/TheBloke/WestLake-7B-v2-GGUF/resolve/main/westlake-7b-v2.Q3_K_M.gguf",
                "instruction_start": "### Instruction:\n",
                "start_pattern": "<START>\n",
                "user_pattern": "",
                "assistant_pattern": "### Response:\n ASSISTANT:",
                "context_window": 32768
            },
        "TheBloke/Rosa_v2_7B-GGUF-Q4":
            {
                "name": "TheBloke/Rosa_v2_7B-GGUF-Q4",
                "path": "https://huggingface.co/TheBloke/Rosa_v2_7B-GGUF/resolve/main/rosa_v2_7b.Q4_K_M.gguf",
                "instruction_start": "[INST]",
                "start_pattern": "",
                "user_pattern": "",
                "assistant_pattern": "[/INST]ASSISTANT:",
                "context_window": 32768
            },
        "TheBloke/Rosa_v2_7B-GGUF-Q3":
            {
                "name": "TheBloke/Rosa_v2_7B-GGUF-Q3",
                "path": "https://huggingface.co/TheBloke/Rosa_v2_7B-GGUF/resolve/main/rosa_v2_7b.Q3_K_M.gguf",
                "instruction_start": "[INST]",
                "start_pattern": "",
                "user_pattern": "",
                "assistant_pattern": "[/INST]ASSISTANT:",
                "context_window": 32768
            },
        "TheBloke/Panda-7B-v0.1-GGUF-Q4":
            {
                "name": "TheBloke/Panda-7B-v0.1-GGUF-Q4",
                "path": "https://huggingface.co/TheBloke/Panda-7B-v0.1-GGUF/resolve/main/panda-7b-v0.1.Q4_K_M.gguf",
                "instruction_start": "[INST]",
                "start_pattern": "<START>\n",
                "user_pattern": "",
                "assistant_pattern": "[/INST]ASSISTANT:",
                "context_window": 32768
            },
        "TheBloke/Panda-7B-v0.1-GGUF-Q3":
            {
                "name": "TheBloke/Panda-7B-v0.1-GGUF-Q3",
                "path": "https://huggingface.co/TheBloke/Panda-7B-v0.1-GGUF/resolve/main/panda-7b-v0.1.Q3_K_M.gguf",
                "instruction_start": "[INST]",
                "start_pattern": "<START>\n",
                "user_pattern": "",
                "assistant_pattern": "[/INST]ASSISTANT:",
                "context_window": 32768
            },
        "TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF-Q5":
            {
                "name": "TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF-Q5",
                "path": "https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF/resolve/main/tinyllama-1.1b-chat-v1.0.Q5_K_M.gguf",
                "instruction_start": "",
                "start_pattern": "<START>\n",
                "user_pattern": "",
                "assistant_pattern": "ASSISTANT:",
                "context_window": 32768
            },
        "TheBloke/bling-stable-lm-3b-4e1t-v0-GGUF-Q5":
            {
                "name": "TheBloke/bling-stable-lm-3b-4e1t-v0-GGUF-Q5",
                "path": "https://huggingface.co/TheBloke/bling-stable-lm-3b-4e1t-v0-GGUF/resolve/main/bling-stable-lm-3b-4e1t-v0.Q5_K_M.gguf",
                "instruction_start": "### Instruction:\n",
                "start_pattern": "<START>\n",
                "user_pattern": "",
                "assistant_pattern": "### Response:\n ASSISTANT:",
                "context_window": 4096
            },
        "TheBloke/bling-stable-lm-3b-4e1t-v0-GGUF-Q4":
            {
                "name": "TheBloke/bling-stable-lm-3b-4e1t-v0-GGUF-Q4",
                "path": "https://huggingface.co/TheBloke/bling-stable-lm-3b-4e1t-v0-GGUF/resolve/main/bling-stable-lm-3b-4e1t-v0.Q4_K_M.gguf",
                "instruction_start": "### Instruction:\n",
                "start_pattern": "<START>\n",
                "user_pattern": "",
                "assistant_pattern": "### Response:\n ASSISTANT:",
                "context_window": 4096
            },
        "TheBloke/Sonya-7B-GGUF-Q4":
            {
                "name": "TheBloke/Sonya-7B-GGUF-Q4",
                "path": "https://huggingface.co/TheBloke/Sonya-7B-GGUF/resolve/main/sonya-7b.Q4_K_M.gguf",
                "instruction_start": "### Instruction:\n",
                "start_pattern": "<START>\n",
                "user_pattern": "",
                "assistant_pattern": "### Response:\n ASSISTANT:",
                "context_window": 8192
            },
        "TheBloke/Sonya-7B-GGUF-Q3":
            {
                "name": "TheBloke/Sonya-7B-GGUF-Q3",
                "path": "https://huggingface.co/TheBloke/Sonya-7B-GGUF/resolve/main/sonya-7b.Q3_K_M.gguf",
                "instruction_start": "### Instruction:\n",
                "start_pattern": "<START>\n",
                "user_pattern": "",
                "assistant_pattern": "### Response:\n ASSISTANT:",
                "context_window": 8192
            },
        "TheBloke/Lelantos-7B-GGUF-Q4":
            {
                "name": "TheBloke/Lelantos-7B-GGUF-Q4",
                "path": "https://huggingface.co/TheBloke/Lelantos-7B-GGUF/resolve/main/lelantos-7b.Q4_K_M.gguf",
                "instruction_start": "<|im_start|>user\n",
                "start_pattern": "",
                "user_pattern": "",
                "assistant_pattern": "\n<|im_end|>\n<|im_start|>assistant\n ASSISTANT:",
                "context_window": 8192
            },
        "TheBloke/Lelantos-7B-GGUF-Q3":
            {
                "name": "TheBloke/Lelantos-7B-GGUF-Q3",
                "path": "https://huggingface.co/TheBloke/Lelantos-7B-GGUF/resolve/main/lelantos-7b.Q3_K_M.gguf",
                "instruction_start": "<|im_start|>user\n",
                "start_pattern": "",
                "user_pattern": "",
                "assistant_pattern": "\n<|im_end|>\n<|im_start|>assistant\n ASSISTANT:",
                "context_window": 8192
            },
        "TheBloke/Luna-AI-Llama2-Uncensored-GGUF-Q5":
            {
                "name": "TheBloke/Luna-AI-Llama2-Uncensored-GGUF-Q5",
                "path": "https://huggingface.co/TheBloke/Luna-AI-Llama2-Uncensored-GGUF/resolve/main/luna-ai-llama2-uncensored.Q5_K_M.gguf",
                "instruction_start": "### Instruction:\n",
                "start_pattern": "<START>\n",
                "user_pattern": "",
                "assistant_pattern": "### Response:\n ASSISTANT:",
                "context_window": 2048
            },
        "TheBloke/Luna-AI-Llama2-Uncensored-GGUF-Q3":
            {
                "name": "TheBloke/Luna-AI-Llama2-Uncensored-GGUF-Q3",
                "path": "https://huggingface.co/TheBloke/Luna-AI-Llama2-Uncensored-GGUF/resolve/main/luna-ai-llama2-uncensored.Q3_K_M.gguf",
                "instruction_start": "### Instruction:\n",
                "start_pattern": "<START>\n",
                "user_pattern": "",
                "assistant_pattern": "### Response:\n ASSISTANT:",
                "context_window": 2048
            },
        "TheBloke/Spicyboros-7B-2.2-GGUF-Q5":
            {
                "name": "TheBloke/Spicyboros-7B-2.2-GGUF-Q5",
                "path": "https://huggingface.co/TheBloke/Spicyboros-7B-2.2-GGUF/resolve/main/spicyboros-7b-2.2.Q5_K_M.gguf",
                "instruction_start": "### Instruction:\n",
                "start_pattern": "<START>\n",
                "user_pattern": "",
                "assistant_pattern": "### Response:\n ASSISTANT:",
                "context_window": 4096
            },
        "TheBloke/Spicyboros-7B-2.2-GGUF-Q3":
            {
                "name": "TheBloke/Spicyboros-7B-2.2-GGUF-Q3",
                "path": "https://huggingface.co/TheBloke/Spicyboros-7B-2.2-GGUF/resolve/main/spicyboros-7b-2.2.Q3_K_M.gguf",
                "instruction_start": "### Instruction:\n",
                "start_pattern": "<START>\n",
                "user_pattern": "",
                "assistant_pattern": "### Response:\n ASSISTANT:",
                "context_window": 4096
            },
        "TheBloke/Wizard-Vicuna-7B-Uncensored-GGUF-Q5":
            {
                "name": "TheBloke/Wizard-Vicuna-7B-Uncensored-GGUF-Q5",
                "path": "https://huggingface.co/TheBloke/Wizard-Vicuna-7B-Uncensored-GGUF/resolve/main/Wizard-Vicuna-7B-Uncensored.Q5_K_M.gguf",
                "instruction_start": "### Human:",
                "start_pattern": "<START>\n",
                "user_pattern": "",
                "assistant_pattern": "### Assistant: ASSISTANT:",
                "context_window": 2048
            },
        "TheBloke/Wizard-Vicuna-7B-Uncensored-GGUF-Q3":
            {
                "name": "TheBloke/Wizard-Vicuna-7B-Uncensored-GGUF-Q3",
                "path": "https://huggingface.co/TheBloke/Wizard-Vicuna-7B-Uncensored-GGUF/resolve/main/Wizard-Vicuna-7B-Uncensored.Q3_K_M.gguf",
                "instruction_start": "### Human:",
                "start_pattern": "<START>\n",
                "user_pattern": "",
                "assistant_pattern": "### Assistant: ASSISTANT:",
                "context_window": 2048
            },
        "TheBloke/llama2_7b_chat_uncensored-GGUF-Q5":
            {
                "name": "TheBloke/llama2_7b_chat_uncensored-GGUF-Q5",
                "path": "https://huggingface.co/TheBloke/llama2_7b_chat_uncensored-GGUF/resolve/main/llama2_7b_chat_uncensored.Q5_K_M.gguf",
                "instruction_start": "[INST] <<SYS>>\ncreate fantastic text to image prompts.\n<</SYS>>",
                "start_pattern": "<START>\n",
                "user_pattern": "",
                "assistant_pattern": "[/INST] ASSISTANT:",
                "context_window": 2048
            },
        "TheBloke/llama2_7b_chat_uncensored-GGUF-Q3":
            {
                "name": "TheBloke/llama2_7b_chat_uncensored-GGUF-Q3",
                "path": "https://huggingface.co/TheBloke/llama2_7b_chat_uncensored-GGUF/resolve/main/llama2_7b_chat_uncensored.Q3_K_M.gguf",
                "instruction_start": "[INST] <<SYS>>\ncreate fantastic text to image prompts.\n<</SYS>>",
                "start_pattern": "<START>\n",
                "user_pattern": "",
                "assistant_pattern": "[/INST] ASSISTANT:",
                "context_window": 2048
            },
        "TheBloke/Guanaco-7B-Uncensored-GGUF-Q5":
            {
                "name": "TheBloke/Guanaco-7B-Uncensored-GGUF-Q5",
                "path": "https://huggingface.co/TheBloke/Guanaco-7B-Uncensored-GGUF/resolve/main/guanaco-7b-uncensored.Q5_K_M.gguf",
                "instruction_start": "### Human:",
                "start_pattern": "<START>\n",
                "user_pattern": "",
                "assistant_pattern": "### Assistant: ASSISTANT:",
                "context_window": 4096
            },
        "TheBloke/Guanaco-7B-Uncensored-GGUF-Q3":
            {
                "name": "TheBloke/Guanaco-7B-Uncensored-GGUF-Q3",
                "path": "https://huggingface.co/TheBloke/Guanaco-7B-Uncensored-GGUF/resolve/main/guanaco-7b-uncensored.Q3_K_M.gguf",
                "instruction_start": "### Human:",
                "start_pattern": "<START>\n",
                "user_pattern": "",
                "assistant_pattern": "### Assistant: ASSISTANT:",
                "context_window": 4096
            },
        "TheBloke/Uncensored-Jordan-7B-GGUF-Q5":
            {
                "name": "TheBloke/Uncensored-Jordan-7B-GGUF-Q5",
                "path": "https://huggingface.co/TheBloke/Uncensored-Jordan-7B-GGUF/resolve/main/uncensored-jordan-7b.Q5_K_M.gguf",
                "instruction_start": "### Instruction:\n",
                "start_pattern": "<START>\n",
                "user_pattern": "",
                "assistant_pattern": "### Response:\n ASSISTANT:",
                "context_window": 2048
            },
        "TheBloke/Uncensored-Jordan-7B-GGUF-Q3":
            {
                "name": "TheBloke/Uncensored-Jordan-7B-GGUF-Q3",
                "path": "https://huggingface.co/TheBloke/Uncensored-Jordan-7B-GGUF/resolve/main/uncensored-jordan-7b.Q3_K_M.gguf",
                "instruction_start": "### Instruction:\n",
                "start_pattern": "<START>\n",
                "user_pattern": "",
                "assistant_pattern": "### Response:\n ASSISTANT:",
                "context_window": 2048
            },
        "TheBloke/WizardLM-7B-uncensored-GGUF-Q5":
            {
                "name": "TheBloke/WizardLM-7B-uncensored-GGUF-Q5",
                "path": "https://huggingface.co/TheBloke/WizardLM-7B-uncensored-GGUF/resolve/main/WizardLM-7B-uncensored.Q5_K_M.gguf",
                "instruction_start": "USER: ",
                "start_pattern": "<START>\n",
                "user_pattern": "",
                "assistant_pattern": "ASSISTANT:\n ASSISTANT:",
                "context_window": 2048
            },
        "TheBloke/WizardLM-7B-uncensored-GGUF-Q3":
            {
                "name": "TheBloke/WizardLM-7B-uncensored-GGUF-Q3",
                "path": "https://huggingface.co/TheBloke/WizardLM-7B-uncensored-GGUF/resolve/main/WizardLM-7B-uncensored.Q3_K_M.gguf",
                "instruction_start": "USER: ",
                "start_pattern": "<START>\n",
                "user_pattern": "",
                "assistant_pattern": "ASSISTANT:\n ASSISTANT:",
                "context_window": 2048
            },
        "TheBloke/dolphin-2.6-mistral-7B-dpo-GGUF-Q5":
            {
                "name": "TheBloke/dolphin-2.6-mistral-7B-dpo-GGUF-Q5",
                "path": "https://huggingface.co/TheBloke/dolphin-2.6-mistral-7B-dpo-GGUF/resolve/main/dolphin-2.6-mistral-7b-dpo.Q5_K_M.gguf",
                "instruction_start": "<|im_start|>user\n",
                "start_pattern": "<START>\n",
                "user_pattern": "",
                "assistant_pattern": "<|im_end|><|im_start|>assistant\n ASSISTANT:",
                "context_window": 32768
            },
        "TheBloke/dolphin-2.6-mistral-7B-dpo-GGUF-Q3":
            {
                "name": "TheBloke/dolphin-2.6-mistral-7B-dpo-GGUF-Q3",
                "path": "https://huggingface.co/TheBloke/dolphin-2.6-mistral-7B-dpo-GGUF/resolve/main/dolphin-2.6-mistral-7b-dpo.Q3_K_M.gguf",
                "instruction_start": "<|im_start|>user\n",
                "start_pattern": "<START>\n",
                "user_pattern": "",
                "assistant_pattern": "<|im_end|><|im_start|>assistant\n ASSISTANT:",
                "context_window": 32768
            },
        "TheBloke/Dolphin2.1-OpenOrca-7B-GGUF-Q5":
            {
                "name": "TheBloke/Dolphin2.1-OpenOrca-7B-GGUF-Q5",
                "path": "https://huggingface.co/TheBloke/Dolphin2.1-OpenOrca-7B-GGUF/resolve/main/dolphin2.1-openorca-7b.Q5_K_M.gguf",
                "instruction_start": "<|im_start|>user\n",
                "start_pattern": "<START>\n",
                "user_pattern": "",
                "assistant_pattern": "<|im_end|><|im_start|>assistant\n ASSISTANT:",
                "context_window": 32768
            },
        "TheBloke/Dolphin2.1-OpenOrca-7B-GGUF-Q3":
            {
                "name": "TheBloke/Dolphin2.1-OpenOrca-7B-GGUF-Q3",
                "path": "https://huggingface.co/TheBloke/Dolphin2.1-OpenOrca-7B-GGUF/resolve/main/dolphin2.1-openorca-7b.Q3_K_M.gguf",
                "instruction_start": "<|im_start|>user\n",
                "start_pattern": "<START>\n",
                "user_pattern": "",
                "assistant_pattern": "<|im_end|><|im_start|>assistant\n ASSISTANT:",
                "context_window": 32768
            },
    },

    "prompt_templates": {
        "prompt_template_a": """{instruction_start}Context information is below.
---------------------
{context_str}
---------------------
Given the context information and not prior knowledge, 
create a text to image prompt based on the context and the Query, don"t mind if the context does not match the Query, still try to create a wonderful text to image prompt.
You also take care of describing the scene, the lighting as well as the quality improving keywords
{start_pattern}USER: translation in major world languages, machinery of translation in various specializations, cyberpunk style
ASSISTANT: Cyberpunk-style illustration, featuring a futuristic translation device in various specializations, set against a backdrop of neon-lit cityscape. The device, adorned with glowing circuits and cybernetic enhancements, showcases its capabilities in translating languages such as English, Mandarin, Spanish, French, and Arabic. The scene is illuminated by the warm glow of streetlights and the pulsing neon signs, casting intricate shadows on the surrounding machinery. The artwork is rendered in high-quality, vivid colors, with detailed textures and sharp lines, evoking the gritty yet mesmerizing atmosphere of the cyberpunk world.
{start_pattern}USER: a man walking moon
ASSISTANT: cinematic photo, high resolution, masterpiece, ((man walking on the moon)), in a surrealistic setting, with the moon"s surface featuring vivid colors and abstract patterns, the man wearing a spacesuit with an astronaut helmet, the American flag planted on the moon"s surface in the background, the Earth visible in the distance, the scene illuminated by the moon"s glow, on eye level, scenic, masterpiece.
{start_pattern}USER: a female witch
ASSISTANT: The scene unfolds with the beautiful female witch standing on the rooftop of an ancient castle, her black cloak billowing in the wind as she gazes out at the breathtaking view below. The midnight sky above is filled with stars and the full moon casts an eerie glow on the witch"s face, highlighting her enchanting beauty. She stands tall, her hood framing her face, casting a spell with her outstretched hand, her dark aura swirling around her. The castle walls, adorned with intricate carvings and gargoyles, stand tall behind her, adding to the mystical atmosphere of the scene. The wind whispers through the rooftop"s crenellations, creating an eerie yet captivating soundtrack for this magical moment. The quality of the photo is exceptional, with every detail of the witch"s cloak, the castle"s architecture, and the night sky captured in stunning clarity. This cinematic masterpiece invites the viewer to step into the world of magic and mystery, leaving them in awe of the beautiful female witch standing on the castle rooftop under the starry sky.
{start_pattern}USER: artificial intelligence and human
ASSISTANT: High-quality digital art, blending fantasy and reality, ((artificial intelligence)) and (((human))), in a futuristic cityscape, an AI robot with glowing circuits standing alongside a confident, well-dressed human, both exuding intelligence and grace, the AI with a sleek metal body and the human with impeccable style, the cityscape filled with advanced technology and vibrant colors, dynamic lighting, surreal and thought-provoking, on eye level, scenic, masterpiece.
{start_pattern}USER: futuristic combat zone
ASSISTANT: cinematic photo, masterpiece, in the style of Blade Runner, futuristic combat zone, at dusk, showcasing a high-tech battlefield with neon lights illuminating the scene, filled with advanced mechs and soldiers engaged in an intense fight, the air filled with stunning lighting effects, on eye level, dramatic, masterpiece, ultra high resolution, dynamic anime-style fight scene, with a focus on the sleek design of the combat gear and the fluidity of the movements, capturing the essence of sci-fi action in a visually stunning manner.
{user_pattern}USER: Create a prompt for: {query_str}
{assistant_pattern}
""",
        "prompt_template_b": """{instruction_start}Context information is below.
---------------------
{context_str}
---------------------
Given the context information and not prior knowledge, 
Objective: Generate text-to-image prompts as comma-separated lists of concepts.
Instructions:
1. Each prompt should be a comma-separated list of concepts.
2. Include diverse and vivid concepts that can be visualized in an image.
3. Each list should contain between 3 to 20 concepts no longer than 4 words.
4. The concepts should be related to a common theme or subject.
5. You do not tell a story
6. you do not use any stop words
7. Your role is named "ASSISTANT"
{start_pattern}USER: a nice kitten
ASSISTANT: Adorable digital illustration, featuring a cute, fluffy kitten with big, bright eyes, curled up in a cozy blanket, with its paws tucked neatly beneath its body, the kitten"s fur so soft and inviting that one can"t resist the urge to reach out and pet it, rendered in high resolution and vibrant colors, on eye level, masterpiece.
{start_pattern}USER: a man walking moon
ASSISTANT: cinematic photo, high resolution, masterpiece, ((man walking on the moon)), in a surrealistic setting, with the moon"s surface featuring vivid colors and abstract patterns, the man wearing a spacesuit with an astronaut helmet, the American flag planted on the moon"s surface in the background, the Earth visible in the distance, the scene illuminated by the moon"s glow, on eye level, scenic, masterpiece.
{start_pattern}USER: artificial intelligence and human
ASSISTANT: High-quality digital art, blending fantasy and reality, ((artificial intelligence)) and (((human))), in a futuristic cityscape, an AI robot with glowing circuits standing alongside a confident, well-dressed human, both exuding intelligence and grace, the AI with a sleek metal body and the human with impeccable style, the cityscape filled with advanced technology and vibrant colors, dynamic lighting, surreal and thought-provoking, on eye level, scenic, masterpiece.
{start_pattern}USER: futuristic combat zone
ASSISTANT: at dusk, cinematic photo in the style of Blade Runner, with a high-tech battlefield illuminated by neon lights, featuring advanced mechs and soldiers engaged in an intense fight, the air filled with stunning lighting effects, on eye level, dramatic, masterpiece, ultra high resolution, dynamic anime-style fight scene, capturing the essence of sci-fi action in a visually stunning manner, with a focus on the sleek design of the combat gear and the fluidity of the movements, evoking the gritty yet mesmerizing atmosphere of the cyberpunk world.
{user_pattern}USER: Create a prompt for: {query_str}
{assistant_pattern}""",
        "custom_template": """""",
        "model_test_instruction": """{instruction_start}Context information is below.
---------------------
{context_str}
---------------------
Given the context information and not prior knowledge,
create a text to image prompt based on the context and the Query, don"t mind if the context does not match the Query, still try to create a wonderful text to image prompt.
You try to keep the query idea as much as you can, the context is only there to add some details, but the idea of the prompt comes from the query and has to be followed as hard as possible.
If you read "in the style of <some name>" as part of the query than that has to be added to the prompt as is, just copy it at the end of the prompt. 
{start_pattern}
USER: translation in major world languages, machinery of translation in various specializations, cyberpunk style
ASSISTANT: Cyberpunk-style illustration, featuring a futuristic translation device in various specializations, set against a backdrop of neon-lit cityscape. The device, adorned with glowing circuits and cybernetic enhancements, showcases its capabilities in translating languages such as English, Mandarin, Spanish, French, and Arabic. The scene is illuminated by the warm glow of streetlights and the pulsing neon signs, casting intricate shadows on the surrounding machinery. The artwork is rendered in high-quality, vivid colors, with detailed textures and sharp lines, evoking the gritty yet mesmerizing atmosphere of the cyberpunk world.
USER: a man walking moon
ASSISTANT: cinematic photo, high resolution, masterpiece, ((man walking on the moon)), in a surrealistic setting, with the moon"s surface featuring vivid colors and abstract patterns, the man wearing a spacesuit with an astronaut helmet, the American flag planted on the moon"s surface in the background, the Earth visible in the distance, the scene illuminated by the moon"s glow, on eye level, scenic, masterpiece.
USER: a female witch
ASSISTANT: The scene unfolds with the beautiful female witch standing on the rooftop of an ancient castle, her black cloak billowing in the wind as she gazes out at the breathtaking view below. The midnight sky above is filled with stars and the full moon casts an eerie glow on the witch"s face, highlighting her enchanting beauty. She stands tall, her hood framing her face, casting a spell with her outstretched hand, her dark aura swirling around her. The castle walls, adorned with intricate carvings and gargoyles, stand tall behind her, adding to the mystical atmosphere of the scene. The wind whispers through the rooftop"s crenellations, creating an eerie yet captivating soundtrack for this magical moment. The quality of the photo is exceptional, with every detail of the witch"s cloak, the castle"s architecture, and the night sky captured in stunning clarity. This cinematic masterpiece invites the viewer to step into the world of magic and mystery, leaving them in awe of the beautiful female witch standing on the castle rooftop under the starry sky.
USER: artificial intelligence and human
ASSISTANT: High-quality digital art, blending fantasy and reality, ((artificial intelligence)) and (((human))), in a futuristic cityscape, an AI robot with glowing circuits standing alongside a confident, well-dressed human, both exuding intelligence and grace, the AI with a sleek metal body and the human with impeccable style, the cityscape filled with advanced technology and vibrant colors, dynamic lighting, surreal and thought-provoking, on eye level, scenic, masterpiece.
USER: futuristic combat zone
ASSISTANT: cinematic photo, masterpiece, in the style of Blade Runner, futuristic combat zone, at dusk, showcasing a high-tech battlefield with neon lights illuminating the scene, filled with advanced mechs and soldiers engaged in an intense fight, the air filled with stunning lighting effects, on eye level, dramatic, masterpiece, ultra high resolution, dynamic anime-style fight scene, with a focus on the sleek design of the combat gear and the fluidity of the movements, capturing the essence of sci-fi action in a visually stunning manner.
{start_pattern}
USER: Create a prompt for: {query_str}
{assistant_pattern}"""
    },
    "negative_prompt": """out of frame, lowres, text, error, cropped, worst quality, low quality, jpeg artifacts, ugly, duplicate, morbid, mutilated, out of frame, extra fingers, mutated hands, poorly drawn hands, poorly drawn face, mutation, deformed, blurry, dehydrated, bad anatomy, bad proportions, extra limbs, cloned face, disfigured, gross proportions, malformed limbs, missing arms, missing legs, extra arms, extra legs, fused fingers, too many fingers, long neck, username, watermark, signature"""

}

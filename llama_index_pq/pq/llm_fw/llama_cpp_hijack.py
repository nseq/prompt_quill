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

import sys
import importlib
from types import ModuleType
from pathlib import Path


class llama_cpp_hijack:
    def __init__(self):
        # Ensure llama_cpp is imported properly
        if 'llama_cpp' not in sys.modules:
            sys.modules['llama_cpp'] = importlib.import_module('llama_cpp')
            
        original_llama = sys.modules['llama_cpp']
        
        if not hasattr(original_llama, 'Llama'):
            raise ImportError("llama_cpp.Llama not found. Check installation or version compatibility.")
        
        # 2. Force reload settings with proper Pydantic v2 handling
        settings_module = importlib.import_module('llama_cpp.server.settings')
        importlib.reload(settings_module)
        
        # 3. Handle different settings configurations
        if hasattr(settings_module, 'Settings'):
            # Pydantic v2 style with required fields
            self.target_batch = settings_module.Settings(
                model="/tmp/llama_index/models/panda-7b-v0.1.Q4_K_M.gguf",  # Required field placeholder:cite[3]:cite[6]
                n_batch=2048              # Your override
            ).n_batch
        else:
            # Fallback for legacy configurations
            self.target_batch = getattr(settings_module, 'n_batch', 512)

        # 4. Monkey-patch the Llama class constructor
        class PatchedLlama(original_llama.Llama):
            def __init__(self, *args, **kwargs):
                # Enforce n_batch with priority:
                # 1. Explicit arguments
                # 2. Settings.py value
                # 3. Default 512:cite[5]
                kwargs.setdefault('n_batch', self.target_batch)
                
                # Handle required model_path if needed
                if 'model_path' not in kwargs:
                    kwargs['model_path'] = "dummy/path.gguf"
                
                super().__init__(*args, **kwargs)

        # 5. Replace module components
        original_llama.Llama = PatchedLlama
        sys.modules['llama_cpp'] = original_llama

        # 6. Debug output
        print(f"llama_cpp hijack complete - n_batch={self.target_batch}")

# Immediate application
llama_cpp_hijack()

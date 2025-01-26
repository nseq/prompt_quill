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

class llama_cpp_hijack:
    def __init__(self):
        # Get reference to original module first
        original_llama = sys.modules.get('llama_cpp', None)
        
        # Force reload settings with potential user modifications
        settings_module = importlib.import_module('llama_cpp.server.settings')
        importlib.reload(settings_module)
        
        # Modern llama.cpp versions use a Settings class
        if hasattr(settings_module, 'Settings'):
            self.target_batch = settings_module.Settings().n_batch
        else:  # Legacy version with direct attributes
            self.target_batch = getattr(settings_module, 'n_batch', 512)  # Fallback

        # Monkey-patch the Llama class
        class PatchedLlama(original_llama.Llama):
            def __init__(self, *args, **kwargs):
                kwargs.setdefault('n_batch', self.target_batch)
                super().__init__(*args, **kwargs)
        
        original_llama.Llama = PatchedLlama
        sys.modules['llama_cpp'] = original_llama

        print(f"Successfully set n_batch to {self.target_batch}")

# Apply the hijack immediately
llama_cpp_hijack()

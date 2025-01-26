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
import inspect
from importlib import reload

# Keep original reference before hijacking
original_llama_cpp = sys.modules.get('llama_cpp', None)

class llama_cpp_hijack:
    def __init__(self):
        # 1. Get the server settings FIRST
        from llama_cpp.server import settings
        self.target_batch = settings.n_batch  # 2048
        
        # 2. Preserve original Llama class
        if original_llama_cpp:
            self.OriginalLlama = original_llama_cpp.Llama
            
        # 3. Monkey-patch the Llama class constructor
        class PatchedLlama(self.OriginalLlama):
            def __init__(self, *args, **kwargs):
                # Force n_batch if not explicitly set
                if 'n_batch' not in kwargs:
                    kwargs['n_batch'] = self.target_batch
                super().__init__(*args, **kwargs)
                
        # 4. Replace the class in the module
        original_llama_cpp.Llama = PatchedLlama
        sys.modules['llama_cpp'] = original_llama_cpp

        # 5. Reload dependent modules
        if 'llama_cpp.server' in sys.modules:
            reload(sys.modules['llama_cpp.server'])

# Apply the hijack
llama_cpp_hijack()

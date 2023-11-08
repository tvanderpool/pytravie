import json
import os
from typing import List, Any, Dict, TypeVar
from .extend import ExtendCls
from pathlib import Path
import importlib

_JsonT = TypeVar('_JsonT', str,List,Dict,None)

@ExtendCls(json)
class __json:
    @staticmethod
    def load_from(filepath:str, noneIfMissing:bool=False)->"_JsonT":
        if noneIfMissing and not os.path.exists(filepath): return None
        with open(filepath) as F:
            return json.load(F)
    @staticmethod
    def dump_to(obj:"_JsonT", filepath:str, **kwargs)->"_JsonT":
        with open(filepath, 'w+') as F:
            json.dump(obj, F, **kwargs)
        return obj

for ext in (travie:=Path(__file__).parent).rglob('_extend.py'):
    importlib.import_module(str(ext.relative_to(travie.parent).with_suffix('')).replace('/','.'))

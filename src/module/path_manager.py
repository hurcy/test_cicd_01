from pathlib import Path

class PathResolver:
    _instance = None
    
    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._root = Path(__file__).parent.parent.parent
        return cls._instance
    
    @property
    def resources(self):
        return self._root / 'resources'
    
    @property
    def tests(self):
        return self._root / 'tests'
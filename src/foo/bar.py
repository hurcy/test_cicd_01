import yaml
from module.path_manager import PathResolver

def parse_bar():
    paths = PathResolver()
    config_path = paths.resources / 'foo/bar.yml'
    with config_path.open() as f:
        data = yaml.safe_load(f)
        return data

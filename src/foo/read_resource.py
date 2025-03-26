from src.module.path_manager import PathResolver

def process_data():
    paths = PathResolver()
    config_path = paths.resources / 'foo/config.yml'
    with config_path.open() as f:
        out = f.readline()
        return out

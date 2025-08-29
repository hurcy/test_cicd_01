from module.path_manager import PathResolver

def parse_bar():
    paths = PathResolver()
    config_path = paths.resources / 'foo/bar.yml'
    with config_path.open() as f:
        out = f.readline()
        return out

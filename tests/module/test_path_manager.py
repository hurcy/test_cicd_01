from src.module.path_manager import PathResolver

def test_path_resolver():
    paths = PathResolver()
    assert 'test_cicd_01/resources' in str(paths.resources)
  
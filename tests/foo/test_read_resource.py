from foo.bar import parse_bar

def test_call_read_resource_function():
    assert parse_bar() == 'test'

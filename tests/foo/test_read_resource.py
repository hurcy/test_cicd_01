from foo.bar import parse_bar

def test_call_read_resource_function():
    result = parse_bar()
    assert isinstance(result, dict)
    assert 'bar_test' in result
    assert result['bar_test']['foo_test'] == 'zoo'

from src import parse, Key, parse_kle


def test_simple_parser():
    input_string = "12"
    result = parse(input_string)
    assert result == 12

    input_string = "a12"
    result = parse(input_string)
    assert result == 12

    input_string = "a12442349asdf123"
    result = parse(input_string)
    assert result == 12442349

def test_kle_key():
    key = Key(a=7)
    assert key.a == 7

def test_parse_kle():
    # TODO: Make this pass.
    src = "[{a:7}]"
    result = parse_kle(src)
    assert result == [Key(a=7)]


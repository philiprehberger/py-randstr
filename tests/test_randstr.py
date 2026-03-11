import string
from philiprehberger_randstr import randstr, token, password, hex_str, uuid_short


def test_randstr_default_length():
    result = randstr()
    assert len(result) == 16


def test_randstr_custom_length():
    result = randstr(32)
    assert len(result) == 32


def test_randstr_alphanumeric():
    result = randstr(100, charset="alphanumeric")
    assert all(c in string.ascii_letters + string.digits for c in result)


def test_randstr_lowercase():
    result = randstr(100, charset="lowercase")
    assert all(c in string.ascii_lowercase for c in result)


def test_randstr_digits():
    result = randstr(100, charset="digits")
    assert all(c in string.digits for c in result)


def test_randstr_custom_charset():
    result = randstr(10, charset="abc")
    assert all(c in "abc" for c in result)


def test_token_length():
    result = token(32)
    assert len(result) == 32


def test_token_url_safe():
    result = token(64)
    # URL-safe base64 uses alphanumeric, -, _
    assert all(c.isalnum() or c in "-_" for c in result)


def test_password_length():
    result = password(16)
    assert len(result) == 16


def test_password_has_diversity():
    result = password(20)
    has_upper = any(c.isupper() for c in result)
    has_digit = any(c.isdigit() for c in result)
    assert has_upper
    assert has_digit


def test_hex_str_length():
    result = hex_str(16)
    assert len(result) == 16


def test_hex_str_valid():
    result = hex_str(32)
    assert all(c in "0123456789abcdef" for c in result)


def test_uuid_short_default():
    result = uuid_short()
    assert len(result) == 8


def test_uuid_short_custom():
    result = uuid_short(12)
    assert len(result) == 12


def test_uniqueness():
    results = {randstr(16) for _ in range(100)}
    assert len(results) == 100  # all unique

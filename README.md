# philiprehberger-randstr

[![Tests](https://github.com/philiprehberger/py-randstr/actions/workflows/publish.yml/badge.svg)](https://github.com/philiprehberger/py-randstr/actions/workflows/publish.yml)
[![PyPI version](https://img.shields.io/pypi/v/philiprehberger-randstr.svg)](https://pypi.org/project/philiprehberger-randstr/)
[![License](https://img.shields.io/github/license/philiprehberger/py-randstr)](LICENSE)

Generate random readable strings for various purposes.

## Installation

```bash
pip install philiprehberger-randstr
```

## Usage

```python
from philiprehberger_randstr import randstr, token, password, hex_str, uuid_short

randstr(16)                       # "aBx4kLm9pQrS2tUv"
randstr(8, charset="lowercase")   # "abcdefgh"

token(32)                         # URL-safe base64 token
password(16)                      # "aB3$kLm!9pQr#2tU"
hex_str(16)                       # "a1b2c3d4e5f6a7b8"
uuid_short()                      # "7f3a8b2c"
```

All generators use the `secrets` module for cryptographic security.

## API

- `randstr(length=16, charset="alphanumeric")` — Random string from charset
- `token(length=32)` — URL-safe base64 token
- `password(length=16, symbols, min_symbols, min_digits, min_upper)` — Strong password
- `hex_str(length=16)` — Random hex string
- `uuid_short(length=8)` — Short UUID-like hex ID

## License

MIT

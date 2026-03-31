# philiprehberger-randstr

[![Tests](https://github.com/philiprehberger/py-randstr/actions/workflows/publish.yml/badge.svg)](https://github.com/philiprehberger/py-randstr/actions/workflows/publish.yml)
[![PyPI version](https://img.shields.io/pypi/v/philiprehberger-randstr.svg)](https://pypi.org/project/philiprehberger-randstr/)
[![Last updated](https://img.shields.io/github/last-commit/philiprehberger/py-randstr)](https://github.com/philiprehberger/py-randstr/commits/main)

Generate random readable strings for various purposes.

## Installation

```bash
pip install philiprehberger-randstr
```

## Usage

### Random Strings

```python
from philiprehberger_randstr import randstr

randstr(16)                       # "aBx4kLm9pQrS2tUv"
randstr(8, charset="lowercase")   # "abcdefgh"
```

### Tokens and Passwords

```python
from philiprehberger_randstr import token, password

token(32)       # URL-safe base64 token
password(16)    # "aB3$kLm!9pQr#2tU"
```

### Hex and Short IDs

```python
from philiprehberger_randstr import hex_str, uuid_short

hex_str(16)     # "a1b2c3d4e5f6a7b8"
uuid_short()    # "7f3a8b2c"
```

All generators use the `secrets` module for cryptographic security.

## API

- `randstr(length=16, charset="alphanumeric")` — Random string from charset
- `token(length=32)` — URL-safe base64 token
- `password(length=16, symbols, min_symbols, min_digits, min_upper)` — Strong password
- `hex_str(length=16)` — Random hex string
- `uuid_short(length=8)` — Short UUID-like hex ID

## Development

```bash
pip install -e .
python -m pytest tests/ -v
```

## Support

If you find this project useful:

⭐ [Star the repo](https://github.com/philiprehberger/py-randstr)

🐛 [Report issues](https://github.com/philiprehberger/py-randstr/issues?q=is%3Aissue+is%3Aopen+label%3Abug)

💡 [Suggest features](https://github.com/philiprehberger/py-randstr/issues?q=is%3Aissue+is%3Aopen+label%3Aenhancement)

❤️ [Sponsor development](https://github.com/sponsors/philiprehberger)

🌐 [All Open Source Projects](https://philiprehberger.com/open-source-packages)

💻 [GitHub Profile](https://github.com/philiprehberger)

🔗 [LinkedIn Profile](https://www.linkedin.com/in/philiprehberger)

## License

[MIT](LICENSE)

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

### Readable IDs

`readable_id` excludes visually-confusable characters (`0`, `1`, `O`, `o`, `I`, `l`) — useful for vouchers, short references, and any human-typed code.

```python
from philiprehberger_randstr import readable_id

readable_id(8)   # e.g. "K7P4MNXR" — never contains 0/1/O/o/I/l
```

All generators use the `secrets` module for cryptographic security.

## API

| Function / Class | Description |
|------------------|-------------|
| `randstr(length=16, charset="alphanumeric")` | Random string from a built-in or custom charset |
| `token(length=32)` | URL-safe base64-encoded token |
| `password(length=16, symbols, min_symbols, min_digits, min_upper)` | Strong password with guaranteed character-class diversity |
| `hex_str(length=16)` | Random lowercase hex string |
| `uuid_short(length=8)` | Short UUID-like hex ID |
| `readable_id(length=8)` | Random ID drawn from a visually-unambiguous alphabet |

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

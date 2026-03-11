"""Generate random readable strings for various purposes."""

from __future__ import annotations

import secrets
import string


__all__ = [
    "randstr",
    "token",
    "password",
    "hex_str",
    "uuid_short",
]

_CHARSETS: dict[str, str] = {
    "alphanumeric": string.ascii_letters + string.digits,
    "lowercase": string.ascii_lowercase,
    "uppercase": string.ascii_uppercase,
    "digits": string.digits,
    "hex": string.hexdigits[:16],
    "letters": string.ascii_letters,
}


def randstr(length: int = 16, *, charset: str = "alphanumeric") -> str:
    """Generate a cryptographically secure random string.

    Args:
        length: Length of the string to generate.
        charset: Name of a built-in charset or a custom string of characters.
            Built-in: ``"alphanumeric"``, ``"lowercase"``, ``"uppercase"``,
            ``"digits"``, ``"hex"``, ``"letters"``.

    Returns:
        Random string of the specified length.
    """
    chars = _CHARSETS.get(charset, charset)
    if not chars:
        msg = f"Empty charset: '{charset}'"
        raise ValueError(msg)
    return "".join(secrets.choice(chars) for _ in range(length))


def token(length: int = 32) -> str:
    """Generate a URL-safe base64-encoded token.

    Args:
        length: Approximate length of the token (actual may vary slightly).

    Returns:
        URL-safe token string.
    """
    nbytes = max(1, (length * 3) // 4)
    return secrets.token_urlsafe(nbytes)[:length]


def password(
    length: int = 16,
    *,
    symbols: str = "!@#$%^&*()-_=+",
    min_symbols: int = 2,
    min_digits: int = 2,
    min_upper: int = 2,
) -> str:
    """Generate a strong password with guaranteed character class diversity.

    Args:
        length: Total password length.
        symbols: Symbol characters to include.
        min_symbols: Minimum symbol count.
        min_digits: Minimum digit count.
        min_upper: Minimum uppercase count.

    Returns:
        Password string meeting all requirements.
    """
    if length < min_symbols + min_digits + min_upper + 1:
        msg = "Length too short for the minimum requirements"
        raise ValueError(msg)

    chars: list[str] = []
    chars.extend(secrets.choice(symbols) for _ in range(min_symbols))
    chars.extend(secrets.choice(string.digits) for _ in range(min_digits))
    chars.extend(secrets.choice(string.ascii_uppercase) for _ in range(min_upper))

    remaining = length - len(chars)
    all_chars = string.ascii_letters + string.digits + symbols
    chars.extend(secrets.choice(all_chars) for _ in range(remaining))

    # Shuffle to avoid predictable positions
    result = list(chars)
    for i in range(len(result) - 1, 0, -1):
        j = secrets.randbelow(i + 1)
        result[i], result[j] = result[j], result[i]

    return "".join(result)


def hex_str(length: int = 16) -> str:
    """Generate a random hexadecimal string.

    Args:
        length: Length of the hex string (must be even for full bytes).

    Returns:
        Lowercase hex string.
    """
    nbytes = (length + 1) // 2
    return secrets.token_hex(nbytes)[:length]


def uuid_short(length: int = 8) -> str:
    """Generate a short UUID-like string from random hex.

    Args:
        length: Length of the short ID.

    Returns:
        Lowercase hex string.
    """
    return hex_str(length)

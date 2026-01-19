from errors import HashError

class HashBase:
    def __init__(self, value: bytes) -> None:
        if len(value) != 32:
            raise ValueError("Un hash Bitcoin doit contenir 32 bytes (256 bits)")
        self._value = value

    @property
    def value(self):
        return self._value

    def to_hex(self):
        return self.value.hex()

    @classmethod
    def from_hex(cls, hexadecimal_in_str: str):
        if not isinstance(hexadecimal_in_str, str):
            raise HashError("Le hash hexadécimal doit être une chaîne de caractères (str)")

        s = hexadecimal_in_str.strip()
        if s.startswith(("0x", "0X")):
            s = s[2:]

        if len(s) != 64:
            raise HashError("Le hash doit contenir exactement 64 caractères hexadécimaux (32 bytes)")

        try:
            raw = bytes.fromhex(s)
        except ValueError as e:
            raise HashError(f"Hash hexadécimal invalide: {e}") from e

        return cls(raw)

    def __str__(self):
        return self.to_hex()

from urllib3.util.util import to_str

from errors import HashError

class HashBase:
    def __init__(self, value: bytes):
        if len(value) != 32:
            raise ValueError("Un hash Bitcoin doit contenir 32 bytes (256 bits)")
        self._value = value

    @property
    def value(self):
        return self._value

    def to_hex(self):
        return self.value.hex()

    @classmethod
    def from_hex(cls, hex_str: str):
        try:
            raw = bytes.fromhex(hex_str)
        except ValueError as e :
            raise HashError(f'Le hash doit contenir 64 caractères -- ({e})')
        return cls(raw)

    def __str__(self):
        return self.to_hex()

from Block import Block
from HashBase import HashBase
from errors import BlockError, BlockNotFoundError, RpcError, HashError

valid_hash = '000000000000000000013c87cd5dbe7c6b4afdd8e6868ee157332f5cd743fb37'

try:
    hash1 = HashBase.from_hex('00000000000000000000611fd22f2df7c8fbd0688745c3a6c3bb5109cc2a12cb')
except HashError as e:
    print(e)

def main() -> None:

    bloc = Block(hash1)

    try:
        print(bloc.get_block())
    except BlockNotFoundError as e:
        print(e)
    except RpcError as e:
        print(e)
    except BlockError as e:
        print(e)
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
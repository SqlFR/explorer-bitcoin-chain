from Block import Block
from HashBase import HashBase
from errors import BlockError, BlockNotFoundError, RpcError, HashError
try:
    hash1 = HashBase.from_hex('000000000000000000012a990314cebe57aa81d1a7117c63d890a530c5dac191')
except HashError as e:
    print(e)

def main() -> None:
    bloc = Block(hash1)

    try:
        print(bloc.get_blockstats())
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
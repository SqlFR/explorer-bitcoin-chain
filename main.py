from Block import Block
from errors import BlockError, BlockNotFoundError, RpcError


def main() -> None:
    bloc = Block('000000000000000000012a990314cebe57aa81d1a7117c63d890a530c5dac191')

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
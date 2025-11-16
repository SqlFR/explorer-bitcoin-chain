from Block import Block
from Block import BlockError, BlockNotFoundError, RpcError


def main() -> None:
    bloc = Block('00000000000200000000000000000f3676e3625d39fc68628e23d575677bf7b0b')

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
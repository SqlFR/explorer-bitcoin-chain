from Block import Block
from HashBase import HashBase
from errors import BlockError, BlockNotFoundError, RpcError, HashError

valid_hash = '000000000000000000013c87cd5dbe7c6b4afdd8e6868ee157332f5cd743fb37'

try:
    hash1 = HashBase.from_hex('000000000000000000013c87cd5dbe7c6b4afdd8e6868ee157332f5cd743fb37')
except HashError as e:
    print(e)

def main() -> None:

    bloc = Block(hash1)

    try:
        print(bloc.get_blockstats('blockhash'))
    except BlockNotFoundError as blocknotfound_error:
        print('BlockNotFoundError : ', blocknotfound_error)
    except RpcError as rpc_error:
        print('RpcError : ', rpc_error)
    except BlockError as block_error:
        print('BlockError : ', block_error)
    except ValueError as value_error:
        print('ValueError : ', value_error)


if __name__ == "__main__":
    main()
from network import EVMNetwork
from network.stablecoin import Stablecoin
from network.fantom.constants import FantomConstants
from stargate import StargateConstants


class Fantom(EVMNetwork):

    def __init__(self):
        supported_stablecoins = {
            'USDC': Stablecoin('USDC', FantomConstants.USDC_CONTRACT_ADDRESS, FantomConstants.USDC_DECIMALS,
                               FantomConstants.STARGATE_CHAIN_ID, StargateConstants.POOLS['USDC'])
        }

        super().__init__(FantomConstants.NAME, FantomConstants.NATIVE_TOKEN, FantomConstants.RPC,
                         FantomConstants.STARGATE_CHAIN_ID, FantomConstants.STARGATE_ROUTER_CONTRACT_ADDRESS,
                         supported_stablecoins)

    def _get_approve_gas_limit(self) -> int:
        return FantomConstants.APPROVE_GAS_LIMIT

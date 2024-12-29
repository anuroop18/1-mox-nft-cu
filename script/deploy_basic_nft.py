from moccasin.boa_tools import VyperContract

from contracts import basic_nft

PUG_URI = "QmSuNxMLsDfomkDnidxMzXrVYCCTWJNHBANMxvCchQbgKQ"

def deploy_basic_nft() -> VyperContract:
    contract = basic_nft.deploy()
    return contract

def moccasin_main() -> VyperContract:
    return deploy_basic_nft()
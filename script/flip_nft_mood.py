import boa
from moccasin.boa_tools import VyperContract

MOOD_CONTRACT_ADDRESS = "0x5FbDB2315678afecb367f032d93F642f64180aa3"

# We need to flip the mood of the NFT 
def flip_nft_mood(mood_contract: VyperContract, token_id: int):
    mood_contract.flip_mood(token_id)
    print(f"Mood: {mood_contract.token_id_to_mood(token_id)}")
    print(f"TokenURI: {mood_contract.tokenURI(token_id)}")

def moccasin_main():
    mood_contract_deployer = boa.load_partial("contracts/mood_nft.vy")
    mood_contract = mood_contract_deployer.at(MOOD_CONTRACT_ADDRESS)
    flip_nft_mood(mood_contract, 0)
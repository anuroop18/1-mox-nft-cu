import boa

from script.deploy_basic_nft import PUG_URI


def test_initialization(basic_nft, owner):
    assert basic_nft.name() == "Puppy NFT"
    assert basic_nft.symbol() == "PNFT"
    assert basic_nft.BASE_URI() == "ipfs://"
    assert basic_nft.owner() == owner

def test_mint(basic_nft, aryan):
    with boa.env.prank(aryan):
        basic_nft.mint(PUG_URI)
    print(f"basic_nft.ownerOf(0): {basic_nft.ownerOf(0)}")
    print(f"aryan: {aryan}")
    assert basic_nft.ownerOf(0) == aryan
    assert basic_nft.tokenURI(0) == "ipfs://" + PUG_URI
    assert basic_nft.balanceOf(aryan) == 1
    assert basic_nft.totalSupply() == 1

def test_token_transfers(basic_nft, aryan, raghav):
    with boa.env.prank(aryan):
        basic_nft.mint(PUG_URI)
    with boa.env.prank(aryan):
        basic_nft.transferFrom(aryan, raghav, 0)
    assert basic_nft.ownerOf(0) == raghav
    assert basic_nft.balanceOf(aryan) == 0
    assert basic_nft.balanceOf(raghav) == 1

def test_approve_and_transfer(basic_nft, aryan, raghav, chikapa):
    with boa.env.prank(aryan):
        basic_nft.mint(PUG_URI)
    assert basic_nft.ownerOf(0) == aryan
    with boa.env.prank(aryan):
        basic_nft.approve(chikapa, 0)
    assert basic_nft.getApproved(0) == chikapa
    with boa.env.prank(chikapa):
        basic_nft.transferFrom(aryan, raghav, 0)
    assert basic_nft.ownerOf(0) == raghav
    assert basic_nft.totalSupply() == 1
    assert basic_nft.balanceOf(aryan) == 0
    assert basic_nft.balanceOf(raghav) == 1
    assert basic_nft.balanceOf(chikapa) == 0

def test_mint_multiple_tokens(basic_nft, aryan):
    with boa.env.prank(aryan):
        for i in range(3):
            basic_nft.mint(PUG_URI)
            assert basic_nft.tokenURI(i) == "ipfs://" + PUG_URI
    assert basic_nft.balanceOf(aryan) == 3
    assert basic_nft.totalSupply() == 3
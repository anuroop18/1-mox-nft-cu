import boa
import base64
import json

def test_initialization(mood_nft, owner):
    assert mood_nft.name() == "Mood NFT"
    assert mood_nft.symbol() == "MNFT"
    assert mood_nft.owner() == owner

def test_mint(mood_nft, aryan):
    with boa.env.prank(aryan):
        mood_nft.mint_nft()
    assert mood_nft.ownerOf(0) == aryan
    assert mood_nft.balanceOf(aryan) == 1
    assert mood_nft.totalSupply() == 1
    assert mood_nft.token_id_to_mood(0) == 1 # HAPPY == 1

def test_flip_mood(mood_nft, aryan):
    with boa.env.prank(aryan):
        mood_nft.mint_nft()
    assert mood_nft.token_id_to_mood(0) == 1 # HAPPY == 1
    with boa.env.prank(aryan):
        mood_nft.flip_mood(0)
    assert mood_nft.token_id_to_mood(0) == 2 # SAD == 2

def _decode_token_uri(uri):
    # Remove the "data:application/json;base64," prefix
    base64_data = uri.replace("data:application/json;base64,", "")
    
    # Decode base64 to bytes, then to string
    decoded_json = base64.b64decode(base64_data).decode('utf-8')
    return json.loads(decoded_json)

def _decode_image_from_json(json_data):
    # Extract the image data
    image_data = json_data['image']
    # Remove the "data:image/svg+xml;base64," prefix
    image_base64 = image_data.replace("data:image/svg+xml;base64,", "")
    
    # Decode the SVG
    return base64.b64decode(image_base64).decode('utf-8')

def test_token_uri(mood_nft, aryan):
    with boa.env.prank(aryan):
        mood_nft.mint_nft()
    uri = mood_nft.tokenURI(0)
    
    json_data = _decode_token_uri(uri)
    svg_content = _decode_image_from_json(json_data)
    
    # Verify it's an SVG
    assert svg_content.startswith("<svg")
    # get svg from images/
    with open("images/happy.svg", "r") as file:
        happy_svg = file.read()
    assert svg_content == happy_svg

    with boa.env.prank(aryan):
        mood_nft.flip_mood(0)
    uri = mood_nft.tokenURI(0)
    json_data = _decode_token_uri(uri)
    svg_content = _decode_image_from_json(json_data)
    assert svg_content.startswith("<svg")
    with open("images/sad.svg", "r") as file:
        sad_svg = file.read()
    assert svg_content == sad_svg


# def test_token_transfers(basic_nft, aryan, raghav):
#     with boa.env.prank(aryan):
#         basic_nft.mint(PUG_URI)
#     with boa.env.prank(aryan):
#         basic_nft.transferFrom(aryan, raghav, 0)
#     assert basic_nft.ownerOf(0) == raghav
#     assert basic_nft.balanceOf(aryan) == 0
#     assert basic_nft.balanceOf(raghav) == 1

# def test_approve_and_transfer(basic_nft, aryan, raghav, chikapa):
#     with boa.env.prank(aryan):
#         basic_nft.mint(PUG_URI)
#     assert basic_nft.ownerOf(0) == aryan
#     with boa.env.prank(aryan):
#         basic_nft.approve(chikapa, 0)
#     assert basic_nft.getApproved(0) == chikapa
#     with boa.env.prank(chikapa):
#         basic_nft.transferFrom(aryan, raghav, 0)
#     assert basic_nft.ownerOf(0) == raghav
#     assert basic_nft.totalSupply() == 1
#     assert basic_nft.balanceOf(aryan) == 0
#     assert basic_nft.balanceOf(raghav) == 1
#     assert basic_nft.balanceOf(chikapa) == 0

# def test_mint_multiple_tokens(basic_nft, aryan):
#     with boa.env.prank(aryan):
#         for i in range(3):
#             basic_nft.mint(PUG_URI)
#             assert basic_nft.tokenURI(i) == "ipfs://" + PUG_URI
#     assert basic_nft.balanceOf(aryan) == 3
#     assert basic_nft.totalSupply() == 3
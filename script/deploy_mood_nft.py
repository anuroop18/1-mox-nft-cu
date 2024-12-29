import base64

from moccasin.boa_tools import VyperContract

from contracts import mood_nft


def deploy_mood_nft() -> VyperContract:
    with (
        open("./images/happy.svg") as happy_f,
        open("./images/sad.svg") as sad_f
    ):
        happy_svg_uri = svg_to_base64_uri(happy_f.read())
        sad_svg_uri = svg_to_base64_uri(sad_f.read())
    mood_contract = mood_nft.deploy(happy_svg_uri, sad_svg_uri)
    # mood_contract.mint_nft()
    # mood_contract.flip_mood(0)
    # print(f"Mood: {mood_contract.token_id_to_mood(0)}")
    # print(f"TokenURI: {mood_contract.tokenURI(0)}")
    return mood_contract

def moccasin_main() -> VyperContract:
    return deploy_mood_nft()


def svg_to_base64_uri(svg: str) -> str:
    svg_bytes = svg.encode("utf-8")
    base64_svg = base64.b64encode(svg_bytes).decode("utf-8")
    return f"data:image/svg+xml;base64,{base64_svg}"

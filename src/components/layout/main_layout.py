from fasthtml.fastapp import *
from src.components.layout import header, footer

def render(children):
    return (
        header.render(),
        Div(children),
        footer.render()
    )
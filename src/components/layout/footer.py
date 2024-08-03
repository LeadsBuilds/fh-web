from fasthtml.fastapp import *

def render():
    return (
        Footer(
            (Div('This, is the footer', 
                 style="width:100%; font-size: 2rem")
            ),
            style="""
                min-height: 100px;
                text-align: center;
                display: flex;
                align-items: center;
                background-color: var(--pico-color-sand-950);
                margin-top: 20px;
            """
        )
    )
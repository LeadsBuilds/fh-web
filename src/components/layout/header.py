from fasthtml.fastapp import *

def render():
    return (
        Header(
            (Div('This, is the header', 
                 style="width:100%; font-size: 2rem")
            ),
            style="""
                min-height: 100px;
                text-align: center;
                display: flex;
                align-items: center;
                background-color: var(--pico-color-sand-950);
                margin-bottom: 20px;
            """
        ),
    )
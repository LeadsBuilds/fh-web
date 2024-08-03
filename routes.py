from fasthtml.fastapp import *
from src.pages.index import *

picocolorscss="https://cdn.jsdelivr.net/npm/@picocss/pico@2/css/pico.colors.min.css";

app, rt = fast_app(live=True, hdrs=(
    (Link(rel="stylesheet", href=picocolorscss),
            Style(":root { --pico-font-size: 100%; }"))
    )
)

@rt("/")
def get():
    return indexPage
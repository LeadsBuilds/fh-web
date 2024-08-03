from fasthtml.fastapp import *
from src.pages.index import *

from fasthtml.common import (
    # These are the HTML components we use in this app
    A, AX, Button, Card, Checkbox, Container, Div, Form, Grid, Group, H1, H2, Hidden, Input, Li, Main, Script, Style, Textarea, Title, Titled, Ul,
    # These are FastHTML symbols we'll use
    Beforeware, fast_app, SortableJS, fill_form, picolink, serve,
    # These are from Starlette, Fastlite, fastcore, and the Python stdlib
    FileResponse, NotFoundError, RedirectResponse, database, patch, dataclass
)

picocolorscss="https://cdn.jsdelivr.net/npm/@picocss/pico@2/css/pico.colors.min.css";

app, rt = fast_app(live=True, hdrs=(
    (Link(rel="stylesheet", href=picocolorscss),
            Style(":root { --pico-font-size: 100%; }"))
    )
)

@rt("/")
def get():
    return indexPage
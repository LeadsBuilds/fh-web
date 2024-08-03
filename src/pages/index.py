from fasthtml.fastapp import *
from src.components.layout import main_layout

page_title = "Titulo"

indexPage = (
    Title(page_title), 
    main_layout.render(
        Titled('Content Title', Div('This is the content'))
    )
)
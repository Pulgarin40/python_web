import reflex as rx
from enum import Enum
from .colors import Color as Color
from .colors import TextColor as TextColor
from .fonts import Font as Font
from .fonts import Font, FontWeight

# Constante
MAX_WIDTH= "550PX"

STYLESHEETS=[
    "https://fonts.googleapis.com/css2?family=Poppins:wght@300,500&display=swap",
    "https://fonts.googleapis.com/css2?family=Comfortaa:wght@500&display=swap"
]

# Sizes
class Size(Enum):
    CERO = "0"
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1.3em"
    LARGE = "1.5em"
    BIG = "2em"
    VERYBIG="7em"

# Styles
BASE_STYLE = {
    "font_family": Font.DEFAULT.value,
    "font_weight": FontWeight.LIGHT.value,
    "background_color": Color.BACKGROUND.value,
    rx.button: {
        "width": "100%",
        "height": "100%",  # Corregido 'heigth' a 'height'
        "display": "block",
        "padding": Size.MEDIUM.value,
        "border_radius": Size.MEDIUM.value,
        "color": TextColor.HEADER.value,
        "background_color": Color.CONTENT.value,
        "_hover":{
            "background_color": Color.SECONDARY.value
        }
    },
    rx.link : {
        "text_decoration": "none",  # Evitamos que se marquen los subrayados en los links
        "_hover": {}
    }
}


navbar_title_style = dict(
    font_family=Font.LOGO.value,
    font_weight= FontWeight.MEDIUM.value,
    font_size=Size.LARGE.value
)

title_style = dict(
    width="100%",
    font_family=Font.TITLE.value,
    font_weight= FontWeight.MEDIUM.value,
    padding_top=Size.DEFAULT.value,  # Asegúrate de que esto sea interpretado correctamente por tu framework/CSS
    color=TextColor.HEADER.value  # Cambiado 'Color' a 'color'
)

button_title_style = dict(
    font_family=Font.TITLE.value,
    font_weight= FontWeight.MEDIUM.value,
    size=Size.DEFAULT.value,  # Cambiado 'Size' a 'size' si es que debe ser 'size'
    color=TextColor.HEADER.value
)

button_body_style = dict(
    size=Size.DEFAULT.value,  # Cambiado 'Size' a 'size' si es que debe ser 'size'
    color=TextColor.BODY.value
)

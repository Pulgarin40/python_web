import reflex as rx
from python_web.styles.styles import Size as Size
from python_web.styles.colors import TextColor as TextColor
from python_web.styles.colors import Color as Color

import reflex as rx
from python_web.styles.styles import Size

def info_text(title: str, body: str) -> rx.Component:
    return rx.hstack(
        rx.text(title, font_weight="bold", color=Color.PRIMARY.value, font_size=Size.MEDIUM.value),
        rx.text(body, font_size=Size.MEDIUM.value),
        align_items="center",
        color=TextColor.BODY.value
    )
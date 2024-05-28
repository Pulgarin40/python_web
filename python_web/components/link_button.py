import reflex as rx
import python_web.styles.styles as styles
from python_web.styles.styles import Size as Size

def link_button(title: str, body: str, url: str, icon_tag: str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon(
                    tag=icon_tag,
                    width=styles.Size.DEFAULT.value,
                    height=styles.Size.DEFAULT.value,
                    marging=Size.MEDIUM.value
                ),
                rx.vstack(
                    rx.text(title, style=styles.button_title_style),
                    rx.text(body, style=styles.button_body_style),
                    align_items="start"                  
                )
            )
        ),
        href=url,
        is_external=True,  # Para que lo abra en una página nueva
        width="100%"
    )

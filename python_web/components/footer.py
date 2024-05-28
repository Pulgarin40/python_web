import reflex as rx
import datetime
from python_web.styles.styles import Size as Size
from python_web.styles.colors import TextColor as TextColor

def footer() -> rx.Component:
    return rx.vstack(
        
        rx.image(
            src="/logo4.jpg",
            height=Size.VERYBIG.value,
            weight=Size.VERYBIG.value,
            alt="Logotipo de PulgaDev. Una J y Una P. "
        ),
        rx.link(
             f"@2022-{datetime.date.today().year} PulgarinDev by Juan Pablo Bermúdez v3",
             href="https://linkedin.com/in/pulgarin40",
             is_external=True,
             font_size=Size.MEDIUM.value
        ),
        rx.text(
            " BUILLDING SOFTWARE WITH FROM CHIPIONA TO THE WORLD.",
            font_size=Size.MEDIUM.value,
            margin_top="0px !important"
        ),
        margin_bottom=Size.BIG.value,
        padding_bottom=Size.BIG.value,
        align="center",
        color=TextColor.FOOTER.value
    
    )
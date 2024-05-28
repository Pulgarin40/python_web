import reflex as rx
from python_web.styles.colors import TextColor
from python_web.styles.styles import Size, button_title_style, button_body_style

def certificaciones_page() -> rx.Component:
    return rx.vstack(
        rx.heading("Certificaciones", size="7", color=TextColor.HEADER.value),
        rx.text(
            "Aquí están todas mis certificaciones.",
            style={"margin_top": "1em"},
            color=TextColor.BODY.value
        ),
        rx.grid(
            *[rx.image(src=f"/assets/certificaciones/cert{i}.png", alt=f"Certificación {i}") for i in range(1, 14)],
            template_columns="repeat(auto-fit, minmax(200px, 1fr))",
            gap="1em"
        ),
        width="100%",
        spacing="2"
    )

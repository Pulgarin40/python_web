import reflex as rx
from python_web.components.link_icon import link_icon
from python_web.components.info_text import info_text
from python_web.styles.styles import Size
from python_web.styles.fonts import Font
from python_web.styles.colors import Color as Color
from python_web.styles.colors import TextColor as TextColor

def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
               src="/avatar2.jpeg",
               size="8",
               color=TextColor.BODY.value,
               bg=Color.CONTENT.value,
               padding="4px",
               border="7px",
               border_color=Color.PRIMARY.value
            ),
            rx.vstack(
                rx.heading(
                    "JUAN PABLO BERMÚDEZ PULGARIN",
                    size="7",
                    color=TextColor.HEADER.value,
                ),
                rx.text(
                    "@jberpu82",
                    margin_top="0px !important",
                    color=TextColor.BODY.value
                ),
                rx.hstack(
                    link_icon("icons/linkedin.svg","https://www.linkedin.com/in/pulgarin40/", "Linkedin"),
                    link_icon("icons/x-twitter.svg","https://x.com/home/", "Twitter"),
                    link_icon("icons/github.svg","https://github.com/Pulgarin40?tab=repositories/", "Github"),
                    spacing="5"  # Añadido espaciado entre iconos si es necesario
                ),
                align_items="start"
            ),
            spacing="7"  # Espaciado entre avatar y vstack
        ),
        rx.flex(
            info_text("💂", "Inglés"),  # Eliminar espacio innecesario después de "1"
            rx.spacer(),
            info_text("🎓", "Grado Superior en Desarrollo Web"),  
            rx.spacer(),
            info_text("+18", "Certificaciones"),  
            width="100%"
        ),
        rx.text(
            f"""
            Soy desarrollador web junior desde hace apenas menos de un año.
            Recién llegado a este mundo del desarrollo web, intento mejorar cada día.
            Soy una persona curiosa y con ganas de aprender. Aquí dejo mis enlaces
            a mis proyectos. ¡Bienvenid@!""",
            style={"margin_top": "1em"},  # Añadir margen superior para separar el texto
            color=TextColor.BODY.value
        ),
        spacing="7",
        align_items="start"
    )



import reflex as rx
from python_web.components.navbar import navbar
from python_web.views.header import header
from python_web.views.links.links import links
from python_web.components.footer import footer
import python_web.styles.styles as styles
from python_web.styles.styles import Size
from python_web.views.certificaciones_page import certificaciones_page


"""
#Definimos el estado de la aplicación
class State(rx.State):
    pass

"""

# Definimos la página principal
def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                links(),
                align="center",
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=Size.BIG.value,
                padding=Size.BIG.value
            )
        ),
        footer()
    )

# Creamos la aplicación Reflex
app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE
)

# Agregamos las páginas a la aplicación
app.add_page(
    index,
    title="Porfolio_con_Reflex"
)

app.add_page(
    certificaciones_page,
    route="/certificaciones_page"
)




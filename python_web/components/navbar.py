import reflex as rx
import python_web.styles.styles as styles
from python_web.styles.styles import Size as Size
from python_web.styles.colors import Color as Color

def navbar() -> rx.Component:
    return rx.hstack(    #Este hstack está representando la barra de navegación 
      rx.box(
            rx.text("PULGA", color=Color.PRIMARY.value, font_weight="bold", display="inline"),
            rx.text("DEV", color=Color.SECONDARY.value, font_weight="bold", display="inline"),
            style=styles.navbar_title_style
        ),
        

      position="sticky",
      bg=Color.CONTENT.value,
      padding_x=Size.DEFAULT.value,
      padding_y=Size.SMALL.value,
      z_index="999",
      top="0"
      
  )
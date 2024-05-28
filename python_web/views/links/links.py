import reflex as rx
from python_web.components.link_button import link_button
from python_web.components.title import title
import python_web.styles.styles as styles

def links() -> rx.Component:
    return rx.vstack(
        title("Información"),
        link_button("Biografía", "", "https://linkedin.com/in/pulgarin40", "user"),
        link_button("Proyectos", "", "https://linkedin.com/in/pulgarin40","folder"),
        link_button("CV", "", "https://drive.google.com/drive/u/1/home", "file_text"),
        link_button("Certificaciones", "", "/certificaciones_page", "award"),
      
        title("Contacto"),
        link_button("Email", "jberpu82@gmail.com" ,f"mailto:https://mail.google.com/mail/","mail"),
        width="100%",
        spacing="2"  # Ajustado a "2em" para consistencia
    )

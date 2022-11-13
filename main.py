import flet
from flet import Container, ElevatedButton, Page, animation
from flet.transform import Scale

def main(page: Page):

    c = Container(
        width=100,
        height=100,
        bgcolor="blue",
        border_radius=5,
        scale=Scale(scale=1),
        animate_scale=animation.Animation(600, "bounceOut"),
    )

    def animate(e):
        # c1.rotate = 1
        c.scale = 2
        page.update()

    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.spacing = 30
    page.add(
        c,
        ElevatedButton("Animate!", on_click=animate),
    )

flet.app(target=main)
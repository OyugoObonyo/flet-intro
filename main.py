import flet
from flet import Page, Text, Column, Row

def main(page: Page):
    # page.add(x) can be used in place of page.controls.append(x)
    page.add(
        Row(controls = [
            Text(value="Hello World red!", color="red"),
            Text(value="Hello World green!", color="green"),
            Text(value="Hello World blue!", color="blue")
        ])
    )
    page.update()


flet.app(target=main, view=flet.WEB_BROWSER)
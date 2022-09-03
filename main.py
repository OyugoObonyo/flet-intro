from time import sleep
import flet
from flet import Page, Text, Column, Row

def main(page: Page):
    t = Text(value="Hello World!", color="red")
    # page.add(x) can be used in place of page.controls.append(x)
    page.add(t)
    for i in range(1, 11):
        t.value = f"Hello world {i}"
        page.update()
        sleep(1)

flet.app(target=main, view=flet.WEB_BROWSER)
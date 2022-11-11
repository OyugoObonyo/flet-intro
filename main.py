import flet
from flet import ListView, Page, Text

def main(page: Page):
    lv = ListView(height=250, spacing=15)
    for i in range(5000):
        lv.controls.append(Text(f"Line {i}"))
    page.add(lv)

flet.app(target=main, view=flet.WEB_BROWSER)
import flet
from flet import Page, Text, TextField, Row, ElevatedButton

def main(page: Page):
    # page.add(x) can be used in place of page.controls.append(x)
    def button_clicked(event):
        page.add(Text("CLICKED"))
        print("CLICKED and e is: ", event)

    page.add(
        Row(controls = [
            TextField(label="What is your name?"),
            ElevatedButton(text="Say my name!", on_click=button_clicked)
        ])
    )
    page.update()


flet.app(target=main, view=flet.WEB_BROWSER)
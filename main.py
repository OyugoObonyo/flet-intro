import flet
from flet import Page, TextField, Row, ElevatedButton, Checkbox, Text, Column

def main(page: Page):
    
    page.title = "TODO App"
    first_name = TextField(label="First name", autofocus=True, width=300)
    last_name = TextField(label="Last name", width=300)
    greetings = Column()

    def button_clicked(e):
        greetings.controls.append(Text(f"Hello {first_name.value} {last_name.value}"))

    page.add(
        first_name,
        last_name,
        ElevatedButton("Greet me", on_click=button_clicked),
        greetings
    )
    page.update()
    
if __name__ == "__main__":
    flet.app(target=main, port=5500, view=flet.WEB_BROWSER)
import flet
from flet import(
    Page, TextField,
    Row, ElevatedButton,
    Checkbox, Text, Column,
    IconButton, icons
)

# To run your flet app in hot reload mode,
# run flet name_of_entry_point.py -d 
def main(page: Page):

    page.title = "TODO App"
    page.horizontal_alignment = "center"
    heading = Text(
        value="Provide your full name",
        size=30,
        color="blue",
        weight="bold")
    first_name = TextField(label="First name", text_align="right", autofocus=True, width=300)
    last_name = TextField(label="Last name", width=300)

    def button_clicked(e):
        if not first_name.value:
            first_name.error_text = "First name cannot be blank"
            page.update()
        if not last_name.value:
            last_name.error_text = "Last name cannot be blank"
            page.update()
        else:
            page.add(Text(f"Hello {first_name.value} {last_name.value}!"))
    
    accept_button = IconButton(icons.LOGOUT_SHARP , icon_color="blue", on_click=button_clicked)

    page.add(
        heading,
        first_name,
        last_name,
        accept_button
    )
    page.update()

if __name__ == "__main__":
    flet.app(target=main, port=5500, view=flet.WEB_BROWSER)
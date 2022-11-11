import flet
from flet import(
    Page, TextField,
    Row, ElevatedButton,
    Checkbox, Text, Column
)

# To run your flet app in hot reload mode,
# run flet name_of_entry_point.py -d 
def main(page: Page):
    page.title = "TODO App"
    heading = Text(
        value="Provide your full name",
        size=30,
        color="blue",
        weight="bold")
    first_name = TextField(label="First name", autofocus=True, width=300)
    last_name = TextField(label="Last name", width=300)

    page.add(
        heading,
        first_name,
        last_name,
    )
    page.update()
    
if __name__ == "__main__":
    flet.app(target=main, port=5500, view=flet.WEB_BROWSER)
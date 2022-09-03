from hashlib import new
import flet
from flet import Page, Text, TextField, Row, ElevatedButton, Checkbox

def main(page: Page):
    # page.add(x) can be used in place of page.controls.append(x)
    def add_clicked(event):
        page.add(Checkbox(label=new_task.value))
    
    new_task = TextField(hint_text="Add a task", width = 300)
    page.add(Row([
        new_task,
        ElevatedButton("Add", on_click=add_clicked)
        ]))
    page.update()


flet.app(target=main)
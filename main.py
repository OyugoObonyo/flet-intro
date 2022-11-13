import flet
from flet import(
        Page,
)

def app(page: Page) -> None:
    page.title = "Demo application"
    page.update()

def main() -> None:
    flet.app(target=app, port=5550, view=flet.WEB_BROWSER)

if __name__ == "__main__":
    main()
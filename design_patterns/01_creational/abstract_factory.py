"""
# Design Pattern: Abstract Factory (Creational)

## Intent
Provides an interface for creating families of related or dependent objects without specifying their concrete classes.

## Use Cases
- Cross-platform UI toolkit (Windows, macOS, Linux buttons, checkboxes, dialogs).
- Multi-database connection and query builder suites (PostgreSQL vs MySQL vs SQLite).
- Theming systems (Dark Theme vs Light Theme suites).
"""

from abc import ABC, abstractmethod


# 1. Abstract Products
class Button(ABC):
    @abstractmethod
    def render(self) -> str:
        pass


class Checkbox(ABC):
    @abstractmethod
    def render(self) -> str:
        pass


# 2. Concrete Products for Light Theme
class LightButton(Button):
    def render(self) -> str:
        return "<Button style='bg: #ffffff, text: #000000'>Light Button</Button>"


class LightCheckbox(Checkbox):
    def render(self) -> str:
        return "<Checkbox style='border: #cccccc'>Light Checkbox</Checkbox>"


# 3. Concrete Products for Dark Theme
class DarkButton(Button):
    def render(self) -> str:
        return "<Button style='bg: #1e1e1e, text: #ffffff'>Dark Button</Button>"


class DarkCheckbox(Checkbox):
    def render(self) -> str:
        return "<Checkbox style='border: #444444'>Dark Checkbox</Checkbox>"


# 4. Abstract Factory
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass


# 5. Concrete Factories
class LightThemeFactory(GUIFactory):
    def create_button(self) -> Button:
        return LightButton()

    def create_checkbox(self) -> Checkbox:
        return LightCheckbox()


class DarkThemeFactory(GUIFactory):
    def create_button(self) -> Button:
        return DarkButton()

    def create_checkbox(self) -> Checkbox:
        return DarkCheckbox()


# 6. Client Code
class Application:
    def __init__(self, factory: GUIFactory):
        self.button = factory.create_button()
        self.checkbox = factory.create_checkbox()

    def render_ui(self) -> list[str]:
        return [self.button.render(), self.checkbox.render()]


# =====================================================================
# Tests
# =====================================================================
def test_abstract_factory():
    light_app = Application(LightThemeFactory())
    rendered_light = light_app.render_ui()
    assert "#ffffff" in rendered_light[0]
    assert "Light Checkbox" in rendered_light[1]

    dark_app = Application(DarkThemeFactory())
    rendered_dark = dark_app.render_ui()
    assert "#1e1e1e" in rendered_dark[0]
    assert "Dark Checkbox" in rendered_dark[1]


if __name__ == "__main__":
    test_abstract_factory()
    print("Abstract Factory tests passed successfully! [OK]")

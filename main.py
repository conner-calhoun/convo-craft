from dearpygui import core, simple, demo

from convo.view import MainMenu
from convo import config

# Create windows
mm = MainMenu()

# Default theme
core.set_theme(config.DEFAULT_THEME)

core.add_additional_font('res/fonts/RobotoCondensed-Regular.ttf', 20)

core.set_main_window_title('Convo-Craft')
core.set_main_window_size(*config.DEFAULT_WINDOW_SIZE)
core.start_dearpygui()

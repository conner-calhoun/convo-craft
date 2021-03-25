from dearpygui import core, simple, demo

from convo.main_menu import MainMenu
from convo import config

# Create windows
mm = MainMenu()

# Default theme
core.set_theme('Cherry')

core.set_main_window_title('Convo-Craft')
core.set_main_window_size(*config.DEFAULT_WINDOW_SIZE)
core.start_dearpygui()
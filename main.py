from dearpygui import core, simple, demo

from convo.view import MainView
from convo import config

# Create windows
mm = MainView()
mm.draw()

# Default theme
core.set_theme(config.DEFAULT_THEME)

# demo.show_demo()

core.set_main_window_title('Convo-Craft')
core.set_main_window_size(*config.DEFAULT_WINDOW_SIZE)
core.start_dearpygui()

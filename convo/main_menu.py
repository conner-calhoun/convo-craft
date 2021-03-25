from dearpygui import core, simple

from convo import config

class MainMenu:
    def __init__(self):
        with simple.window('Convo-Craft', **config.MENU_CONFIG):
            self.title_bar()
            core.add_text('Hello World')

    def title_bar(self):
        '''
        Creates the titlebar / menu
        '''
        with simple.menu_bar('Main Menu'):

            with simple.menu('File'):
                core.add_menu_item('Save', callback=self.save)
                core.add_menu_item('Save As', callback=self.save_as)

            core.add_separator()

            with simple.menu('Settings'):
                with simple.menu('Theme'):
                    for theme in config.THEMES:
                        core.add_menu_item(theme, callback=self.set_theme)

    def save(self):
        '''
        Save Callback
        '''
        print('SAVING...')

    def save_as(self):
        '''
        Save as callback
        '''
        pass

    def set_theme(self, theme):
        '''
        Sets the theme
        '''
        core.set_theme(theme)
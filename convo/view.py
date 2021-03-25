from dearpygui import core, simple

from convo import config, dialogue

class View:
    '''
    Base View Class
    '''
    def __init__(self):
        self.title = ''

class MainMenu:
    def __init__(self):
        self.tree = dialogue.DialogueTree()
        self.active_theme = config.DEFAULT_THEME
        self.title = 'Convo-Craft'

        self.draw()

    def draw(self):
        '''
        Draws the MainMenu
        '''
        with simple.window(self.title, **config.MENU_CONFIG):
            with simple.menu_bar('Main Menu'):

                with simple.menu('File'):
                    core.add_menu_item('New', callback=self.new)
                    core.add_menu_item('Open', callback=self.open_file)
                    core.add_menu_item('Save', callback=self.save)
                    core.add_menu_item('Save As', callback=self.save_as)

                with simple.menu('Settings'):
                    with simple.menu('Theme'):
                        for theme in config.THEMES:
                            # TODO find a way to have the default theme "checked" by default
                            core.add_menu_item(theme, callback=self.set_theme, check=True)

    def refresh(self):
        '''
        Refreshes the MainMenu
        '''
        core.delete_item(self.title)
        self.draw()

    def new(self):
        '''
        Creates a new dialogue menu
        '''
        # TODO: ask if the user is sure, as it will delete editor contents

        self.tree = dialogue.DialogueTree()

    def open_file(self):
        '''
        Opens / Reads the json file
        '''
        # TODO: read the passed in json file and create the dialogue tree from it
        # then re-create the node editor to match the dialogue tree
        pass

    def save(self):
        '''
        Save Callback
        '''
        # TODO: save the following
        self.tree.to_json()

    def save_as(self):
        '''
        Save as callback
        '''
        # TODO: open a modal, take in a filename, and save the json file
        filename = 'replace-me'
        self.tree.name = filename

        self.save

    def set_theme(self, theme):
        '''
        Sets the theme
        '''
        core.set_theme(theme)
        self.active_theme=theme
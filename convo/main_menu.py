from dearpygui import core, simple

from convo import config, dialogue

class MainMenu:
    def __init__(self):
        self.tree = dialogue.DialogueTree()

        with simple.window('Convo-Craft', **config.MENU_CONFIG):
            self.title_bar()
            core.add_text('Hello World')

    def title_bar(self):
        '''
        Creates the titlebar / menu
        '''
        with simple.menu_bar('Main Menu'):

            with simple.menu('File'):
                core.add_menu_item('New', callback=self.new)
                core.add_menu_item('Open', callback=self.open_file)
                core.add_menu_item('Save', callback=self.save)
                core.add_menu_item('Save As', callback=self.save_as)

            core.add_separator()

            with simple.menu('Settings'):
                with simple.menu('Theme'):
                    for theme in config.THEMES:
                        core.add_menu_item(theme, callback=self.set_theme)

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
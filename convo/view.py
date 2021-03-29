from dearpygui import core, simple

from convo import config, dialogue


class View:
    '''
    Base View Class
    '''

    def __init__(self):
        self.title = ''

    def draw(self):
        '''
        Must Implement
        '''
        raise NotImplementedError

    def refresh(self):
        '''
        Refreshes the MainMenu

        usage -- NOTE: draw() must be called before refresh()
        '''
        core.delete_item(self.title)
        self.draw()


class DialogueEditor(View):
    '''
    Dialogue Node Editor
    '''

    def __init__(self):
        pass


class MainMenu(View):
    '''
    Titlebar / MainMenu class
    '''

    def __init__(self):
        self.tree = dialogue.DialogueTree()
        self.active_theme = config.DEFAULT_THEME
        self.title = 'Convo-Craft'

        self.node_index = 0
        self.nodes = {}

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
                            core.add_menu_item(
                                theme, callback=self.set_theme, check=True)

            if self.tree.name:
                core.add_text("Tree: {}".format(self.tree.name))
            else:
                core.add_text("Tree: <unnamed>.json")

            with simple.node_editor("Dialogue Tree"):
                # Add the root node
                self.create_node()

                # Add some sample responses for now
                self.add_response()
                self.add_response()

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
        if self.tree.name:
            self.tree.to_json()
        else:
            self.save_as()

    def save_as(self):
        '''
        Save as callback
        '''
        # TODO: open a modal, take in a filename, and save the json file
        filename = 'replace-me'
        self.tree.name = filename

        self.save()

    def set_theme(self, theme):
        '''
        Sets the theme
        '''
        core.set_theme(theme)
        self.active_theme = theme

    def add_response(self):
        '''
        Creates a response node
        '''
        self.create_node("Response")

    def create_node(self, node_type="Root Prompt"):
        '''
        Creates a node
        '''
        node_name = "{}##{}".format(node_type, self.node_index)

        with simple.node(node_name):
            with simple.node_attribute("ID##{0}".format(self.node_index), static=True):
                core.add_text("ID: {}".format(self.node_index))
            with simple.node_attribute("Input##{}".format(self.node_index)):
                pass
            with simple.node_attribute("Output##{}".format(self.node_index), output=True):
                core.add_input_text("Text##{}".format(
                    self.node_index), width=200, height=200)
            with simple.node_attribute("IsEnd##{}".format(self.node_index), static=True):
                core.add_checkbox("IS End##{}".format(self.node_index))

        self.nodes[self.node_index] = node_name

        if node_type == "Response":
            self.tree.add_response()
        else:
            self.tree.add_prompt()

        self.node_index += 1

from dearpygui import core, simple

import json


class Prompt:
    '''
    Prompt Class
    '''

    def draw_node(self):
        # TODO: draw the imnode
        pass

    def to_json(self):
        pass


class Response:
    '''
    Response Class
    '''

    def draw_node(self):
        # TODO: draw the imnode
        pass

    def to_json(self):
        pass


class DialogueTree:
    '''
    DialogueTree, keeps a list of nodes (Prompts and Responses)
    '''

    def __init__(self, name='default_name'):
        self.name = name
        self.nodes = []

    def to_json(self):
        return json.dumps({
            'name': self.name
        })

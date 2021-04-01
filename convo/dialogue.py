from dearpygui import core, simple

import json


class Node:
    def __init__(self):
        self.id = 0


class Prompt(Node):
    '''
    Prompt Class
    '''

    def draw_node(self):
        # TODO: draw the imnode
        pass

    def to_json(self):
        return {
            'id': self.id
        }


class Response(Node):
    '''
    Response Class
    '''

    def __init__(self):
        self.is_end = False
        self.has_callback = False

    def draw_node(self):
        # TODO: draw the imnode
        pass

    def to_json(self):
        return {
            'id': self.id
        }


class DialogueTree:
    '''
    DialogueTree, keeps a list of nodes (Prompts and Responses)
    '''

    def __init__(self, name=None):
        self.name = name
        self.nodes = []

    def add_prompt(self):
        self.nodes.append(Prompt())

    def add_response(self):
        self.nodes.append(Response())

    def to_json(self):
        return json.dumps({
            'name': self.name,
            'nodes': [node.to_json() for node in self.nodes]
        })

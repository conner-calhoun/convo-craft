# Convo-Craft

A tool for creating dialogue trees.


### How it works

Works on a Prompt/Response system. Prompts are made by NPCs and Responses are made by the player.

A prompt can point to many responses. A response can only point to one prompt.


Response Optional Fields:

- Parameter option. If the parameter check is selected the game will need to pass a "check" function that returns true/false if the check is passed and the response can be made.
- Callback option. If the callback check is selected, the game will need to pass in a callback function that gets triggered when the response is made.
""" A RecipeController Module """

from masonite.controllers import Controller
from masonite.request import Request
from app.Recipe import Recipe

class RecipeController(Controller):
    
    def __init__(self, request: Request):
        self.request = request

    def index(self):
        return Recipe.all()

    def show(self):
        id = self.request.param('id')
        return Recipe.find(id)

    def create(self):
        name = self.request.input('name')
        image = self.request.input('image')
        instructions = self.request.input('instructions')
        ingredients = self.request.input('ingredients')
        url = self.request.input('url')
        recipe = Recipe.create({"name": name, "image": image, "instructions": instructions, "ingredients": ingredients, "url": url})
        print(recipe)
        return recipe

    def update(self):
        id = self.request.param('id')
        name = self.request.input('name')
        image = self.request.input('image')
        instructions = self.request.input('instructions')
        ingredients = self.request.input('ingredients')
        url = self.request.input('url')
        Recipe.where('id', id).update({"name": name, "image": image, "instructions": instructions, "ingredients": ingredients, "url": url})
        return Recipe.find(id)

    def destroy(self):
        id = self.request.param('id')
        recipe = Recipe.where('id', id).get()
        Recipe.where('id', id).delete()
        return recipe
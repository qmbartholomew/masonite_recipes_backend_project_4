"""Web Routes."""

from masonite.routes import Get, Post, Put, Delete, RouteGroup

ROUTES = [
    Get("/", "WelcomeController@show").name("welcome"),

    RouteGroup([
        Get('/', 'RecipeController@index').name('index'),
        Get('/@id', 'RecipeController@show').name('show'),
        Post('/', 'RecipeController@create').name('create'),
        Put('/@id', 'RecipeController@update').name('update'),
        Delete('/@id', 'RecipeController@destroy').name('destroy')
    ], prefix='/recipes', name='recipes')
]

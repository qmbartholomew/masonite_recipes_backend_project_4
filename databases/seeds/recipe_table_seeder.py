"""RecipeTableSeeder Seeder."""

from masoniteorm.seeds import Seeder
from app.Recipe import Recipe


class RecipeTableSeeder(Seeder):
    def run(self):
        Recipe.create({"name": "Bread Pudding", "image": "https://www.lifeloveandsugar.com/wp-content/uploads/2021/02/Classic-Bread-Pudding5.jpg", "instructions": "Mix ingredients, bake, add pudding", "ingredients": "Flower, Eggs, Yeast Pudding", "url": "No reference"})

"""CreateRecipesTable Migration."""

from masoniteorm.migrations import Migration


class CreateRecipesTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("recipes") as table:
            table.increments("id")
            table.string("name")
            table.string("description").default("A delicious meal!")
            table.string("image")
            table.string("instructions")
            table.string("ingredients")
            table.string("author").default("Original Recipe")
            table.string("url")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("recipes")

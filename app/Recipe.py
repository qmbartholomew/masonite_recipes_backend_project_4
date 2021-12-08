"""Recipe Model."""

from masoniteorm.models import Model


class Recipe(Model):
    __table__="recipes"
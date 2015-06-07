from django.db import models


class Technology(models.Model):
    """
    name
    description

    Reverse relations can be used to compute experience of the lanuage

    This class should be abstract
    """
    pass


class Category(Technology):
    pass


class Framework(Technology):
    pass


class Lanuages(Technology):
    pass


class Project(models.Model):
    """
    name
    languages -> one-to-many Lanuage
    categories -> one-to-many Category
    frameworks -> one-to-many Framework
    """
    pass

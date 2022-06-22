from tortoise.models import Model
from tortoise import fields


class Team(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)

    def __str__(self):
        return self.name

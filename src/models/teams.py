from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator


class Team(models.Model):
    """model of Team"""

    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)

    def __str__(self):
        return self.name


Team_Pydantic = pydantic_model_creator(Team, name="Team")
TeamIn_Pydantic = pydantic_model_creator(Team, name="TeamIn", exclude=("id",))

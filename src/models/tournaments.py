from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator


class Tournament(models.Model):
    """models of Tournament"""

    name = fields.CharField(max_length=255)

    def __str__(self):
        return self.name


Tournament_Pydantic = pydantic_model_creator(Tournament, name="Tournament")
TournamentIn_Pydantic = pydantic_model_creator(Tournament, name="TournamentIn")

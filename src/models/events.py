from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator


class Event(models.Model):
    """model of Events"""

    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    tournament = fields.ForeignKeyField("models.Tournament", related_name="events")
    participants = fields.ManyToManyField(
        "models.Team", related_name="events", through="event_team"
    )

    def __str__(self):
        return self.name


Event_Pydantic = pydantic_model_creator(Event, name="Event")
EventIn_Pydantic = pydantic_model_creator(Event, name="EventIn")

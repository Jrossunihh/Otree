from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import random

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'cheap_talk_instructions'
    players_per_group = 3
    num_rounds = 1


class Subsession(BaseSubsession):
    def creating_session(self):
        self.group_randomly(fixed_id_in_group=True)


class Group(BaseGroup):

    pass

class Player(BasePlayer):

    workerid = models.StringField()
    q11 = models.IntegerField()
    q12 = models.IntegerField()
    q21 = models.IntegerField()
    q22 = models.IntegerField()
    q31 = models.IntegerField(
        choices=[
            [1, 'Yes'],
            [0, 'No'],
        ]
    )
    q32 = models.IntegerField(
        choices=[
            [1, 'Yes'],
            [0, 'No'],
        ]
    )
    errors = models.IntegerField(initial=0)



 #   Q1 = models.IntegerField(
 #       choices=[
 #           [1, 'Answer1'],
 #           [2, 'Answer2'],
 #           [3, 'Answer3'],
 #       ],
 #       widget = widgets.RadioSelect
 #   )




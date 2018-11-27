from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range,
)
import random

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'voting'
    players_per_group = 3
    num_rounds = 1


class Subsession(BaseSubsession):
    def creating_session(self):
        for player in self.get_players():
            player.signal = random.choice([1, 9])


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    workerid = models.StringField()
    message = models.IntegerField(
        choices = [
                  [1, '1'],
                  [2, '9'],
              ],
        widget = widgets.RadioSelect
    )

    choice = models.IntegerField(
        choices=[
                [1, 'A'],
                [2, 'B'],
            ],
        widget = widgets.RadioSelect
    )
    signal = models.IntegerField(initial=1)


    def role(self):
        if self.id_in_group == 1 or self.id_in_group == 2:
            return 'Sender'
        if self.id_in_group == 3:
            return 'Receiver'
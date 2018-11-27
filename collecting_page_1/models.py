from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'collecting_page_1'
    players_per_group = 6
    num_rounds = 1


class Subsession(BaseSubsession):
    # def creating_session(self):
    #     self.participant.vars['skip_the_end_of_app_collecting_page_1'] = False
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    skip = models.BooleanField()

    pass

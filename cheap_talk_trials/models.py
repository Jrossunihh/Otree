from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'cheap_talk_trials'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    trialmessage1 = models.IntegerField(
        choices=[
            [1, '1'],
            [3, '3'],
            [5, '5'],
            [7, '7'],
            [9, '9'],
        ],
        widget=widgets.RadioSelectHorizontal)

    trialmessage2 = models.IntegerField(
        choices=[
            [1, '1'],
            [3, '3'],
            [5, '5'],
            [7, '7'],
            [9, '9'],
        ],
        widget=widgets.RadioSelectHorizontal)

    trialchoice1 = models.IntegerField(
        choices=[
            [0, 'A'],
            [1, 'B'],
        ],
        widget=widgets.RadioSelectHorizontal
    )
    trialchoice2 = models.IntegerField(
        choices=[
            [0, 'A'],
            [1, 'B'],
        ],
        widget=widgets.RadioSelectHorizontal
    )
    #
    # def trialsignalsender(self):
    #     if self.round_number == 1:
    #         return 5
    #     if self.round_number == 2:
    #         return 9
    #     if self.round_number == 3:
    #         return 1
    #
    # def trialsignalreceiver1(self):
    #     if self.round_number == 1:
    #         return 1
    #     if self.round_number == 2:
    #         return 5
    #     if self.round_number == 3:
    #         return 7
    #
    # def trialsignalreceiver2(self):
    #     if self.round_number == 1:
    #         return 9
    #     if self.round_number == 2:
    #         return 5
    #     if self.round_number == 3:
    #         return 3
    #
    # def role_continuous(self):
    #     return self.participant.vars['role']
    #
    # def bla(self):
    #     if self.participant.vars['type'] != 1:
    #         return 'receiver'
    #     else:
    #         return 'sender'

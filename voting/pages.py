from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random

class instructions(Page):
    form_model = 'player'
    form_fields = ['workerid']

class senderchoice(Page):
    form_model = 'player'
    form_fields = ['message']
    def is_displayed(self):
        return self.player.id_in_group == 1 or self.player.id_in_group == 2


class receiverchoice(Page):
    form_model = 'player'
    form_fields = ['choice']
    def is_displayed(self):
        return self.player.id_in_group == 3

class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class Results(Page):
    pass


page_sequence = [
    instructions,
    senderchoice,
    receiverchoice
]

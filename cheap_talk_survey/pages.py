from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Questionaire(Page):
    form_model = 'player'
    form_fields = ['gender', 'age', 'income', 'education', 'riskaversion', 'nationality']


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class Results(Page):
    pass


page_sequence = [
    Questionaire
]

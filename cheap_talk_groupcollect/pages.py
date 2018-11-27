from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

import random

class GroupingWaitPage(WaitPage):
    group_by_arrival_time = True

    def get_players_for_group(self, waiting_players):
        if len(waiting_players) >= 8:
            random.shuffle(waiting_players)
            return waiting_players

    def is_displayed(self):
        return self.round_number == 1




page_sequence = [
    GroupingWaitPage,
]

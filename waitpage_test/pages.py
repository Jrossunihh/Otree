from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

from otree_mturk_utils.pages import CustomMturkPage, CustomMturkWaitPage


class Grouping1(CustomMturkWaitPage):
    group_by_arrival_time = True

    def get_players_for_group(self, waiting_players):
        # sender_players = [p for p in waiting_players if p.participant.vars['type'] == 0]
        # receiver_players = [p for p in waiting_players if p.participant.vars['type'] == 1]
        # if len(sender_players) >= 2 and len(receiver_players) >= 2:
        #     print('creating group')
        #     return [1, 2], [3, 4]
        #
        # print('not enough players to create a group')
        sender_players = [p for p in waiting_players]
        if len(sender_players) >= 2:
            print('creating group of 2')
            return [sender_players[0], sender_players[1]]

        print('not enough players to create a group')



page_sequence = [
    Grouping1
]

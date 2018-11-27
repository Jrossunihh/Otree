from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from otree_mturk_utils.pages import CustomMturkPage, CustomMturkWaitPage

class MyPage(Page):
    pass


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass

class GroupingWaitPage(WaitPage):
    group_by_arrival_time = True

    def get_players_for_group(self, waiting_players):
        self.subsession.do_my_shuffle(waiting_players)

    # def after_all_players_arrive(self):
    #     self.subsession.do_my_shuffle()

    # def do_my_shuffle(self, waiting_players):
    #     zero_players = [p for p in waiting_players if p.participant.vars['type'] == 0]
    #     one_players = [p for p in waiting_players if p.participant.vars['type'] == 1]
    #     if len(zero_players) >= 2 and len(one_players) >= 2:
    #         return [zero_players[0], one_players[0], zero_players[1], one_players[1]]

    # def get_players_for_group(self, waiting_players):
    #     zero_players = [p for p in waiting_players if p.participant.vars['type'] == 0]
    #     one_players = [p for p in waiting_players if p.participant.vars['type'] == 1]
    #     if len(zero_players) >= 2 and len(one_players) >= 2:
    #         return [zero_players[0], one_players[0], zero_players[1], one_players[1]]

class Results(Page):
    pass


page_sequence = [
    GroupingWaitPage,
    MyPage
]

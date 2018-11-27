from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
# class Startup(WaitPage):
#
#     pass
import random
class WorkerID(Page):
    form_model = 'player'
    form_fields = ['workerid']

class Instructions1(Page):
    def is_displayed(self):
        return self.player.round_number == 1

class Instructions2(Page):
    def is_displayed(self):
        return self.player.round_number == 1

class Instructions3(Page):
    def is_displayed(self):
        return self.player.round_number == 1

class Instructions4(Page):
    def is_displayed(self):
        return self.player.round_number == 1

class Image1(Page):
    def is_displayed(self):
        return self.player.round_number == 1

class Image2(Page):
    def is_displayed(self):
        return self.player.round_number == 1

class Q1(Page):

    form_model = 'player'
    form_fields = ['q11', 'q12', 'q21', 'q22', 'q31', 'q32']

    def error_message(self, value):
        #print('your answer is', value)
        if value["q11"] != 0 or value["q12"] != 1 or value["q21"] != 70 or value["q22"] != 0 or value["q31"] != 0 or value["q32"] != 0:
            self.player.errors += 1
            return 'At least one of your answers is not correct, please try again!'




    #def after_all_players_arrive(self):
    #    self.group.m1 = 1
    #    self.group.m2 = 9
    #def after_all_players_arrive(self):


    #    group = self.group
     #   players = group.get_players()
    #    choice = [p.choice for p in players]
    #    group.choicesum = sum(choice)
        pass


page_sequence = [
    #Startup,
    WorkerID,
    Instructions1,
    Instructions2,
    Instructions3,
    Instructions4,
    #Image1,
    #Image2,
    #Q1,
]
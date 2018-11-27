from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

#
# class RoleInformation(Page):
#
#     def is_displayed(self):
#         return self.player.round_number == 1

class TrialIntro(Page):
    pass

class ReceiverTrial(Page):

    form_model = 'player'
    form_fields = ['trialchoice1']

class ReceiverTrial2(Page):

    form_model = 'player'
    form_fields = ['trialchoice2']

class ReceiverResults(Page):

    # def is_displayed(self):
    #     if self.player.participant.vars['type'] == 1:
    #         if self.player.round_number == 3:
    #             return True
    #         else:
    #             return False
    #     else:
    #         return False

    def vars_for_template(self):
        if self.player.trialchoice1 == 0:
            x = 'A'
        else:
            x = 'B'
        if self.player.trialchoice2 == 0:
            y = 'A'
        else:
            y = 'B'
        return {
            'choice1': x,
            'choice2': y,
        }

class SenderTrial(Page):

    form_model = 'player'
    form_fields = ['trialmessage1']

class SenderTrial2(Page):

    form_model = 'player'
    form_fields = ['trialmessage2']

class SenderResults(Page):

    # def is_displayed(self):
    #     if self.player.participant.vars['type'] != 1:
    #         if self.player.round_number == 3:
    #             return True
    #         else:
    #             return False
    #     else:
    #         return False

    def vars_for_template(self):
        return {
            'message1': self.player.trialmessage1,
            'message2': self.player.trialmessage2,
        }

    # def is_displayed(self):
    #     return self.player.round_number == 3

#
# class ResultsWaitPage(WaitPage):
#
#     def after_all_players_arrive(self):
#         pass
#
#
# class Results(Page):
#     pass


page_sequence = [
    TrialIntro,
    SenderTrial,
    SenderTrial2,
    SenderResults,
    ReceiverTrial,
    ReceiverTrial2,
    ReceiverResults,
]

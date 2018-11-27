from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

import random

class Startup(WaitPage):

    def after_all_players_arrive(self):
        sender1 = self.group.get_player_by_role(1)
        sender2 = self.group.get_player_by_role(2)
        #adjust round numbers for signal
        sender1.signal = sender1.participant.vars['signal1']
        sender2.signal = sender2.participant.vars['signal1']
        self.group.outcomevar = random.randrange(0, 10, 1)
        print(self.group.outcomevar)

class Infopage(Page):

    pass
class Sending(Page):

    timeout_seconds = 30
    form_model = 'player'
    form_fields = ['message']

    def is_displayed(self):
        if self.player.participant.vars['type'] == 0:
            return True
        else:
            return False

    def before_next_page(self):
        if self.timeout_happened:
            self.player.message = random.randrange(1, 9, 2)
            self.player.timeout = True

class Receiving(Page):

    timeout_seconds = 30
    def is_displayed(self):
        if self.player.participant.vars['type'] == 1:
            return True
        else:
            return False
    form_model = 'player'
    form_fields = ['choice']

    def before_next_page(self):
        if self.timeout_happened:
            self.player.choice = random.randrange(0, 1, 1)
            self.player.timeout = True

class ResultsWaitPage(WaitPage):

    title_text = "Wait Page"
    body_text = "Please wait for the senders to make their decisions"

    #def after_all_players_arrive(self):
    #    self.group.m1 = 1
    #    self.group.m2 = 9
    #def after_all_players_arrive(self):


    #    group = self.group
     #   players = group.get_players()
    #    choice = [p.choice for p in players]
    #    group.choicesum = sum(choice)


class ResultsWaitPage2(WaitPage):

    def after_all_players_arrive(self):
        players = self.group.get_players()
        sender1 = self.group.get_player_by_id(1)
        sender2 = self.group.get_player_by_id(2)
        receiver = self.group.get_player_by_id(3)

        if receiver.choice == 0:
            sender1.winner = 1
            sender2.winner = 0
            if sender1.signal > self.group.outcomevar:
                receiver.winner = 1
            else:
                receiver.winner = 0
        else:
            sender1.winner = 0
            sender2.winner = 1
            if sender2.signal > self.group.outcomevar:
                receiver.winner = 1
            else:
                receiver.winner = 0

        #Save values for participants
        sender1.participant.vars['signal1'] = sender1.signal
        sender2.participant.vars['signal1'] = sender2.signal

        sender1.participant.vars['message1'] = sender1.message
        sender2.participant.vars['message1'] = sender2.message

        sender1.participant.vars['othermessage1'] = sender2.message
        sender2.participant.vars['othermessage1'] = sender1.message

        sender1.participant.vars['receiversuccess1'] = receiver.winner
        sender2.participant.vars['receiversuccess1'] = receiver.winner

        sender1.participant.vars['winner1'] = sender1.winner
        sender2.participant.vars['winner1'] = sender2.winner

        receiver.participant.vars['choice1'] = receiver.choice
        receiver.participant.vars['winner1'] = receiver.winner

        receiver.participant.vars['messageA1'] = sender1.message
        receiver.participant.vars['messageB1'] = sender2.message

        receiver.participant.vars['signalA1'] = sender1.signal
        receiver.participant.vars['signalB1'] = sender2.signal

        for p in players:
            p.participant.vars['timeout1'] = p.timeout

        #
        # if receiver.choice == 0:
        #     receiver.participant.vars['choicem1'] = 'A'
        # else:
        #     receiver.participant.vars['choicem1'] = 'B'
        # if receiver.winner == 0:
        #     receiver.participant.vars['winnnerm1'] = 'You haven\'t won!'
        # else:
        #     receiver.participant.vars['winnnerm1'] = 'You have won!'

    #def after_all_players_arrive(self):
    #    self.group.m1 = 1
    #    self.group.m2 = 9
    #def after_all_players_arrive(self):


    #    group = self.group
     #   players = group.get_players()
    #    choice = [p.choice for p in players]
    #    group.choicesum = sum(choice)
        pass

# class SenderResults(Page):
#     def is_displayed(self):
#         if self.player.participant.vars['type'] == 0 and self.player.round_number == 1:
#             return True
#         else:
#             return False
#
#     def vars_for_template(self):
#         receiver = self.group.get_player_by_id(3)
#         # sender1 = self.group.get_player_by_role('sender1')
#         # sender2 = self.group.get_player_by_role('sender2')
#         if self.player.id_in_group == 1:
#             othersender = self.group.get_player_by_id(2)
#             return {
#                 'ownsignal1': self.player.in_round(1).signal,
#                 'ownmessage1': self.player.in_round(1).get_message_display,
#                 #'ownmessage2': self.player.in_round(2).get_message_display,
#                 #'ownmessage3': self.player.in_round(3).get_message_display,
#                 'othermessage1': othersender.in_round(1).get_message_display,
#                 #'othermessage1': othersender.in_round(2).get_message_display,
#                 #'othermessage1': othersender.in_round(3).get_message_display,
#                 'winner1': self.player.in_round(1).sendermessage,
#                 #'winner2': self.player.in_round(2).sendermessage,
#                 #'winner3': self.player.in_round(3).sendermessage,
#                 'receiversuccess1': receiver.senderreceiverwinmessage
#                     }
#         if self.player.id_in_group == 2:
#             othersender = self.group.get_player_by_id(1)
#             return {
#                 'ownsignal1': self.player.in_round(1).signal,
#                 'ownmessage1': self.player.in_round(1).get_message_display,
#                 #'ownmessage2': self.player.in_round(2).get_message_display,
#                 #'ownmessage3': self.player.in_round(3).get_message_display,
#                 'othermessage1': othersender.in_round(1).get_message_display,
#                 #'othermessage1': othersender.in_round(2).get_message_display,
#                 #'othermessage1': othersender.in_round(3).get_message_display,
#                 'winner1': self.player.in_round(1).sendermessage,
#                 #'winner2': self.player.in_round(2).sendermessage,
#                 #'winner3': self.player.in_round(3).sendermessage,
#                 'receiversuccess1': receiver.senderreceiverwinmessage
#                 }



# class ReceiverResults(Page):
#     def is_displayed(self):
#         if self.player.participant.vars['type'] == 1 and self.player.round_number == 1:
#             return True
#         else:
#             return False
#
#     def vars_for_template(self):
#         sendera = self.group.get_player_by_id(1)
#         senderb = self.group.get_player_by_id(2)
#         return {
#             'messageA1': sendera.in_round(1).get_message_display,
#             'messageB1': senderb.in_round(1).get_message_display,
#             #'messageA2': sendera.in_round(2).get_message_display,
#             #'messageB2': sendera.in_round(2).get_message_display,
#             #'messageA3': sendera.in_round(3).get_message_display,
#             #'messageB3': sendera.in_round(3).get_message_display,
#             'choice1': self.player.in_round(1).choiceletter,
#             #'choice1': self.player.in_round(2).choiceletter,
#             #'choice1': self.player.in_round(3).choiceletter,
#             'winner1': self.player.in_round(1).receivermessage,
#             #'winner2': self.player.in_round(2).receivermessage,
#             #'winner3': self.player.in_round(3).receivermessage,
#         }

class TreatmentInfoRR(Page):
    def is_displayed(self):
        if self.player.participant.vars['treatment'] == 0 and self.player.round_number == 1:
            return True
        else:
            return False
        #     if self.player.round_number == 1:
        #         return True
        #     else:
        #         return False
        # else:
        #     return False

class TreatmentInfoTT(Page):
    def is_displayed(self):
        if self.player.participant.vars['treatment'] == 1 and self.player.round_number == 1:
            return True
        else:
            return False

page_sequence = [

    Startup,
    #Infopage,
    #TreatmentInfoRR,
    #TreatmentInfoTT,
    Sending,
    ResultsWaitPage,
    Receiving,
    ResultsWaitPage2,
    #SenderResults,
    #ReceiverResults
]
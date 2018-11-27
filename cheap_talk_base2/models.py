from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import random

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'cheap_talk_base2'
    players_per_group = 3
    num_rounds = 1


class Subsession(BaseSubsession):
    # def creating_session(self):
    #     for p in self.get_players():
    #         if p.participant.vars['treatment'] == 1:
    #             p.treatmentstring = 'rr'
    #         else:
    #             p.treatmentstring = 'tt'


    pass

    # def creating_session(self):
    #     players = self.get_players()
    #     rr_players = [p for p in players if p.participant.vars['treatment'] == 'rr']
    #     tt_players = [p for p in players if p.participant.vars['treatment'] == 'tt']
    #     group_matrix = []
    #         # pop elements from M_players until it's empty
    #     while rr_players:
    #         rr_group = [
    #             rr_players.pop(),
    #             rr_players.pop(),
    #             rr_players.pop()
    #         ]
    #         group_matrix.append(rr_group)
    #
    #     while tt_players:
    #         tt_group = [
    #             tt_players.pop(),
    #             tt_players.pop(),
    #             tt_players.pop()
    #         ]
    #         group_matrix.append(tt_group)
    #
    #     self.set_group_matrix(group_matrix)
    #     #Works only with at least 6 participants
    # def creating_session(self):
    #     if self.round_number == 1:
    #         for p in self.get_players():
    #             if p.id_in_group == 1:
    #                 p.participant.vars['role'] = 'sender1'
    #             if p.id_in_group == 2:
    #                 p.participant.vars['role'] = 'sender2'
    #             if p.id_in_group == 3:
    #                 p.participant.vars['role'] = 'receiver'

class Group(BaseGroup):

    outcomevar = models.IntegerField()

    def message1(self):
        sender = self.get_player_by_id(1)
        return sender.message

    def message2(self):
        sender = self.get_player_by_id(2)
        return sender.message

    def winner(self):
        receiver = self.get_player_by_id(3)
        return receiver.choice

class Player(BasePlayer):
    #Randomization Variables:

    def treatment(self):
        return self.participant.vars['treatment']

    def type(self):
        return self.participant.vars['type']

    def role(self):
        return self.id_in_group


        # if self.participant.vars['role'] == 'sender1':
        #     return 'sender1'
        # if self.participant.vars['role'] == 'sender1':
        #     return 'sender2'
        # if self.participant.vars['role'] == 'sender1':
        #     return 'receiver'


    message = models.IntegerField(
        choices=[
            [1, '1'],
            [3, '3'],
            [5, '5'],
            [7, '7'],
            [9, '9'],
        ],
        widget=widgets.RadioSelectHorizontal
    )
    choice = models.IntegerField(
        choices=[
            [0, 'A'],
            [1, 'B'],
        ],
        widget=widgets.RadioSelectHorizontal
    )

    winner = models.IntegerField()
    signal = models.IntegerField()
    timeout = models.BooleanField(initial=False)


    def sendermessage(self):
        if self.winner == 1:
            return 'You have been chosen!'
        else:
            return 'You have not been chosen!'

    def receivermessage(self):
        if self.winner == 1:
            return 'You have won!'
        else:
            return 'You have lost!'

    def senderreceiverwinmessage(self):
        if self.winner == 1:
            return 'Receiver has won!'
        else:
            return 'Receiver has lost!'

    def choiceletter(self):
        if self.choice == 0:
            return 'A'
        else:
            return 'B'

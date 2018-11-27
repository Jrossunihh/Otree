from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import itertools
author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'randomizationtest'
    players_per_group = None
    num_rounds = 3


class Subsession(BaseSubsession):

    # def do_my_shuffle(self):
    #     # note: to use this function
    #     # you would need to call self.subsession.make_groups()
    #     # from somewhere, such as after_all_players_arrive
    #     players = self.get_players()
    #     playerslist = [p for p in players]
    #     group_matrix = []
    #
    #         # pop elements from M_players until it's empty
    #     while playerslist:
    #         new_group = [
    #             playerslist.pop(3),
    #             playerslist.pop(2),
    #             playerslist.pop(1),
    #             playerslist.pop(0),
    #         ]
    #         group_matrix.append(new_group)
    #
    #     self.set_group_matrix(group_matrix)




    def do_my_shuffle(self, waiting_players):
        print('in get_players_for_group')
        playerslist = [p for p in waiting_players]
        print(playerslist)
        if len(waiting_players) >= 2:
            print('in get_players_for_group')
            group_matrix = []
            red_group = [
                playerslist.pop(1),
                playerslist.pop(0)]

            group_matrix.append(red_group)

            self.set_group_matrix(group_matrix)

        print('not enough players to create a group')



    # def creating_session(self):
    #     bla = itertools.cycle([0, 1])
    #     for p in self.get_players():
    #         p.type = next(bla)

        # players = self.get_players()
        # zero_players = [p for p in players if p.type == 0]
        # one_players = [p for p in players if p.type == 1]
        # group_matrix = []
        # #         # pop elements from M_players until it's empty
        # while zero_players:
        #             new_group = [
        #                 zero_players.pop(),
        #                 one_players.pop(),
        #             ]
        #             group_matrix.append(new_group)
        # self.set_group_matrix(group_matrix)
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
    pass


class Player(BasePlayer):
    type = models.IntegerField()

from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range,
)

import itertools, random



author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'grouping_test'
    players_per_group = None
    num_rounds = 3


class Subsession(BaseSubsession):

    def creating_session(self):
        #treatment tt rr
        treatment = itertools.cycle([0, 1, 2, 3])
        #type = itertools.cycle([0, 0, 1])
        for p in self.get_players():
            p.participant.vars['id'] = next(treatment)
        #generate randomization tables:
        # msr1 = [1, 2, 4, 5, 7, 8]
        # mrr1 = [3, 6, 9]
        # random.shuffle(msr1)
        # random.shuffle(mrr1)
        # self.session.vars['groupmatrixr1'] = [[msr1.pop(), msr1.pop(), mrr1.pop()],
        #                                       [msr1.pop(), msr1.pop(), mrr1.pop()],
        #                                       [msr1.pop(), msr1.pop(), mrr1.pop()]]
        # print(self.session.vars['groupmatrixr1'])


    def do_my_shuffle(self):
        print('setting group matrix')
        players = self.group.get_players
        print('got players')
        bla = self.get_group_matrix()
        print(bla)
        matrix = [[3, 2, 1],
                  [6, 5, 4]]
        print(matrix)
        self.set_group_matrix(matrix)

    #     matrix = self.session.vars['groupmatrixr1']
    #     self.set_group_matrix(matrix)
        # note: to use this function
        # you would need to call self.subsession.make_groups()
        # from somewhere, such as after_all_players_arrive
        # players = self.get_players()
        # print('enough players arrived')
        # sender_players = [p for p in players if p.participant.vars['type'] == 0]
        # receiver_players = [p for p in players if p.participant.vars['type'] == 1]
        # print('List:', sender_players)
        # random.shuffle(sender_players)
        # random.shuffle(receiver_players)
        # print('List(shuffeled):', sender_players)
        # group1 = [[sender_players.pop(), sender_players.pop(), receiver_players.pop()]]
        # print('create 1 group of 3')
        # # Predetermine Groupings here. careful with roles!
        # self.group_matrix.append(group1)
        # print('created group matrix')
        # self.set_group_matrix(group_matrix)

        # if len(players) >= 9:
        #     print('enough players arrived')
        #     sender_players = [p for p in players if p.participant.vars['type'] == 0]
        #     receiver_players = [p for p in players if p.participant.vars['type'] == 1]
        #     print('List:', sender_players)
        #     random.shuffle(sender_players)
        #     random.shuffle(receiver_players)
        #     print('List(shuffeled):', sender_players)
        #     group_matrix = [
        #                     [sender_players.pop(), sender_players.pop(), receiver_players.pop()],
        #                     [sender_players.pop(), sender_players.pop(), receiver_players.pop()],
        #                     [sender_players.pop(), sender_players.pop(), receiver_players.pop()],
        #                     ]
        #     print('created groups')
        #     #Predetermine Groupings here. careful with roles!
        #     self.set_group_matrix(group_matrix)
        #     print('created group matrix')
        #     pass

        # if round(2):
        #     group_matrix = [[players[2], players[1]],
        #                     [players[4], players[3]]]
        #     self.set_group_matrix(group_matrix)
        # if round(3):
        #     group_matrix = [[players[1], players[2]],
        #                     [players[3], players[4]]]
        #     self.set_group_matrix(group_matrix)
        # a_players = [p for p in waiting_players]
        # if len(waiting_players) >= 2:
        #     print('creating group')
        #
        #     # red_group = [
        #     #     1,
        #     #     2]
        #     return [a_players[0], a_players[1]]
        # print('not enough players to create a group')
        # group_matrix = [[1, 4],
        #                 [3, 2]]
            # pop elements from M_players until it's empty
        #new_group = [1, 2]
        # g1 = [Players.pop(3), Players.pop(0), ]
        # group_matrix.append(g1)
        # g2 = [Players.pop(0), Players.pop(0), ]
        # group_matrix.append(g2)
        #self.set_group_matrix(group_matrix)
        #print(group_matrix)


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    subgroupid = models.IntegerField()
    pass

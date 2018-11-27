from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from otree_mturk_utils.pages import CustomMturkPage, CustomMturkWaitPage
import itertools, random

class Grouping1(WaitPage):
    title_text = "Custom title text"
    #Adjust group size for waitpage!
    # template_name = 'grouping_test/Grouping_Waitpage.html'
    # def vars_for_template(self):
    #     return {'waitingplayers': waiting_players}
    group_by_arrival_time = True

    def get_players_for_group(self, waiting_players):
        # sender_players = [p for p in waiting_players if p.participant.vars['type'] == 0]
        # receiver_players = [p for p in waiting_players if p.participant.vars['type'] == 1]
        # if len(sender_players) >= 2 and len(receiver_players) >= 2:
        #     print('creating group')
        #     return [1, 2], [3, 4]
        #
        # print('not enough players to create a group')
        sender_players = [p for p in waiting_players if p.participant.vars['type'] == 0]
        receiver_players = [p for p in waiting_players if p.participant.vars['type'] == 1]

        if len(sender_players) >= 4 and len(receiver_players) >= 2:
            print('shuffeling senders/receivers')
            random.shuffle(sender_players)
            random.shuffle(receiver_players)
            print('creating group of 3')
            # return [sender_players[0], sender_players[1], receiver_players[0], sender_players[2], sender_players[3],
            #         receiver_players[1], sender_players[4], sender_players[5], receiver_players[2]]

            groupmatrix = [sender_players[0], sender_players[1], receiver_players[0],
                           ]
            print(groupmatrix)

            return groupmatrix


        print('not enough players to create a group')
            #
            # print('creating group')
            # matrix = []
            # group1 = [sender_players[0], sender_players[2], ]
            # group2 = [sender_players[1], sender_players[3], ]
            # group3 = [sender_players[0], sender_players[2], sender_players[1], sender_players[3], ]
            # matrix.append(group1)
            # matrix.append(group2)
            # # group3 = [sender_players[0], sender_players[2]]
            # return group3



        # sender_players = [p for p in waiting_players if p.participant.vars['type'] == 0]
        # receiver_players = [p for p in waiting_players if p.participant.vars['type'] == 1]
        # if len(sender_players) >= 2 and len(receiver_players) >= 2:
        #     print('creating group')
        #     return [1, 2], [3, 4]
        #
        # print('not enough players to create a group')
    #     sender_players = [p for p in waiting_players]
    #     if len(sender_players) >= 4:
    #         matrix = []
    #         group1 = [sender_players[0], sender_players[2], ]
    #         group2 = [sender_players[1], sender_players[3], ]
    #         group3 = [sender_players[0], sender_players[2], sender_players[1], sender_players[3], ]
    #         matrix.append(group1)
    #         matrix.append(group2)
    #         return
    #
    # def get_players_for_group2(self, waiting_players):

        # matrix = []
        # group1 = [sender_players[0], sender_players[1], ]
        # group2 = [sender_players[0], sender_players[1], ]
        # group3 = [sender_players[0], sender_players[2], sender_players[1], sender_players[3], ]
        # matrix.append(group1)
        # matrix.append(group2)


            # group3 = [sender_players[0], sender_players[2]]
            #return matrix


        #print('not enough players to create a group')
        #Working old version
        # print('All players arrived, shuffeling')
        # a_players = [p for p in waiting_players]
        # if len(waiting_players) >= 2:
        #     print('creating group')
        #
        #     # red_group = [
        #     #     1,
        #     #     2]
        #     return [a_players[0], a_players[1]]
        # print('not enough players to create a group')

class Grouping2(WaitPage):

    def after_all_players_arrive(self):
        players = self.group.get_players()
        for p in players:
            if p.id_in_group == 6:
                self.subsession.do_my_shuffle(self)
            pass



class GroupInfo(Page):

    def vars_for_template(self):
        subgroupx = self.player.subgroupid
        othersingroup1 = self.player.get_others_in_group()[0]
        othersingroup2 = self.player.get_others_in_group()[1]
        own = self.player.participant.vars['firstid']
        other1 = othersingroup1.participant.vars['firstid']
        other2 = othersingroup2.participant.vars['firstid']
        return {
            'subgroup': subgroupx,
            'ownid': own,
            'other1': other1,
            'other2': other2,
        }
    pass

class ResultsWaitPage(WaitPage):

   pass

class Results(Page):
    pass


page_sequence = [
    Grouping1,
    Grouping2,
    GroupInfo,
]

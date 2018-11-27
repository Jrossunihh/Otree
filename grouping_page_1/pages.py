from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from otree_mturk_utils.pages import CustomMturkPage, CustomMturkWaitPage
import itertools, random

class Grouping1(CustomMturkWaitPage):
    title_text = "Forming Groups"
    startwp_timer = 10
    #Adjust group size for waitpage!
    # template_name = 'grouping_test/Grouping_Waitpage.html'
    # def vars_for_template(self):
    #     return {'waitingplayers': waiting_players}
    group_by_arrival_time = True
    skip_until_the_end_of = 'app'
    #skip_until_the_end_of = 'app'
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

        if len(sender_players) >= 2 and len(receiver_players) >= 1:
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

class skippinfo(Page):

    def vars_for_template(self):
        skipped = self.player.participant.vars.get('skip_the_end_of_app_collecting_page_1', False)
        self.player.skip = skipped
        return {
            'skipped': skipped,
        }
    pass

class GroupInfo(Page):

    def vars_for_template(self):

        othersingroup1 = self.player.get_others_in_group()[0]
        othersingroup2 = self.player.get_others_in_group()[1]
        own = self.player.participant.vars['firstid']
        other1 = othersingroup1.participant.vars['firstid']
        other2 = othersingroup2.participant.vars['firstid']
        return {
            'ownid': own,
            'other1': other1,
            'other2': other2,
        }
    pass


page_sequence = [
    Grouping1,
]

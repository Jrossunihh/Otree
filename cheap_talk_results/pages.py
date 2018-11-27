from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class SenderResults(Page):


    def is_displayed(self):
        if self.player.participant.vars['type'] == 0:
            return True
        else:
            return False

    def vars_for_template(self):
        skippeda = {}
        skippedb = {}
        winninground = self.session.vars['paying_round']
        ownsignalprint = {}
        roundnumber = {}
        ownmessageprint = {}
        othermessageprint = {}
        winnerprint = {}
        receivermessageprint = {}
        for p in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
            roundnumber['{}'.format(p)] = p
            skippeda['{}'.format(p)] = self.participant.vars.get('skip_the_end_of_app_collecting_page_{}'.format(p),
                                                                 False)
            skippedb['{}'.format(p)] = self.participant.vars.get('skip_the_end_of_app_grouping_page_{}'.format(p),
                                                                 False)
        #     ownsignalprint['{}'.format(p)] = self.participant.vars.get('signal{}'.format(p), 'miss')
        # return {
        #     'ownsignal1': ownsignalprint['1'],
        #     'ownsignal2': ownsignalprint['2'],
        #     'ownsignal3': ownsignalprint['3'],
        #     'ownmessage1': 'a',
        #     'othermessage1': 'b',
        #     'winner1': 'c',
        #     'receiversuccess1': 'd',
        #
                #'ownsignal2': ownsignalprint(2),
                # 'winner2': self.player.in_round(2).sendermessage,
                # 'winner3': self.player.in_round(3).sendermessage,
                # 'othermessage1': othersender.in_round(2).get_message_display,
                # 'othermessage1': othersender.in_round(3).get_message_display,
                # 'ownmessage2': self.player.in_round(2).get_message_display,
                # 'ownmessage3': self.player.in_round(3).get_message_display,
            #}
            if self.participant.vars.get('skip_the_end_of_app_grouping_page_{}'.format(p), False):
                ownsignalprint['{}'.format(p)] = 'skipped'
                ownmessageprint['{}'.format(p)] = 'skipped'
                othermessageprint['{}'.format(p)] = 'skipped'
                winnerprint['{}'.format(p)] = 'skipped'
                receivermessageprint['{}'.format(p)] = 'skipped'
            else:
                if self.participant.vars.get('timeout{}'.format(p), False) == False:
                    ownsignalprint['{}'.format(p)] = self.participant.vars.get('signal{}'.format(p), 'miss')
                    ownmessageprint['{}'.format(p)] = self.participant.vars.get('message{}'.format(p), 'miss')
                    othermessageprint['{}'.format(p)] = self.participant.vars.get('othermessage{}'.format(p), 'miss')
                    if self.participant.vars.get('winner{}'.format(p), 2) != 2:
                        if self.participant.vars.get('winner{}'.format(p), 2) == 1:
                            winnerprint['{}'.format(p)] = 'You have been chosen!'
                        if self.participant.vars.get('winner{}'.format(p), 2) == 0:
                            winnerprint['{}'.format(p)] = 'You haven\'t been chosen!'
                    else:
                        winnerprint['{}'.format(p)] = 'miss'

                    if self.participant.vars.get('receiversuccess{}'.format(p), 'miss') != 'miss':
                        if self.participant.vars.get('receiversuccess{}'.format(p), 'miss') == 1:
                            receivermessageprint['{}'.format(p)] = 'Win!'
                        if self.participant.vars.get('receiversuccess{}'.format(p), 'miss') == 0:
                            receivermessageprint['{}'.format(p)] = 'Loose!'
                    else:
                        receivermessageprint['{}'.format(p)] = 'miss'


                else:
                    ownsignalprint['{}'.format(p)] = 'timeout'
                    ownmessageprint['{}'.format(p)] = 'timeout'
                    othermessageprint['{}'.format(p)] = 'timeout'
                    winnerprint['{}'.format(p)] = 'timeout'
                    receivermessageprint['{}'.format(p)] = 'timeout'
                # receiver = self.group.get_player_by_id(3)
                # sender1 = self.group.get_player_by_role('sender1')
                # sender2 = self.group.get_player_by_role('sender2')

        skipnumber = sum(skippedb.values())
        payoff = self.player.payoff + skipnumber * 0.1
        return {
            'round1': roundnumber['1'],
            'round2': roundnumber['2'],
            'round3': roundnumber['3'],
            'round4': roundnumber['4'],
            'round5': roundnumber['5'],
            'round6': roundnumber['6'],
            'round7': roundnumber['7'],
            'round8': roundnumber['8'],
            'round9': roundnumber['9'],
            'round10': roundnumber['10'],

            'ownsignal1': ownsignalprint['1'],
            'ownsignal2': ownsignalprint['2'],
            'ownsignal3': ownsignalprint['3'],
            'ownsignal4': ownsignalprint['4'],
            'ownsignal5': ownsignalprint['5'],
            'ownsignal6': ownsignalprint['6'],
            'ownsignal7': ownsignalprint['7'],
            'ownsignal8': ownsignalprint['8'],
            'ownsignal9': ownsignalprint['9'],
            'ownsignal10': ownsignalprint['10'],

            'ownmessage1': ownmessageprint['1'],
            'ownmessage2': ownmessageprint['2'],
            'ownmessage3': ownmessageprint['3'],
            'ownmessage4': ownmessageprint['4'],
            'ownmessage5': ownmessageprint['5'],
            'ownmessage6': ownmessageprint['6'],
            'ownmessage7': ownmessageprint['7'],
            'ownmessage8': ownmessageprint['8'],
            'ownmessage9': ownmessageprint['9'],
            'ownmessage10': ownmessageprint['10'],

            'othermessage1': othermessageprint['1'],
            'othermessage2': othermessageprint['2'],
            'othermessage3': othermessageprint['3'],
            'othermessage4': othermessageprint['4'],
            'othermessage5': othermessageprint['5'],
            'othermessage6': othermessageprint['6'],
            'othermessage7': othermessageprint['7'],
            'othermessage8': othermessageprint['8'],
            'othermessage9': othermessageprint['9'],
            'othermessage10': othermessageprint['10'],

            'winner1': winnerprint['1'],
            'winner2': winnerprint['2'],
            'winner3': winnerprint['3'],
            'winner4': winnerprint['4'],
            'winner5': winnerprint['5'],
            'winner6': winnerprint['6'],
            'winner7': winnerprint['7'],
            'winner8': winnerprint['8'],
            'winner9': winnerprint['9'],
            'winner10': winnerprint['10'],

            'receiversuccess1': receivermessageprint['1'],
            'receiversuccess2': receivermessageprint['2'],
            'receiversuccess3': receivermessageprint['3'],
            'receiversuccess4': receivermessageprint['4'],
            'receiversuccess5': receivermessageprint['5'],
            'receiversuccess6': receivermessageprint['6'],
            'receiversuccess7': receivermessageprint['7'],
            'receiversuccess8': receivermessageprint['8'],
            'receiversuccess9': receivermessageprint['9'],
            'receiversuccess10': receivermessageprint['10'],

            'winninground': winninground,
            'payoff': payoff,
            'skipnumber': skipnumber
            }


class ReceiverResults(Page):
    def is_displayed(self):
        if self.player.participant.vars['type'] == 1:
            return True
        else:
            return False



    def vars_for_template(self):
        winninground = self.session.vars['paying_round']
        skippeda = {}
        skippedb = {}
        messageaprint = {}
        messagebprint = {}
        choiceprint = {}
        winnerprint = {}
        roundnumber = {}
        for p in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
            roundnumber['{}'.format(p)] = p
            skippeda['{}'.format(p)] = self.participant.vars.get('skip_the_end_of_app_collecting_page_{}'.format(p),
                                                                 False)
            skippedb['{}'.format(p)] = self.participant.vars.get('skip_the_end_of_app_grouping_page_{}'.format(p),
                                                                 False)
            if self.participant.vars.get('skip_the_end_of_app_grouping_page_{}'.format(p), False):
                messageaprint['{}'.format(p)] = 'skipped'
                messagebprint['{}'.format(p)] = 'skipped'
                choiceprint['{}'.format(p)] = 'skipped'
                winnerprint['{}'.format(p)] = 'skipped'
            else:
                if self.participant.vars.get('timeout{}'.format(p), False) == False:
                    messageaprint['{}'.format(p)] = self.participant.vars.get('messageA{}'.format(p), 'miss')
                    messagebprint['{}'.format(p)] = self.participant.vars.get('messageB{}'.format(p), 'miss')
                    if self.participant.vars.get('choice{}'.format(p), 'miss') != 'miss':
                        if self.participant.vars.get('choice{}'.format(p), 'miss') == 0:
                            choiceprint['{}'.format(p)] = 'A'
                        if self.participant.vars.get('choice{}'.format(p), 'miss') == 1:
                            choiceprint['{}'.format(p)] = 'B'
                    else:
                        choiceprint['{}'.format(p)] = 'miss'
                    if self.participant.vars.get('winner{}'.format(p), 'miss') != 'miss':
                        if self.participant.vars.get('winner{}'.format(p), 'miss') == 1:
                            winnerprint['{}'.format(p)] = 'You have won!'
                        if self.participant.vars.get('winner{}'.format(p), 'miss') == 0:
                            winnerprint['{}'.format(p)] = 'You haven\'t won!'
                    else:
                        winnerprint['{}'.format(p)] = 'miss'
                else:
                    messageaprint['{}'.format(p)] = 'timeout'
                    messagebprint['{}'.format(p)] = 'timeout'
                    choiceprint['{}'.format(p)] = 'timeout'
                    winnerprint['{}'.format(p)] = 'timeout'
        skipnumber = sum(skippedb.values())
        payoff = self.player.payoff + skipnumber * 0.1
        return {
            'round1': roundnumber['1'],
            'round2': roundnumber['2'],
            'round3': roundnumber['3'],
            'round4': roundnumber['4'],
            'round5': roundnumber['5'],
            'round6': roundnumber['6'],
            'round7': roundnumber['7'],
            'round8': roundnumber['8'],
            'round9': roundnumber['9'],
            'round10': roundnumber['10'],

            'messageA1': messageaprint['1'],
            'messageA2': messageaprint['2'],
            'messageA3': messageaprint['3'],
            'messageA4': messageaprint['4'],
            'messageA5': messageaprint['5'],
            'messageA6': messageaprint['6'],
            'messageA7': messageaprint['7'],
            'messageA8': messageaprint['8'],
            'messageA9': messageaprint['9'],
            'messageA10': messageaprint['10'],

            'messageB1': messagebprint['1'],
            'messageB2': messagebprint['2'],
            'messageB3': messagebprint['3'],
            'messageB4': messagebprint['4'],
            'messageB5': messagebprint['5'],
            'messageB6': messagebprint['6'],
            'messageB7': messagebprint['7'],
            'messageB8': messagebprint['8'],
            'messageB9': messagebprint['9'],
            'messageB10': messagebprint['10'],

            'choice1': choiceprint['1'],
            'choice2': choiceprint['2'],
            'choice3': choiceprint['3'],
            'choice4': choiceprint['4'],
            'choice5': choiceprint['5'],
            'choice6': choiceprint['6'],
            'choice7': choiceprint['7'],
            'choice8': choiceprint['8'],
            'choice9': choiceprint['9'],
            'choice10': choiceprint['10'],

            'winner1': winnerprint['1'],
            'winner2': winnerprint['2'],
            'winner3': winnerprint['3'],
            'winner4': winnerprint['4'],
            'winner5': winnerprint['5'],
            'winner6': winnerprint['6'],
            'winner7': winnerprint['7'],
            'winner8': winnerprint['8'],
            'winner9': winnerprint['9'],
            'winner10': winnerprint['10'],

            'winninground': winninground,
            'payoff': payoff,
            'skipnumber': skipnumber
        }


page_sequence = [
    SenderResults,
    ReceiverResults
]

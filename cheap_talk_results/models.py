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
    name_in_url = 'cheap_talk_results'
    players_per_group = None
    num_rounds = 1



class Subsession(BaseSubsession):
    def creating_session(self):
        paying_round = random.randint(1, 10)
        self.session.vars['paying_round'] = paying_round
        print('set the paying round to', paying_round)


class Group(BaseGroup):

    def set_payoffs(self):
        players = self.get_players()
        round = self.session.vars['paying_round']
        for p in players:
            if p.participant.vars['winner{}'.format(round), 0] == 1:
                p.payoff = 3
            else:
                p.payoff = 0



class Player(BasePlayer):
    pass

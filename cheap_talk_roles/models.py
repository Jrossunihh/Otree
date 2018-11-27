from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'cheap_talk_roles'
    players_per_group = 3
    num_rounds = 1

class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            for p in self.get_players():
                if p.id_in_group == 1:
                    p.participant.vars['role'] = 'sender1'
                if p.id_in_group == 2:
                    p.participant.vars['role'] = 'sender2'
                if p.id_in_group == 3:
                    p.participant.vars['role'] = 'receiver'


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # def constantrole(self):
    #     return self.participant.vars['role']
    # def bla(self):
    #     if self.id_in_group == 1:
    #         return 'sender1'
    #     if self.id_in_group == 2:
    #         return 'sender2'
    #     if self.id_in_group == 3:
    #         return 'receiver'
    pass
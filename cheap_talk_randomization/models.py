from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range,
)
import itertools, random

author = 'Your name here'

doc = """
Your app description
"""
import itertools

class Constants(BaseConstants):
    name_in_url = 'cheap_talk_randomization'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    def creating_session(self):
        #treatment tt rr
        treatment = itertools.cycle([0, 1])
        type = itertools.cycle([0, 0, 1])
        #type = itertools.cycle([0, 1])
        for p in self.get_players():
            p.participant.vars['treatment'] = next(treatment)
        for p in self.get_players():
            if p.participant.vars['treatment'] == 0:
                p.treatment = 'rr'
            else:
                p.treatment = 'tt'

        for p in self.get_players():
            p.participant.vars['type'] = next(type)
        for p in self.get_players():
            if p.participant.vars['type'] == 0:
                p.type = 'sender'
            else:
                p.type = 'receiver'
        for p in self.get_players():
            p.participant.vars['firstid'] = p.id_in_group
        for p in self.get_players():
            #scale up to full roster!
            signal = [1, 3, 5, 7, 9]
            random.shuffle(signal)
            p.participant.vars['signal1'] = signal[0]
            p.participant.vars['signal2'] = signal[1]
            p.participant.vars['signal3'] = signal[2]
            p.participant.vars['signal4'] = signal[3]
            p.participant.vars['signal5'] = signal[4]
            signal2 = [1, 3, 5, 7, 9]
            random.shuffle(signal2)
            p.participant.vars['signal6'] = signal2[0]
            p.participant.vars['signal7'] = signal2[1]
            p.participant.vars['signal8'] = signal2[2]
            p.participant.vars['signal9'] = signal2[3]
            p.participant.vars['signal10'] = signal2[4]




        # if self.round_number == 1:
        #     for p in self.get_players():
        #         if p.id_in_group == 1:
        #             p.participant.vars['type'] = 0
        #         if p.id_in_group == 2:
        #             p.participant.vars['type'] = 0
        #         if p.id_in_group == 3:
        #             p.participant.vars['type'] = 1
        #
        # for p in self.get_players():
        #     if p.participant.vars['role'] == 3:
        #         p.type = 'receiver'
        #     else:
        #         p.type = 'sender'
class Group(BaseGroup):
    pass


class Player(BasePlayer):
    treatment = models.StringField()
    type = models.StringField()

    pass
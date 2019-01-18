from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

author = 'Vadim Selyutin'

doc = """
This is the "11-20 Money Request Game".
"""


class Constants(BaseConstants):
    name_in_url = 'my_11_20_game'
    players_per_group = 2
    num_rounds = 15


class Subsession(BaseSubsession):
    def before_session_starts(self):
        self.group_randomly()


class Group(BaseGroup):
    request_1 = models.CurrencyField(choices=currency_range(11, 20, c(1)))
    request_2 = models.CurrencyField(choices=currency_range(11, 20, c(1)))

    def set_payoffs(self):
        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)

        if self.request_2 - self.request_1 == 1:
            p1.payoff = self.request_1 + 20
            p2.payoff = self.request_2
        else:
            if self.request_1 - self.request_2 == 1:
                p1.payoff = self.request_1
                p2.payoff = self.request_2 + 20
            else:
                p1.payoff = self.request_1
                p2.payoff = self.request_2


class Player(BasePlayer):
    name = models.StringField()
    sex = models.StringField()
    department = models.StringField()
    group_number = models.IntegerField()

from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Players_info(Page):
    form_model = 'player'
    form_fields = ['name', 'sex', 'department', 'group_number']

    def is_displayed(self):
        return self.round_number == 1


class ResultsWaitPage(WaitPage):
    title_text = "Пожалуйста, подождите пока ваш противник примет решение"
    body_text = " "

    def after_all_players_arrive(self):
        self.group.set_payoffs()


class Results(Page):
    def vars_for_template(self):
        # self.group.set_payoffs()
        return {'total_payoff': sum([p.payoff for p in self.player.in_all_rounds()])
        }


class Instructions(Page):
    def is_displayed(self):
        return self.round_number == 1


class Request_1(Page):

    form_model = 'group'
    form_fields = ['request_1']

    def is_displayed(self):
        return self.player.id_in_group == 1


class Request_2(Page):

    form_model = 'group'
    form_fields = ['request_2']

    def is_displayed(self):
        return self.player.id_in_group == 2

class AllGroupsWaitPage(WaitPage):
    wait_for_all_groups = True
    title_text = "Пожалуйста, подождите пока все игроки примут решения"
    body_text = " "


page_sequence = [
    Players_info,
    Instructions,
    Request_1,
    Request_2,
    ResultsWaitPage,
    AllGroupsWaitPage,
    Results
]

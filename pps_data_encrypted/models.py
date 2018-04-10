from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
from django.db import models as djmodels

class Constants(BaseConstants):
    name_in_url = 'pps_data'
    players_per_group = None
    num_rounds = 1

    fields_with_encryption = [
        'first_name', 'last_name', 'account_number',
    ]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    account_number_cleartext = models.StringField()
    account_number_encrypted = djmodels.BinaryField(null=True)

    first_name_cleartext = models.StringField()
    first_name_encrypted = djmodels.BinaryField(null=True)

    last_name_cleartext = models.StringField()
    last_name_encrypted = djmodels.BinaryField(null=True)


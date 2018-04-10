from Cryptodome.Cipher import PKCS1_OAEP
from crypto_pps import get_public_key

from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

public_key = get_public_key()
cipher = PKCS1_OAEP.new(public_key)

class PersonalInfo(Page):

    form_model = 'player'
    form_fields = ['{}_cleartext'.format(f) for f in Constants.fields_with_encryption]

    def before_next_page(self):
        for f in Constants.fields_with_encryption:
            cleartext_value = getattr(self.player, '{}_cleartext'.format(f))
            # before encrypting, need to encode to bytes
            cleartext_value = cleartext_value.encode('utf-8')
            encrypted_value = cipher.encrypt(cleartext_value)
            setattr(self.player, '{}_encrypted'.format(f), encrypted_value)

            # delete the sensitive cleartext data
            setattr(self.player, '{}_cleartext'.format(f), None)


page_sequence = [
    PersonalInfo,
]

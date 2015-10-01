# This file is part party_identifier module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta

__all__ = ['Party']
__metaclass__ = PoolMeta


class Party:
    __name__ = 'party.party'
    identifier_code = fields.Function(fields.Char('Identifier Code'),
        'get_identifier_code', searcher='search_identifier_code')

    def get_identifier_code(self, name):
        if self.identifiers:
            identifier, = self.identifiers
            return identifier.code

    @classmethod
    def search_identifier_code(cls, name, clause):
        return [
            ('identifiers.code',) + tuple(clause[1:]),
            ]

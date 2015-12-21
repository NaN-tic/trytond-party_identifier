# This file is part party_identifier module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import Pool, PoolMeta

__all__ = ['Party']
__metaclass__ = PoolMeta


class Party:
    __name__ = 'party.party'
    identifier_code = fields.Function(fields.Char('Identifier Code'),
        'get_identifier_code', setter='set_identifer_code',
        searcher='search_identifier_code')

    def get_identifier_code(self, name):
        if self.identifiers:
            identifiers = self.identifiers
            if identifiers:
                return identifiers[0].code

    @classmethod
    def search_identifier_code(cls, name, clause):
        return [
            ('identifiers.code',) + tuple(clause[1:]),
            ]

    @classmethod
    def set_identifer_code(cls, parties, name, value):
        Identifier = Pool().get('party.identifier')
        for party in parties:
            identifier = Identifier.search([
                    ('party', '=', party.id)
                    ])
            if identifier and value:
                Identifier.write([identifier[0]], {'code': value})
            elif identifier and not value:
                Identifier.delete([identifier[0]])
            else:
                Identifier.create([{
                            'party': party,
                            'code': value,
                            }])

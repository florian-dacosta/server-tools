#    Author: Florian da Costa
#    Copyright 2015 Akretion
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distnaributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
from openerp.tests.common import TransactionCase


class TestExportSqlQuery(TransactionCase):

    def test_sql_query(self):
        test = self.sql_model.export_sql_query(
            self.cr, self.uid, [self.query_id])
        print test, "******************"

    def setUp(self):
        super(TestExportSqlQuery, self).setUp()
        print "!!!!!!!!!!!!!!!!!!!!!!!!!!"
        raise
        query_vals = {
            'name': test,
            'query': "SELECT name, street FROM res_partner;"
        }
        self.sql_model = registry('sql.export')
        self.query_id = self.sql_model.create(
            self.cr,
            self.uid,
            query_vals)

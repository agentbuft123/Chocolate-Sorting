import unittest
from proj3_choc import *

# proj3_choc_test.py
# You must NOT change this file. You can comment stuff out while debugging but
# don't forget to restore it to its original form!

class TestDatabase(unittest.TestCase):

    def test_bar_table(self):
        conn = sqlite3.connect(DBNAME)
        cur = conn.cursor()

        sql = 'SELECT Company FROM Bars'
        results = cur.execute(sql)
        result_list = results.fetchall()
        self.assertIn(('Sirene',), result_list)
        self.assertEqual(len(result_list), 1795)

        sql = '''
            SELECT Company, SpecificBeanBarName, CocoaPercent,
                   Rating, BroadBeanOrigin
            FROM Bars
            WHERE Company="Woodblock"
            ORDER BY Rating DESC
        '''
        results = cur.execute(sql)
        result_list = results.fetchall()
        #print(result_list)
        self.assertEqual(len(result_list), 8)
        self.assertEqual(result_list[0][3], 4.0)

        conn.close()

    def test_country_table(self):
        conn = sqlite3.connect(DBNAME)
        cur = conn.cursor()

        sql = '''
            SELECT EnglishName
            FROM Countries
            WHERE Region="Oceania"
        '''
        results = cur.execute(sql)
        result_list = results.fetchall()
        self.assertIn(('Australia',), result_list)
        self.assertEqual(len(result_list), 27)

        sql = '''
            SELECT COUNT(*)
            FROM Countries
        '''
        results = cur.execute(sql)
        count = results.fetchone()[0]
        self.assertEqual(count, 250)

        conn.close()

    def test_joins(self):
        conn = sqlite3.connect(DBNAME)
        cur = conn.cursor()

        sql = '''
            SELECT Alpha2
            FROM Bars
                JOIN Countries
                ON Bars.CompanyLocationId=Countries.Id
            WHERE SpecificBeanBarName="Hacienda Victoria"
                AND Company="Arete"
        '''
        results = cur.execute(sql)
        result_list = results.fetchall()
        self.assertIn(('US',), result_list)
        conn.close()

class TestBarSearch(unittest.TestCase):

    def test_bar_search(self):
        results = process_command('bars ratings top=1')
        self.assertEqual(results[0][0], 'Chuao')

        results = process_command('bars cocoa bottom=10')
        self.assertEqual(results[0][0], 'Guadeloupe')

        results = process_command('bars sellcountry=CA ratings top=5')
        self.assertEqual(results[0][3], 4.0)

        results = process_command('bars sourceregion=Africa ratings top=5')
        self.assertEqual(results[0][3], 4.0)


class TestCompanySearch(unittest.TestCase):

    def test_company_search(self):
        results = process_command('companies region=Europe ratings top=5')
        self.assertEqual(results[1][0], 'Idilio (Felchlin)')

        results = process_command('companies country=US bars_sold top=5')
        self.assertTrue(results[0][0] == 'Fresco' and results[0][2] == 26)

        results = process_command('companies cocoa top=5')
        self.assertEqual(results[0][0], 'Videri')
        self.assertGreater(results[0][2], 0.79)

class TestCountrySearch(unittest.TestCase):

    def test_country_search(self):
        results = process_command('countries sources ratings bottom=5')
        self.assertEqual(results[1][0],'Uganda')

        results = process_command('countries sellers bars_sold top=5')
        self.assertEqual(results[0][2], 764)
        self.assertEqual(results[1][0], 'France')


class TestRegionSearch(unittest.TestCase):

    def test_region_search(self):
        results = process_command('regions sources bars_sold top=5')
        self.assertEqual(results[0][0], 'Americas')
        self.assertEqual(results[3][1], 66)
        self.assertEqual(len(results), 4)

        results = process_command('regions sellers ratings top=10')
        self.assertEqual(len(results), 5)
        self.assertEqual(results[0][0], 'Oceania')
        self.assertGreater(results[3][1], 3.0)

unittest.main()

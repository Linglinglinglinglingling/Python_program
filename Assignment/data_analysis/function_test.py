from card_analyze import Card_analysis
from card import Card
import unittest

class Testforcard_analyze(unittest.TestCase):


    #test function --is_flush
    #valid case
    def test_is_flush_valid(self):
        list_card=[Card(1,'H'),Card(13,'H'),Card(10,'H')]
        self.assertTrue(Card_analysis(4).is_flush(list_card))

    #invalid case
    def test_is_flush_invalid(self):
        list_card=[Card(1,'H'),Card(13,'C'),Card(10,'S')]
        self.assertFalse(Card_analysis(4).is_flush(list_card))

    #boundary case
    def test_is_flush_bond(self):
        list_card=[Card(1,'H'),Card(1,'H'),Card(10,'S')]
        self.assertFalse(Card_analysis(4).is_flush(list_card))


    #test function--contain_pair
    # valid case
    def test_contain_pair_valid(self):
        list_card = [Card(1, 'H'), Card(1, 'S'), Card(1, 'D')]
        self.assertTrue(Card_analysis(4).contain_pair(list_card))

    # invalid case
    def test_contain_pair_invalid(self):
        list_card = [Card(1, 'H'), Card(13, 'C'), Card(10, 'S')]
        self.assertFalse(Card_analysis(4).contain_pair(list_card))

    # boundary case
    def test_contain_pair_bond(self):
        list_card = [Card(1, 'H'), Card(1, 'S'), Card(10, 'S')]
        self.assertTrue(Card_analysis(4).contain_pair(list_card))

    #test function--result_string
    def test_result_string(self):
        result_list=[1,2,3]
        self.assertEqual(Card_analysis(4).result_string(result_list),
                         '(1/1000+2/1000+3/1000)/3=0.2%')

    #test function--average_value
    def test_average_value(self):
        list_occurrence,sum_value=Card_analysis(4).average_value()
        #the length of result list should be 13
        #the sum value need to a integer
        self.assertEqual(len(list_occurrence),13)
        self.assertIsInstance(sum_value,int)


    #test function--flush_pair_chance
    #boundary case
    def test_flush_pair_chance_bond(self):
        #when there is only 1 suit, every time will draw a flush and can't draw a pair
        self.assertEqual(Card_analysis(1).flush_pair_chance(3),([0,0,0],[1000,1000,1000]))

    #valid case
    def test_flush_pair_chance_valid(self):
        #run 5 times, so result list should contain 5 items
        list_pair,list_flush=Card_analysis(4).flush_pair_chance(5)
        self.assertEqual(len(list_pair),5)
        self.assertEqual(len(list_flush),5)


    #test function--change_in_chance
    #boundary case
    def test_change_in_chance_bond(self):
        #the number of suit stays at 1, then every time will draw a flush and can't draw a pair
        self.assertEqual(Card_analysis(1).change_in_chance(1,1),([1000],[0]))

    #valid case
    def test_change_in_chance_valid(self):
        list_flush,list_pair=Card_analysis(1).change_in_chance(1,5)

        #since the number of suit change from 1 to 5, there should be 5 item in result list
        self.assertEqual(len(list_flush),5)
        self.assertEqual(len(list_pair),5)
        #since the number if suit starts from 1, the first item in the list of flush should
        #be 1000, the first item in list of pair should be 1
        self.assertEqual(list_flush[0],1000)
        self.assertEqual(list_pair[0],0)



if __name__ == '__main__':
    unittest.main()

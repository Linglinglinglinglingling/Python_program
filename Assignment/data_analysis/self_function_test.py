from Assignment.data_analysis.card_analyze import Card_analysis
from Assignment.data_analysis.card import Card

def test_is_flush_valid():
    list_card=[Card(1,'H'),Card(13,'H'),Card(10,'H')]
    assert(Card_analysis(4).is_flush(list_card)),str(Card_analysis(4).is_flush(list_card))+' is not True'


    #invalid case
def test_is_flush_invalid():
    list_card=[Card(1,'H'),Card(13,'H'),Card(10,'H')]
    assert(Card_analysis(4).is_flush(list_card)==True),str(Card_analysis(4).is_flush(list_card))+' not equal to '+'False'

if __name__ == '__main__':
    test_is_flush_valid()
    test_is_flush_invalid()
    print('all ok')
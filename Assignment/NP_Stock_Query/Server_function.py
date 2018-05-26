#
class Stock_Server:
    def __init__(self):
        self.stockinfo = [
            ["UGG Slippers", "Pink", "25$", 100],
            ["UGG Slippers", "Pink", "20$", 80],
            ["UGG Slippers", "Pink", "30$", 20],
            ["UGG Slippers", "Grey", "25$", 100],
            ["UGG Slippers", "Grey", "20$", 80],
            ["UGG Slippers", "Grey", "30$", 20],
            ["UGG boots", "Black", "100$", 200],
            ["UGG boots", "Black", "90$", 270],
            ["UGG boots", "Black", "130$", 150],
            ["UGG boots", "Red", "100$", 150],
            ["UGG boots", "Red", "90$", 240],
            ["UGG boots", "Red", "130$", 90],
        ]


    def stock_menu(self):
        menu_list = []
        index = 1
        for item in self.stockinfo:
            if item[:2] not in menu_list:
                menu_list.append(item[:2])

        # Add consecutive number in the front of the list
        for item in menu_list:
            item.insert(0, str(index))
            index += 1

        # return list like [[1,"UGG boots","Red"],]
        return menu_list

    def stock_query(self, index):
        highest_buy = 0
        highest_buy_item=[]
        result = ""
        # menu index starts from 1, therefore minus 1
        search_name = self.stock_menu()[index - 1][1:]
        for item in self.stockinfo:
            if item[:2]== search_name and item[3] > highest_buy:
                highest_buy_item=item
                highest_buy=item[3]
        for type in highest_buy_item:
            result+= str(type) +"\t"
        return result

    def __str__(self):
        menu = self.stock_menu()
        display_str = ""
        for item in menu:
            for type in item:
                display_str += type + '\t'
            display_str += "\n"
        return display_str


def main():
    pass


if __name__ == '__main__':
    a = Stock_Server()
    menu = a.stock_menu()
    print(a)


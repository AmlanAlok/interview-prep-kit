import unittest


class MyTestCase(unittest.TestCase):

    """create blank/ with data dictionary"""

    def test_1(self):
        dic = {}
        print('Initial dictionary = ', dic)
        self.assertEqual({}, dic)
        dic = {1: 'Amlan', 2: 'Alok'}
        print('Initiating dictionary with values = ', dic)
        self.assertEqual({1: 'Amlan', 2: 'Alok'}, dic)

    """dictionaries can have duplicate values"""

    def test_2(self):
        dic = {1: 'Amlan', 2: 'Alok', 3: 'Alok'}
        print('Initial dictionary = ', dic)
        self.assertEqual({1: 'Amlan', 2: 'Alok', 3: 'Alok'}, dic)

    """dictionaries can only have unique values. If same key is used again for a different value then, the value gets updated/ overwritten in the dic for that key"""

    def test_3(self):
        dic = {1: 'Amlan', 2: 'Alok', 2: 'Mohapatra'}
        print(dic)
        self.assertEqual({1: 'Amlan', 2: 'Mohapatra'}, dic)

    """Adding new element to dict"""
    """Updating already existing element"""

    def test_4(self):
        dic = {1: 'Amlan', 2: 'Alok'}
        print('Initial dictionary = ', dic)

        dic[3] = 'Jon'
        print('After adding new element to dict = ', dict)
        self.assertEqual({1: 'Amlan', 2: 'Alok', 3: 'Jon'}, dic)

        dic[3] = 'Arya'
        print('After updating new element in dict = ', dict)
        self.assertEqual({1: 'Amlan', 2: 'Alok', 3: 'Arya'}, dic)

    """deleting elements"""

    def test_5(self):
        dic = {1: 'Amlan', 2: 'Alok', 3: 'Jon'}
        print('Initial dictionary = ', dic)

        deleted_element = dic.pop(3)
        print('deleted_element = ', deleted_element)
        self.assertEqual('Jon', deleted_element)

        print('dic after deletion = ', dic)
        self.assertEqual({1: 'Amlan', 2: 'Alok'}, dic)

        popped_item = dic.popitem()
        print('popped_item = ', popped_item)

        print('dic after popitem = ', dic)
        self.assertEqual({1: 'Amlan'}, dic)

        print('clearing the dic')
        dic.clear()
        self.assertEqual({}, dic)


if __name__ == '__main__':
    unittest.main()

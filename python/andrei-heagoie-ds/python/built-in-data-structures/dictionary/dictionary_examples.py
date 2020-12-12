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

        """ 
        pop func allows you to delete elements based on the key 
        it returns the value of that key
        """
        deleted_element = dic.pop(3)
        print('deleted_element = ', deleted_element)
        self.assertEqual('Jon', deleted_element)

        print('dic after deletion = ', dic)
        self.assertEqual({1: 'Amlan', 2: 'Alok'}, dic)

        """
        popitem removes the last element of the dictionary
        """

        popped_item = dic.popitem()
        print('popped_item = ', popped_item)

        print('dic after popitem = ', dic)
        self.assertEqual({1: 'Amlan'}, dic)

        print('clearing the dic')
        dic.clear()
        self.assertEqual({}, dic)

    """ Accessing values from the dictionary using keys """

    def test_6(self):
        dic = {1: 'Amlan', 2: 'Alok', 3: 'Jon'}
        print('Initial dictionary = ', dic)

        """ accessing values from dict using key value  """

        print('Value for key = 1 is', dic[1])
        self.assertEqual('Amlan', dic[1])
        print('Value for key = 2 is', dic.get(2))
        self.assertEqual('Alok', dic.get(2))

    """ Other func for dictionaries """

    def test_7(self):
        dic = {1: 'Amlan', 2: 'Alok', 3: 'Jon'}
        print('Initial dictionary = ', dic)

        # this returns a list containing all the keys
        print('Display all keys = ', dic.keys())
        # self.assertEqual(dict_keys([1, 2, 3]), dic.keys())

        # this returns a list containing all the values
        print('Display all values = ', dic.values())

        # this returns a list of tuples
        print('Display all key-value pairs = ', dic.items())


if __name__ == '__main__':
    unittest.main()

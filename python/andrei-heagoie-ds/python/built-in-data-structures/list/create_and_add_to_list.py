import unittest


class MyTestCase(unittest.TestCase):
    """creating empty lists"""

    def test_create_blank_list(self):
        print('------------------------------------------')
        print('creating empty lists')
        print('------------------------------------------')
        print('creating a blank list')
        list_a = []
        print('Created new list = ', list_a)
        print('Length of the list = ', len(list_a))
        self.assertEqual(0, len(list_a))

    '''creating list containing multiple data types'''

    def test_create_list_with_different_data_types(self):
        print('------------------------------------------')
        print('creating list containing multiple data types')
        print('------------------------------------------')
        print('Creating list with different data types')
        list_a = [1, 1.2, 'Amlan', True]

        print('Created new list = ', list_a)
        self.assertEqual([1, 1.2, 'Amlan', True], list_a)

        print('Length of the list = ', len(list_a))
        self.assertEqual(4, len(list_a))

    '''append() function in list'''

    def test_add_list_as_an_element_to_a_list_using_append_function(self):
        print('------------------------------------------')
        print('append() function in list')
        print('------------------------------------------')
        print('Creating list with different data types')
        list_a = [1, 1.2, 'Amlan', True]
        print('Adding a list with 2 strings as element to list_a using append function')
        list_a.append(['Naruto', 'Uzumaki'])

        print('List after adding new element = ', list_a)
        self.assertEqual([1, 1.2, 'Amlan', True, ['Naruto', 'Uzumaki']], list_a)

        print('Length of the list = ', len(list_a))
        self.assertEqual(5, len(list_a))


    '''extend() function in list'''

    def test_add_elements_from_list_as_elements_to_a_list_using_extend_function(self):
        print('------------------------------------------')
        print('extend() function in list')
        print('------------------------------------------')
        print('Creating list with different data types')
        list_a = [1, 1.2, 'Amlan', True]
        print('Adding a list with 2 strings as element to list_a using extend function')
        list_a.extend(['Naruto', 'Uzumaki'])

        print('List after adding new element = ', list_a)
        self.assertEqual([1, 1.2, 'Amlan', True, 'Naruto', 'Uzumaki'], list_a)

        print('Length of the list = ', len(list_a))
        self.assertEqual(6, len(list_a))

    '''insert() function in list'''

    def test_add_element_to_be_inserted_at_index_using_insert_function(self):
        print('------------------------------------------')
        print('insert() function in list')
        print('------------------------------------------')
        print('Creating list with different data types')
        list_a = [1, 1.2, 'Amlan', True]
        print('Adding a string as element to list_a using insert function')
        i = 1
        list_a.insert(i, 'Naruto')

        print('List after adding new element = ', list_a)
        self.assertEqual([1, 'Naruto', 1.2, 'Amlan', True], list_a)
        print('Length of the list = ', len(list_a))
        self.assertEqual(5, len(list_a))
        self.assertEqual('Naruto', list_a[1])

    '''using del keyword on list'''

    def test_delete_element_from_list_at_given_index_using_del_keyword(self):
        print('------------------------------------------')
        print('using del keyword on list')
        print('------------------------------------------')
        print('Creating list with different data types')
        list_a = [1, 1.2, 'Amlan', True]
        i = 1
        del list_a[i]

        print('List after deleting element = ', list_a)
        self.assertEqual([1, 'Amlan', True], list_a)

        print('Length of the list = ', len(list_a))
        self.assertEqual(3, len(list_a))

        self.assertNotEqual(1.2, list_a[1])

    '''using remove() function in list on element that has single occurrence'''

    def test_delete_element_from_list_using_remove_function(self):
        print('------------------------------------------')
        print('using remove function in list')
        print('------------------------------------------')
        print('Creating list with different data types')
        list_a = [1, 1.2, 'Amlan', True]
        list_a.remove(1.2)

        print('List after deleting element = ', list_a)
        self.assertEqual([1, 'Amlan', True], list_a)

        print('Length of the list = ', len(list_a))
        self.assertEqual(3, len(list_a))

        self.assertNotEqual(1.2, list_a[1])

    '''using remove() function in list on element that has multiple occurrence will only remove the first occurrence of it.
    So if there are 2 elements such elements, remove function will have to be used twice to remove both of them'''

    def test_delete_element_from_list_using_remove_function(self):
        print('------------------------------------------')
        print('using remove function in list')
        print('------------------------------------------')
        print('Creating list with different data types')
        remove_element = 1.2
        list_a = [1, 1.2, 'Amlan', True, 1.2]
        list_a.remove(remove_element)
        print('List after deleting element = ', list_a)
        print('Length of the list = ', len(list_a))
        self.assertEqual(4, len(list_a))
        self.assertNotEqual(remove_element, list_a[1])

        list_a.remove(remove_element)
        print('List after deleting element = ', list_a)
        print('Length of the list = ', len(list_a))
        self.assertEqual(3, len(list_a))
        self.assertNotEqual(remove_element, list_a[-1])

    '''using pop function in list. Unlike the del keyword, pop function returns the deleted element'''

    def test_delete_element_from_list_at_given_index_using_pop_function(self):
        print('------------------------------------------')
        print('using pop function on list')
        print('------------------------------------------')
        print('Creating list with different data types')
        list_a = [1, 1.2, 'Amlan', True]
        i = 1
        deleted_element = list_a.pop(i)
        print('Deleted element = ', deleted_element)

        print('List after deleting element = ', list_a)
        self.assertEqual([1, 'Amlan', True], list_a)

        print('Length of the list = ', len(list_a))
        self.assertEqual(3, len(list_a))

        self.assertNotEqual(deleted_element, list_a[i])

    '''using clear function to empty a list'''

    def test_empty_list_using_clear_function(self):
        print('------------------------------------------')
        print('using clear function in list')
        print('------------------------------------------')
        print('Creating list with different data types')
        list_a = [1, 1.2, 'Amlan', True]
        list_a.clear()

        print('List after using clear function = ', list_a)
        self.assertEqual([], list_a)

        print('Length of the list = ', len(list_a))
        self.assertEqual(0, len(list_a))

    '''ways to access the list'''

    def test_accessing_elements(self):
        print('------------------------------------------')
        print('accessing elements in list')
        print('------------------------------------------')
        print('Creating list with different data types')
        list_a = [1, 1.2, 'Amlan', True]

        print('Display elements in the list using for loop (one by one)')
        for element in list_a:
            print(element)

        print('Displaying all elements = ', list_a)
        self.assertEqual([1, 1.2, 'Amlan', True], list_a)

        print('Accessing element at a given index = ', list_a[2])
        self.assertEqual('Amlan', list_a[2])

        print('Accessing elements from index 0 to 1 = ', list_a[0:2])
        self.assertEqual([1, 1.2], list_a[0:2])         # here 0 is inclusive and 2 is exclusive

        print('Access elements in reverse order = ', list_a[::-1])
        self.assertEqual([True, 'Amlan', 1.2, 1], list_a[::-1])

    '''some other functions to keep in mind'''

    def test_some_other_functions(self):
        print('------------------------------------------')
        print('some other functions of lists')
        print('------------------------------------------')
        print('Creating list of int')
        list = [1, 2, 3, 10, 30, 10]

        print('Created list is = ', list)
        self.assertEqual([1, 2, 3, 10, 30, 10], list)

        print('Length of created list = ', len(list))
        self.assertEqual(6, len(list))

        print('Find index of element 10\'s first occurrence = ', list.index(10))
        self.assertEqual(3, list.index(10))

        print('Find the number of times element 10 has occurred = ', list.count(10))
        self.assertEqual(2, list.count(10))

        print('display list in sorted way but without changing the original list = ', sorted(list))
        self.assertEqual([1, 2, 3, 10, 10, 30], sorted(list))

        print('sorting the original list using .sort(reverse=False) ')
        list.sort(reverse=False)
        print('Displaying sorted list = ', list)
        self.assertEqual([1, 2, 3, 10, 10, 30], list)

        print('sorting the original list using .sort(reverse=True) ')
        list.sort(reverse=True)
        print('Displaying reverse sorted list = ', list)
        self.assertEqual([30, 10, 10, 3, 2, 1], list)


if __name__ == '__main__':
    unittest.main()

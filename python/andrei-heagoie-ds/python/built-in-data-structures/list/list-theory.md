# List Theory

Source = https://www.edureka.co/blog/data-structures-in-python/

Python has 4 built-in data structures

1.  List
2.  Dictionary
3.  Tuple
4.  Sets

# 1.  List
<br>

##    1.1 Properties of List
<br>

####    1.1.1   Lists are used to store data of different data types in a sequential manner.
####    1.1.2   There are addresses assigned to every element of the list, which is called as Index.
####    1.1.3   The index value starts from 0 and goes on until the last element called the positive index.
####    1.1.4   There is also negative indexing which starts from -1 enabling you to access elements from the last to first.

<br>

##     1.2 Creating a List
<br>

####    1.2.1   Creating an empty list

    # creates an empty list
    my_list = []
    print(my_list)
    
    # Output
    [] 
    
####    1.2.2   Creating a list with data

    # creating list with data   
    my_list = [1, 2, 3, 'example', 3.132]
    print(my_list)
    
    # Output
    [1, 2, 3, ‘example’, 3.132]    

<br>

##     1.3 Adding elements to a list
<br>

####    1.3.1   The append() function adds all the elements passed to it as a single element.
####    1.3.2   The extend() function adds the elements one-by-one into the list.
####    1.3.3   The insert() function adds the element passed to the index value and increase the size of the list too.        

    my_list = [1, 2, 3]
    print(my_list)
    
    my_list.append([555, 12]) #add as a single element
    print(my_list)
    
    my_list.extend([234, 'more_example']) #add as different elements
    print(my_list)
    
    my_list.insert(1, 'insert_example') #add element i
    print(my_list)
    
    # Output
    [1, 2, 3]
    [1, 2, 3, [555, 12]]
    [1, 2, 3, [555, 12], 234, ‘more_example’]
    [1, ‘insert_example’, 2, 3, [555, 12], 234, ‘more_example’]
    
##      1.4 Deleting elements from a list

####    1.4.1   del keyword is used to delete elements at a given index. This does not return anything.
####    1.4.2   The pop() function does the same thing but returns the deleted element
####    1.4.3   remove(element) deletes the element with value passed as argument
####    1.4.4   clear() function empties the list

    my_list = [1, 2, 3, 'example', 3.132, 10, 30]
    
    del my_list[5] #delete element at index 5
    print(my_list)
    
    my_list.remove('example') #remove element with value
    print(my_list)
    
    a = my_list.pop(1) #pop element from list
    print('Popped Element: ', a, ' List remaining: ', my_list)
    
    my_list.clear() #empty the list
    print(my_list) 

    # Output
    [1, 2, 3, ‘example’, 3.132, 30]
    [1, 2, 3, 3.132, 30]
    Popped Element: 2 List remaining: [1, 3, 3.132, 30]
    []
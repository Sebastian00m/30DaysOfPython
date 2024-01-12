#Exercises: Day 11
#Exercises: Level 1
#a_Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers(num_1,num_2):
    return num_1+num_2

print('La suma es :',add_two_numbers(4,5))

#b_Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
#c_Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
#d_Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
#e_Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
#f_Write a function called calculate_slope which return the slope of a linear equation
#g_Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
#h_Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def print_list(*list):
    for i in list:
        print(i)

print_list(2,4,6,8,10,12)
#i_Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
def reverse_list(list):
    return list[::-1]

print(reverse_list([1,2,3,4,5,6,7]))
'''print(reverse_list([1, 2, 3, 4, 5]))
# [5, 4, 3, 2, 1]
print(reverse_list1(["A", "B", "C"]))
 # ["C", "B", "A"]'''
#j_Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
def capitalize_list_items (list):
    for i in list:
        list[list.index(i)]=i.capitalize()
    return list

print(capitalize_list_items(['python','javascript','java']))
#k_Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
def add_item(list, item_add):
    list.append(item_add)
    return list
print(add_item([1,2,3,4,5],'Puto'))
'''food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
    print(add_item(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
    numbers = [2, 3, 7, 9];
    print(add_item(numbers, 5))    #  [2, 3, 7, 9, 5]'''
#l_Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
def remove_item (list, r_item):
    list.remove(r_item)
    return list
print(remove_item([1,2,3,4],3))
'''food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
    print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
    numbers = [2, 3, 7, 9];
    print(remove_item(numbers, 3))  # [2, 7, 9]'''
#m_Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
def sum_of_numbers(num):
    total=0
    for i in range(num+1):
        total+=i
    return total
print(sum_of_numbers(5))
'''print(sum_of_numbers(5))  # 15
    print(sum_all_numbers(10)) # 55
    print(sum_all_numbers(100)) # 5050'''
#n_Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
def sum_of_odds(num):
    list_odds=[]
    for i in range(num+1):
        if i % 2 != 0:
            list_odds.append(i)
    return list_odds
print(sum_of_odds(5))
#ñ_Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that range.
def sum_of_even(num):
    list_odds=[]
    for i in range(num+1):
        if i % 2 == 0:
            list_odds.append(i)
    return list_odds
print(sum_of_even(5))

#Exercises: Level 2
#a_Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
def evens_and_odds(high):
    count_even=0
    count_odds=0
    for i in range(high + 1):
        if i % 2 == 0:
            count_even +=i
        else:
            count_odds +=i
    print('Cant of evens :',count_even)
    print('Cant of odds :',count_odds)
evens_and_odds(10)
    #print(evens_and_odds(100))
    # The number of odds are 50.
    # The number of evens are 51.
#b_Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
#c_Call your function is_empty, it takes a parameter and it checks if it is empty or not
#d_Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).

#Exercises: Level 3
#Write a function called is_prime, which checks if a number is prime.
#Write a functions which checks if all items are unique in the list.
def chek_unique_items(list):
    unique_items=set(list)
    if len(unique_items) == len(list):
        return True
    else:
        return False

if(chek_unique_items([1,2,3,4,5,6])):
    print('All items are unique')
else:
    print('The items are not unique')


#Write a function which checks if all the items of the list are of the same data type.
def chek_same_type(list):
    f_item=type(list[0])
    for item in list[1:]:
        if type(item) != f_item:
            return False
    return True
if(chek_same_type([1,2,3,4.34,'Python',6])):
    print('All items are the same type')
else:
    print('The items are not the same type')
#Write a function which check if provided variable is a valid python variable
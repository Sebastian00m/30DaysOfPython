#Exercises: Day 5
#Exercises: Level 1
#Declare an empty list
my_list= list()

#Declare a list with more than 5 items
my_list_1=[1,2,3,4,5,6,7]

#Find the length of your list
print(len(my_list_1))

#Get the first item, the middle item and the last item of the list
print('Fisrt item',my_list_1[0])
print('midle item',my_list_1[len(my_list_1)//2])
print('last item ',my_list_1[-1])

#Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
personal_data=['Mauro',23,1.60,'Single','Arg']

#Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

#Print the list using print()
print(it_companies)

#Print the number of companies in the list
print(len(it_companies))

#Print the first, middle and last company
print('First companie',it_companies[0])
print('Midle companie',it_companies[len(it_companies)//2])
print('Last companie',it_companies[-1])

#Print the list after modifying one of the companies
it_companies[0]='Mercado Libre'
print(it_companies)

#Add an IT company to it_companies
it_companies.append('Ebay')

#Insert an IT company in the middle of the companies list
it_companies.insert(len(it_companies)//2,'middle companie')
print(it_companies)

#Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[0]=it_companies[0].upper()
print(it_companies)

#Join the it_companies with a string '#;  '
print('#; '.join(it_companies))

#Check if a certain company exists in the it_companies list.

#Sort the list using sort() method

#Reverse the list in descending order using reverse() method

#Slice out the first 3 companies from the list

#Slice out the last 3 companies from the list

#Slice out the middle IT company or companies from the list

#Remove the first IT company from the list

#Remove the middle IT company or companies from the list

#Remove the last IT company from the list

#Remove all IT companies from the list

#Destroy the IT companies list
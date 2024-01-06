#Exercises - Day 4
#Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
main_string = 'Thirty', 'Days', 'Of', 'Python'
concat_string = ' '.join(main_string)
print(concat_string)
#Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
main_string1 = 'Coding', 'For' , 'All'
concat_string1 = ' '.join(main_string1)
print(concat_string1)
#Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"
#Print the variable company using print().
print(company)
#Print the length of the company string using len() method and print().
print(len(company))
#Change all the characters to uppercase letters using upper() method.
print(company.upper())
#Change all the characters to lowercase letters using lower() method.
print(company.lower())
#Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.swapcase())
print(company.title())
#Cut(slice) out the first word of Coding For All string.
print(company[0:7])
#Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(company.index('Coding'))
#Replace the word coding in the string 'Coding For All' to Python.
print(company.replace('Coding','Python'))
company_v2 = company.replace('Coding','Python')
print(company_v2.replace('All','Everyone'))
#3Change Python for Everyone to Python for All using the replace method or other methods.
#Split the string 'Coding For All' using space as the separator (split()) .
print(company.split())
#"Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
social_red = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(social_red.split(', '))
#What is the character at index 0 in the string Coding For All.
print(company[0])
#What is the last index of the string Coding For All.
print(len(company)-1)
#What character is at index 10 in "Coding For All" string.
print(company[10])
#Create an acronym or an abbreviation for the name 'Python For Everyone'.
words = company_v2.split()
print(words[0][0] + words[1][0] + words[2][2])

#Create an acronym or an abbreviation for the name 'Coding For All'.
#Use index to determine the position of the first occurrence of C in Coding For All.
#Use index to determine the position of the first occurrence of F in Coding For All.
#Use rfind to determine the position of the last occurrence of l in Coding For All People.
#Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
#Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
#Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
#Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
#Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
#Does ''Coding For All' start with a substring Coding?
#Does 'Coding For All' end with a substring coding?
#'   Coding For All      '  , remove the left and right trailing spaces in the given string.
#Which one of the following variables return True when we use the method isidentifier():
#30DaysOfPython
#thirty_days_of_python
#The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
libraries = 'Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon'
print(' # '.join(libraries))
# One vs others
teams = ['Dragons','Wolves','Pandas','Univorns']

for home_team in teams:
	for away_team in teams:
		if home_team != away_team:
			print(home_team + " Vs" + away_team)

#________________________________________
# Square Rot of number
import math
a = math.sqrt(5)	
print(a)

#________________________________________
# write a program that calculates how many seconds there are in a week, if a week is 7 days.  Print the result on the screen.
sIntoM = 60
sIntoH = 60 * sIntoM
sIntoDay = 24 * sIntoH
sIntoWeek = 7 * sIntoDay
print(sIntoWeek)			

#________________________________________
"""
Use Python to calculate how many different passwords can be formed with 6 lower case English letters.  
For a 1 letter password, there would be 26 possibilities.  
For a 2 letter password, each letter is independent of the other, so there would be 26 times 26 possibilities.  
Using this information, print the amount of possible passwords that can be formed with 6 letters.

"""
print(26*6)


#________________________________________
# implicit conversion. The interpreter automatically converts one data type into another. 
print(5+7.8)
--> 12.8

# Explicite Conversion. we manually convert from one data type to another by calling the relevant function for the data type we want to convert to.
total = 2048+4357+97658+125+8
files = 5
average = total / files
print("The average size is: " + str(average))  # here we concert it into string

#________________________________________
# Flesh out the body of the print_seconds function so that it prints the total amount of seconds given the hours, minutes, and 
# seconds function parameters.Remember that there are 3600 seconds in an hour and 60 seconds in a minute.
def print_seconds(hours, minutes, seconds):
    print(hours*60*60+minutes*60+seconds)

print_seconds(1,2,3)

-->3723
#________________________________________
# Use the get_seconds function to work out the amount of seconds in 2 hours and 30 minutes, then add this number to the 
# amount of seconds in 45 minutes and 15 seconds. Then print the result.

def get_seconds(hours, minutes, seconds):
  return 3600*hours + 60*minutes + seconds

amount_a = get_seconds(2,30,0)
amount_b = get_seconds(0,45,15)
result = amount_a+amount_b
print(result)

#________________________________________
# Month and Month days 
def month_days(month, days):

	print(month + " has " + str(days) + " days.")

month_days("jan", 31)
month_days("Feb", 28)

#________________________________________
# Code should be in maner that can be understooable refactored code is here

def rectangle_area(base, height):
	area = base*height  # the area is base*height
	print("The area is " + str(area))
rectangle_area(5,6)	

#________________________________________
# This function compares two numbers and returns them in increasing order.
def order_numbers(number1, number2):
	if number2 > number1:
		return number1, number2
	else:
		return number2, number1

# of the function call
smaller,bigger = order_numbers(100, 99)
print(smaller, bigger)

--> 99,100

#________________________________________
# 1) Complete the function to return the result of the conversion
def convert_distance(miles):
	km = miles * 1.6  # approximately 1.6 km in 1 mile
	return km

my_trip_miles = 55

# 2) Convert my_trip_miles to kilometers by calling the function above
my_trip_km = convert_distance(my_trip_miles)

# 3) Fill in the blank to print the result of the conversion
print("The distance in kilometers is " + str(my_trip_km))

# 4) Calculate the round-trip in kilometers by doubling the result,
#    and fill in the blank to print the result
print("The round-trip in kilometers is " + str(2.0*my_trip_km))


#________________________________________
# passing list in function
def print_alpha_nums(abc_list,num_list):
	for char in abc_list:
		for num in num_list:
				print(char,num)

	return

print_alpha_nums(['a','b','c'],[1,2,3])				

a 1
a 2
a 3
b 1
b 2
b 3
c 1
c 2
c 3

#________________________________________
# The is_positive function should return True if the number received is positive, 
# otherwise it returns None. Can you fill in the gaps to make that happen?

def is_positive(number):
  if number > 0:
    return True
  else:
    None

is_positive(1)  

--> True

# 2nd way

def is_even(number):
	if number %2 == 0:
		return True
	return False
	
is_even(11)	


#________________________________________
# use name validation

def hint_username(username):
	if len(username) < 3:
		print("Invalid username. User name must be at least 3 charactors long")
	elif len(username) > 15:
		print("Invalid username. User name must be at most 15 charactors long")
	else:
		print("Valid Username")

hint_username("gautam")			

# _______________________________
# Positive Negative Zero

def number_group(number):
  if number == 0:
    return "Zero"
  elif number < 0:
    return "Negative"
  else:
    return "Positive"

print(number_group(10)) #Should be Positive
print(number_group(0)) #Should be Zero
print(number_group(-5)) #Should be Negative

#_______________________________
# SUm fuction

def sum(x, y):
		return(x+y)
print(sum(sum(1,2), sum(3,4)))

--> 10
#_______________________________
# The longest_word function is used to compare 3 words. It should return the word with the most number of characters 
# (and the first in the list when they have the same length). Fill in the blank to make this happen
def longest_word(word1, word2, word3):
	if len(word1) >= len(word2) and len(word1) >= len(word3):
		word = word1
	elif len(word2) >= len(word1) and len(word2) >= len(word3):
		word = word2
	else:
		word = word3
	return(word)

print(longest_word("chair", "couch", "table"))
print(longest_word("bed", "bath", "beyond"))
print(longest_word("laptop", "notebook", "desktop"))

--> chair
	beyond
	notebook

#______________________________________
# Name format

def format_name(first_name, last_name):
	# code goes here
	string = "Name: "
	if first_name != "" and last_name != "":
	  string += last_name + ", " + first_name
	elif first_name != "" and last_name == "":
	  string += first_name
	elif first_name == "" and last_name != "":
	  string += last_name
	else:
	  string = ""
	return string 

print(format_name("Ernest", "Hemingway"))
# Should be "Name: Hemingway, Ernest"

print(format_name("", "Madonna"))
# Should be "Name: Madonna"

print(format_name("Voltaire", ""))
# Should be "Name: Voltaire"

print(format_name("", ""))
# Should be ""

--> Name: Hemingway, Ernest
	Name: Madonna
	Name: Voltaire

#_________________________________________________

# Class Grade System

def exam_grade(score):
	if score > 95:
		grade = "Top Score"
	elif score >= 60:
		grade = "Pass"
	else:
		grade = "Fail"
	return grade

print(exam_grade(65)) # Should be Pass
print(exam_grade(55)) # Should be Fail
print(exam_grade(60)) # Should be Pass
print(exam_grade(95)) # Should be Pass
print(exam_grade(100)) # Should be Top Score
print(exam_grade(0)) # Should be Fail


--> Pass
	Fail
	Pass
	Pass
	Top Score
	Fail

#___________________________________________________
# while loop under the function

def attempts(n):
    x = 1
    while x <= n:
        print("Attempt " + str(x))
        x += 1
    print("Done")
    
attempts(8)


#_____________________________________
 # Adding all no within 1 to 10

x= 1
sum = 0
while x < 10:
	sum += x
	x += 1
print(sum)	

#________________________
# Printing in rverse order

def count_down(start_number):
  current = 3
  while (current > 0):
    print(current)
    current -= 1
  print("Zero!")

count_down(3)

-->
3
2
1
Zero!

#_______________________________

def print_range(start, end):
	# Loop through the numbers from start to end
	n = start
	end = 4
	while n <= end:
		n += 1
		print(n)

print_range(0, 5)  # Should print 1 2 3 4 5 (each number on its own line) 



#____________________________________
# check no is power of 2

def is_power_of_two(n):
  # Check if the number can be divided by two without a remainder
  if n == 0:
    return False
  while n % 2 == 0:
    n = n / 2
  # If after dividing by two the number is 1, it's a power of two
  if n == 1:
    return True
  return False
  

print(is_power_of_two(0)) # Should be False
print(is_power_of_two(1)) # Should be True
print(is_power_of_two(8)) # Should be True
print(is_power_of_two(9)) # Should be False

#________________________________________________________________
# it returns the sum of all the divisors of a number, without including it. 
# A divisor is a number that divides into another without a remainder.
import math
def sum_divisors(n):
  sum = 1
  # Return the sum of all divisors of n, not including n
  div = 2
  if n == 0:
    return 0
  
  while div < n/2+1:
    if n % div == 0:
      sum += div
    div += 1
    
  
  
  return sum

print(sum_divisors(6)) # Should be 6 (sum of 1+2+3)
print(sum_divisors(12)) # Should be 16 (sum of 1+2+3+4+6)

--> 6
	16

#______________________________________	
# sum of square of no

def square(n):
    return n*n

def sum_squares(x):
    sum = 0
    for n in range(x):
        sum += n**2
    return sum

print(sum_squares(10)) # Should be 285

#__________________________
# itrate over list using for loop

friends = ['Gautam','vivek','Aman','sumit']

for friend in friends:
	print("HI", friend)

#__________________________________________________

# finsing lenght f list and sum ofnubers

values = [23,4,65,3,45,7,676]
sum = 0
length =0
for value in values:
	sum = sum + value
	length = length+1

print("Total sum: ", str(sum) + " - Average: " + str(sum/length))	 


#______________________________________________
# convert celcious to farenhite

def to_celsius(x):
	return (x-32)*5/9

for x in range(0,101,10):
	print(x , to_celsius(x))

#______________________________________________
# printing dice combination

for left in range(7):
	for right in range(left,7):
		print("[" + str(left) + "]" + "|" + str(right) + "]", end=" ")
	print()	

[0]|0] [0]|1] [0]|2] [0]|3] [0]|4] [0]|5] [0]|6]
[1]|1] [1]|2] [1]|3] [1]|4] [1]|5] [1]|6]
[2]|2] [2]|3] [2]|4] [2]|5] [2]|6]
[3]|3] [3]|4] [3]|5] [3]|6]
[4]|4] [4]|5] [4]|6]
[5]|5] [5]|6]
[6]|6]

#_____________________________________________________
# prints the first 10 cube numbers (x**3), starting with x=1 and ending with x=10.

for x in range(1,11):
  print(x**3)


#_____________________________________
# prints the multiples of 7 between 0 and 100

for i in range(0,101,7):
  print(i)  

#_____________________________________
# Factorial using recursion

def factorial(n):
	if n< 2:
		return 1
	return n* factorial(n-1)

print(factorial(5))		


#_________________________________________________________
# make the is_power_of function return whether the number is a power of the given base.

def is_power_of(number, base):
  # Base case: when number is smaller than base.
  if number < base:
    # If number is equal to 1, it's a power (base**0).
    return number == 1

  # Recursive case: keep dividing number by base.
  return is_power_of(number/base, base)

print(is_power_of(8,2)) # Should be True
print(is_power_of(64,4)) # Should be True
print(is_power_of(70,10)) # Should be False

#________________________________________________________
# sum_positive_numbers function, as a recursive function that returns the sum of all positive numbers between the number n received and 1

def sum_positive_numbers(n):
  sum = 0
  if n == 1:
    return 1
  else:
    sum += n + sum_positive_numbers(n-1)
    
  return sum

print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15

#____________________________
# this code to print out the numbers 1 through 7.


number = 1
while number <= 7:
	print(number, end=" ")
	number += 1


#_________________________________________
# The even_numbers function returns a space-separated string of all positive numbers that are divisible by 2.

def even_numbers(maximum):
    return_string = ""
    for x in range(0, maximum + 1):
        if x != 0 and x % 2 == 0:
            return_string += str(x) + " "
    return return_string.strip()


print(even_numbers(6))  # Should be 2 4 6
print(even_numbers(10))  # Should be 2 4 6 8 10
print(even_numbers(1))  # No numbers displayed
print(even_numbers(3))  # Should be 2
print(even_numbers(0))  # No numbers displayed


#_________________________________________________________
# Match first charactor and last charactor in string

def first_and_last(message):
  for char in message:
    if char[0] == char[-1]:
      return True
    elif char == " ":
      return True
    else:
      return False

print(first_and_last("else"))
print(first_and_last("tree"))
print(first_and_last(""))


#2n Way
def first_and_last(message):
  if not message or message[0] == message[len(message)-1]:
    return True
  else:
    return False

print(first_and_last("else"))
print(first_and_last("tree"))
print(first_and_last(""))
	

#__________________________________________
# Fill in the gaps in the initials function so that it returns the initials of the words contained in the phrase received, in upper case. 
# For example: "Universal Serial Bus" should return "USB"; "local area network" should return "LAN”.

def initials(phrase):
   words = phrase.split()
   result = ""
   for word in words:
       result = result+ word[0].upper()
   return result

print(initials("Universal Serial Bus")) # Should be: USB
print(initials("local area network")) # Should be: LAN
print(initials("Operating system")) # Should be: OS

#________________________________________________________
# String Formating

def student_grade(name, grade):
        return "{name} received {grade}% on the exam".format (name= name , grade=grade)
    
print(student_grade("Reed", 80))
print(student_grade("Paige", 92))
print(student_grade("Jesse", 85))

-->
Reed received 80% on the exam
Paige received 92% on the exam
Jesse received 85% on the exam

#____________________________________________________
# Using format fr clean output
# {:.2f} means that you’d format this as a float number, with two digits after the decimal dot. 
# the expression {:>3.2f} would align the text three spaces to the right


def to_celsius(x):
	return (x-3)*5/9

for x in range(0,101,10):
	print("{:>3} F | {:>6.2f} C".format(x,to_celsius(x)))   #{:>3} align the text three spaces to the right 

-->
  0 F |  -1.67 C
 10 F |   3.89 C
 20 F |   9.44 C
 30 F |  15.00 C
 40 F |  20.56 C
 50 F |  26.11 C
 60 F |  31.67 C
 70 F |  37.22 C
 80 F |  42.78 C
 90 F |  48.33 C
100 F |  53.89 C

#___________________________________________
# miles to KM

def convert_distance(miles):
	km = miles * 1.6 
	result = "{} miles equals {:.1f} km".format(miles,km)
	return result

print(convert_distance(12)) # Should be: 12 miles equals 19.2 km
print(convert_distance(5.5)) # Should be: 5.5 miles equals 8.8 km
print(convert_distance(11)) # Should be: 11 miles equals 17.6 km


#____________________________________________
# uses the format method to return first_name and the first initial of last_name followed by a period. 
# For example, nametag("Jane", "Smith") should return "Jane S."

def nametag(first_name, last_name):
	return("{} {}.".format(first_name,last_name[0]))

print(nametag("Jane", "Smith")) 
# Should display "Jane S." 
print(nametag("Francesco", "Rinaldi")) 
# Should display "Francesco R." 
print(nametag("Jean-Luc", "Grand-Pierre")) 
# Should display "Jean-Luc G." 


#___________________________________________
# Check if the old string is at the end of the sentence 

def replace_ending(sentence, old, new):
	# Check if the old string is at the end of the sentence 
	if old[:] == sentence[-len(old):]:
		# Using i as the slicing index, combine the part
		# of the sentence up to the matched string at the 
		# end with the new string
		i = len(old)
		new_sentence = sentence[:-i] + new
		return new_sentence

	# Return the original sentence if there is no match 
	return sentence
	
print(replace_ending("It's raining cats and cats", "cats", "dogs")) 
# Should display "It's raining cats and dogs"
print(replace_ending("She sells seashells by the seashore", "seashells", "donuts")) 
# Should display "She sells seashells by the seashore"
print(replace_ending("The weather is nice in May", "may", "april")) 
# Should display "The weather is nice in May"
print(replace_ending("The weather is nice in May", "May", "April")) 
# Should display "The weather is nice in April"


#___________________________________________________________________________
# palindrome check

def is_palindrome(input_string):
	# We'll create two strings, to compare them
	new_string = ""
	reverse_string = ""
	# Traverse through each letter of the input string
	for letter in input_string:
		# Add any non-blank letters to the 
		# end of one string, and to the front
		# of the other string. 
		if letter != " ":
			new_string += letter.lower() 
			reverse_string = letter.lower() + reverse_string
	# Compare the strings
	
	if new_string == reverse_string:
		return True
	return False

print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True


#_______________________________________________________________
# replace the domain of email

def replace_domain(email, old_domain, new_domain):
	if "@" + old_domain in email:
		index = email.index("@" +old_domain)
		new_email = email[:index] + "@" +new_domain
		return new_email
	return email	

print(replace_domain("gautam@mac.com","@gmail.com","@mac.com"))


#_______________________________________________________________
# Check Leap Year

def is_leap(year):
    leap = False
    
    # Write your logic here
    if year%4==0:
        if year%100==0:
            if year%400==0:
                leap=True
            else:
                leap=False
        else:
             leap=True
    else:
        leap=False

    return leap

year = int(input())
print(is_leap(year))

#_______________________________________
# First Name Last Name 

def print_full_name(first, last):
    print("Hello {} {}! You just delved into python.".format(first,last))

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)

#________________________________________________
# file size

def file_size(file_info):
    File_Name, File_Ext, Bytes = file_info
    return("{:.2f}".format(Bytes / 1024))

print(file_size(('Class Assignment', 'docx', 17875))) # Should print 17.46
print(file_size(('Notes', 'txt', 496))) # Should print 0.48
print(file_size(('Program', 'py', 1239))) # Should print 1.21


#___________________________________
# Iterating over Lists

animals = ['zebra','Lion','Dolphin','Monkey']

char = 0
for animal in animals:
	char = char+len(animal)

print("Total charactors: {}, Average Lengh: {}".format(char,char/len(animals)))

#____________________________________
# Enumerate - if you want to access the elements in a list, along with the index of the element.
# The enumerate() function takes a list as a parameter and returns a tuple for each element in the list. The first value of the tuple is the index and the second value is the element itself.


winers = ['Ashley', "Dylan","Resse"]
for index,person in enumerate(winers):
	print("{} - {}".format(index+1,person))

1 - Ashley
2 - Dylan
3 - Resse	

#____________________________________
# skip odd index element

def skip_elements(elements):
    list=[]
    for index,element in enumerate(elements):
        if index%2==0:
            list.append('{}'.format(element))
    return list

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']


#________________________________________
# Name with full Email

def full_emails(people):
	result =[]
	for email,name in people:
		result.append("{}  <{}>".format(name,email))
	return result

print(full_emails([("gautam@example.com", "gautam kumar"),("gaurav@example.com", "Gaurac sen"),("sam@example.com", "cherry sam")]))	


#________________________________________
# List comprehensions

multiples = []
for x in range(1,11):
	multiples.append(x*7)
print(multiples)	

# In just one line

multiples = [x*7 for x in range(1,11)]
print(multiples)


#--------------------------------------------
# create list comprehension from the existing list

# Find the length of each element in list
languages = ['python','perl','c','c++','java','Ruby','Go']
lenghts = [len(language) for language in languages]
print(lenghts)


# find multiple of 3(use if condition in it)
z = [x for x in range(0,101) if x % 3 == 0]
print(z) 


# use function for list comprehension
def odd_numbers(n):
	return [x for x in range(0, n+1) if x%2 != 0]

print(odd_numbers(5))  # Should print [1, 3, 5]
print(odd_numbers(10)) # Should print [1, 3, 5, 7, 9]
print(odd_numbers(11)) # Should print [1, 3, 5, 7, 9, 11]
print(odd_numbers(1))  # Should print [1]
print(odd_numbers(-1)) # Should print []


#______________________________________________________________
# rename file extentions

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
newfilenames = [word.replace("hpp","h") if word.endswith("hpp") else word for word in filenames ]

print(newfilenames) 
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]

#_______________________________________________________
# The group_list function accepts a group name and a list of members, and returns a string with the format: group_name: member1, member2, … 

def group_list(group, users):
  members = ', '.join(users)
  return group + ': ' + members

print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users", "")) # Should be "Users:"

== >
Marketing: Mike, Karen, Jake, Tasha
Engineering: Kim, Jay, Tom
Users: 

#______________________________________

def guest_list(guests):
    for name, age, job in guests:
        
        print("{} is {} years old and works as {}".format(name,age,job))

guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])

"""
Output should match:
Ken is 30 years old and works as Chef
Pat is 35 years old and works as Lawyer
Amanda is 25 years old and works as Engineer
"""
#________________________________________________
# Dictionary Example

toc = {"Introduction":1, "Chapter 1":4, "Chapter 2":11, "Chapter 3":25, "Chapter 4":30}
toc["Epilogue"] = 39 # Epilogue starts on page 39
toc["Chapter 3"] = 24 # Chapter 3 now starts on page 24
print(toc) # What are the current contents?
print("Chapter 5" in toc) # Is there a Chapter 5?


#_______________________________________________
# how many times each letter apppear in peice of text


def count_letters(text):
	result = {}
	for letter in text:
		if letter not in result:
			result[letter] = 0
		result[letter] = result[letter] + 1
	return result

print(count_letters('aaaa')) # {'a': 4}

print(count_letters("Tenet")) # {'T': 1, 'e': 2, 'n': 1, 't': 1}

print(count_letters('A long string with lot of letters')) # {'A': 1, ' ': 6, 'l': 3, 'o': 3, 'n': 2, 'g': 2, 's': 2, 't': 5, 'r': 2, 'i': 2, 'w': 1, 'h': 1, 'f': 1, 'e': 2}


#_________________________________________________________________________

wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
for cloth in wardrobe:
    for color in wardrobe[cloth]:
        print("{} {}".format(color, cloth))

#_________________________________________________________________________
# to generate a list that contains complete email addresses (e.g. diana.prince@gmail.com).

def email_list(domains):
	emails = []
	for domain,users in domains.items():
	  for user in users:
	    emails.append(user+'@'+domain)
	return(emails)

print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))

#_____________________________________________________________________
# print keys

host_addresses = {"router": "192.168.1.1", "localhost": "127.0.0.1", "google": "8.8.8.8"}
print(host_addresses.keys())



#______________________________________
# code to iterate through the keys and values of the car_prices dictionary, printing out some information about each one.

def car_listing(car_prices):
  result = ""
  for car,price in car_prices.items():
    result += "{} costs {} dollars".format(car,price) + "\n"
  return result

print(car_listing({"Kia Soul":19000, "Lamborghini Diablo":55000, "Ford Fiesta":13000, "Toyota Prius":24000}))


#________________________________________________


def squares(start, end):
	return [x*x for x in range(start,end+1)]

print(squares(2, 3)) # Should be [4, 9]
print(squares(1, 5)) # Should be [1, 4, 9, 16, 25]
print(squares(0, 10)) # Should be [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]	



#________________________________________

# The highlight_word function changes the given word in a sentence to its upper-case version. 
# For example, highlight_word("Have a nice day", "nice") returns "Have a NICE day". Can you write this function in just one line?

def highlight_word(sentence, word):
  ret = ""
  l = len(word)
  words = sentence.split()
  for i,w in enumerate(words):
    if w[:l] == word:
      ret += w[:l].upper()+w[l:]
    else:
      ret += w
    if i != len(words)-1:
      ret += " "
  return ret

print(highlight_word("Have a nice day", "nice"))
print(highlight_word("Shhh, don't be so loud!", "loud"))
print(highlight_word("Automating with Python is fun", "fun"))


#_________________________________________________________________________________
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Pull it All Togeter !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


def get_event_date(event):
  return event.date

# Define function
def current_users(events):
	# sort the events and pass the funtion as key
  events.sort(key=get_event_date)
  # store name and user of the machine
  machines = {}
  for event in events:
    if event.machine not in machines:
      machines[event.machine] = set()
    if event.type == "login":
    	# add usrs
      machines[event.machine].add(event.user)
    elif event.type == "logout" and event.user in machines[event.machine]:
      machines[event.machine].remove(event.user)
  return machines

def generate_report(machines):
  for machine, users in machines.items():
    if len(users) > 0:
      user_list = ", ".join(users)
      print("{}: {}".format(machine, user_list))

class Event:
  def __init__(self, event_date, event_type, machine_name, user):
    self.date = event_date
    self.type = event_type
    self.machine = machine_name
    self.user = user


events = [
    Event('2020-01-21 12:45:56', 'login', 'myworkstation.local', 'jordan'),
    Event('2020-01-22 15:53:42', 'logout', 'webserver.local', 'jordan'),
    Event('2020-01-21 18:53:21', 'login', 'webserver.local', 'lane'),
    Event('2020-01-22 10:25:34', 'logout', 'myworkstation.local', 'jordan'),
    Event('2020-01-21 08:20:01', 'login', 'webserver.local', 'jordan'),
    Event('2020-01-23 11:24:35', 'logout', 'mailserver.local', 'chris'),
]

users = current_users(events)
print(users)


generate_report(users)

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!










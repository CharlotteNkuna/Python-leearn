#Making the computer speak
print ("hello world")

#Storing data inside variable
name = "Charlotte"
print (name)

#Making code interactive
name = input("Enter your name ")
print(f"Greetings, {name}")


#Converting data type
# concerting string to integer
birthYear = input("Enter your birth year: ")
age = 2026 - int(birthYear) #Parsing the string to int
print(age)

#Type conversion
#Combining data types
first = input("First number: ")
second = input("Second number: ")
#sum = int(first) + int(second)
sum = int(first) + float(second)
print("Sum: " + str(sum))

#OR 
first = float (input("First number: "))
second = float (input("Second number: "))
sum = first + second
print(sum)


#String objects and its build in methods
course = 'Python for beginners'
print (course.upper())
# replace method
print(course.replace("beginners", "pros"))
#Finds by index
print(course.find("for"))
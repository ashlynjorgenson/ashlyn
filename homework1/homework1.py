
#---Variables and Datatypes---
a=10
print(a)
print(type(a))
#a is an integer
b=1.5
print(b)
print(type(a))
#b is a float
c=3j
print(c)
print(type(c))
#c is a complex number
d="hello"
print(d)
print(type(d))
#d is a string
e=[1,2,3]
print(e)
print(type(e))
#e is a list
f={"name": "Ellen", "favorite fruit": "strawberry"}
print(f)
print(type(f))
#f is a dictionary
g=(1,2)
print(g)
print(type(g))
#g is a tuple
h=["apple", "banana", "strawberry"]
print(h)
print(type(h))
#h is a list
i=True
print(i)
print(type(i))
#i is a boolean
j=None
print(j)
print(type(j))
#j is a NoneType
k=[True, "blue", 12]
print(k)
print(type(k))
#k is a list
l=str(14)
print(l)
print(type(l))
#l is a string
m=1e4
print(m)
print(type(m))
#m is an float
n={1,2,3}
print(n)
print(type(n))
#n is a set
# 1: 9
# 2: String, float, integer, complex number, list, set, dictionary, tuple, boolean, NoneType
# 3: A, b; l, d; h, k
# 4: It’s a string. It’s not an integer because an integer is the input of the function, not the function itself. Converts numbers into strings
print(10>9)
#true, 10 is greater than 9
print(10==9) #false, 10 and 9 are not equal
print(10<=9) #false, 10 is not less than or equal to 9
bool("abc") #true, abc is the correct sequence
bool(123) #true, 123 is a correct sequence
bool(["apple", "cherry", "banana"]) #true, the list is all of fruits
print("start")
bool(True) #true
bool(False) #false
bool(0)
bool("")
bool(" ")
bool(())
bool([])
bool({})
bool(True and False)
bool(True and True)
bool(False and False)
bool(True or False)
bool(True or True)
bool(False or False)
bool(not(False))
bool(not(True))
print("3.3")
print(10+5) #15, + performs addition
print(10-5) #5, - performs subtraction
print(2*4) #8, * performs multiplication
print(6/3) #2, / performs division
print(5%2) #1, % performs division then outputs the remainder
print(3**2) #9, ** performs raises a variable to a power
print(15//2) #7, // performs division and rounds the quotient to the nearest whole number
print(5==2) #False, == performs equal to
print(10!=10) #False, != performs not equal to
print(2<5) #True, < performs less than
print(12>5) #True, > performs greater than
print(5<=6) #True, <= performs less than or equal to
print(1>=10) #False, >= performs greater than or equal to

print("3.3.3")
x=5
x+=5 #adds a value to a variable then assigns the result back to the same variable
print(x)
x-=4 #subtracts the value on the right hand side from the variable on the left side. Assigns the result back to the variable.
print(x)
x*=3 #multiplies the value of the variable by the value of the operand. Assigns the result back to the variable
print(x)
# 1: The difference between / and // is / divides while // rounds the division to the nearest whole integer
# 2: the difference between % and // is % outputs the remainder of a division operation while // outputs the rounded quotient
# 3: You would use %
print(5%4) #example
# 4: an assignment operator assigns a value to a variable

# 3.3.4 Logical Operators
#and combines two or more conditions. If at least one condition is false, it outputs False. If all conditions are true, then it outputs True
print(True and True)
print(True and False)
# and evaluates to True if at least one condition is true, otherwise it outputs False
print(True or True)
print(False or False)
# not Inverts the truth value
a=True
print(not a)

print("3.4: Strings")
my_string="Hello"
print(my_string) # prints hello
print(my_string[0]) # prints h
print(my_string[1]) # prints e
print(my_string[2]) # prints l
print(my_string[3]) # prints l
print(my_string[4]) # prints o
print(my_string[-1]) # prints o
print(my_string[1:3]) # prints el
print(my_string[0:5:2]) # prints hlo
print(len(my_string)) # prints 5
print(my_string+ "goodbye") # prints Hellogoodbye
print(my_string*7) # prints Hello 7 times
name="Oski"
print("Hello, my name is", name) # prints Hello, my name is Oksi
name="Oski"
print(f"Hello, my name is {name}") # prints Hello, my name is Oski

print("3.5: Terminal Commands")
# cd
# Change directories. Use it to move from one folder to another
# cd python_decal_fa25
# ls, list. Use it to list everything in the folder you're in.
# ls
# ls -a, list all including hidden folders. Use it to find hidden folders.
# mkdir, make directory. Use it to make a new folder
# mkdir python_decal_fa25
# cat, concatenate. display file contents to standard output.
# cat python_decal_fa25
# pwd, print working directory. use it to view your file path and where you're at
# cd .., naviagtes one level up in a heirarchy of the parent directory. Use it to travel back one folder.
# cd .. datatypes.py
# cd ., current directory. navigates to current directory (?)
# cp, copy. use to copy files or directories
# cp python_decal_fa25
# mv, move. moves or renames files
# mv python_decal_fa25
# rm, remove. removes files from directories
# remove python_decal_fa25
#clear, clears contents of mutable data structure
# my_list.clear()
# grep. search for pattern in each file or standard input
#echo $0: prints current shell type. Type and enter echo $0 into your terminal.
#touch: creates a new file. Type touch then desired filename
#whoami: tells you the current user. Type whoami on the command line.
# 2: ls lists everything it can see in a directory while ls -a shows you everything including hidden folders or files
# 3: It’s a file that’s hidden by default to prevent accidental deletion
# 4: For rm; -f forces removal; Type rm -f <filename> to remove said file;-i prompts before removal;
# Type rm -i <filename> to remove said file with a prompt;-r recursively removes directories and their contents; Type rm -r directory_name



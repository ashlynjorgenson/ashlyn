# def say_goodbye(name):
#     print("Goodbye,", name)
# name="Ashlyn"
# say_goodbye(name)

def area_of_circle(radius):
    print(3.14 * radius**2) 
# radius=4
# print(area_of_circle(radius))


def subtract(a, b):
    return a-b
# a=1000000
# b=2
# print(subtract(a, b))

def multiply(a, b):
    return a * b
# a=14000
# b=1700
# print(multiply(a, b))

def divide(a, b):
    return a/b
# a=9
# b=3
# print(divide(a, b))

def outfit(temperature):
    minimum_temp=min(temperature)
    maximum_temp=max(temperature)
    return (minimum_temp, maximum_temp)
# temperature=[62, 65, 68, 70, 72, 75]
# print(outfit(temperature))

def is_weekend(day):
    if day == 7 or day == 1:
        return "It is the weekend! Party it up"
    else:
        return "it is not the weekend loser"
sunday=1
monday=2
tuesday=3
wednesday=4
thursday=5
friday=6
saturday=7
# day=4
# print(is_weekend(day))


def efficiency(distance, fuel_used):
    miles_per_gallon=distance/fuel_used
    return miles_per_gallon
# distance=100
# fuel_used=6.8
# print(efficiency(distance, fuel_used))

def secret_code(integer):
    last_digit= integer % 10
    remainder= integer//10
    num_digits = len(str(remainder))
    code= last_digit * (10 ** num_digits) + remainder
    return code
# integer=12345
# last_digit=5
# remainder=12345
# num_digits=4
# print(secret_code(integer))

def raise_to_power(x, y):
    start=1
    for _ in range(y):
        start=start * x
    return start
# x=4
# y=2
# print(raise_to_power(x,y))

def minimum(number):
    minimum=number[0]
    for num in number:
        if num<minimum:
            minimum=num
    return minimum
# list=[1,2,3,4,5,6,7,8,9,10]
# print(minimum(list))

def maximum(number):
    maximum=number[0]
    for num in number:
        if num>maximum:
            maximum=num
    return maximum
# list=[1,2,3,4,5,6,7,8,9,10]
# print(maximum(list))


# number=[3, 10, 1000000, 2, 5]
def minimum(number):
    min=number[0]
    i = 1
    while i < len(number):
        if number[i] < min:
            min=number[i]
        i+=1
    return min

# print(minimum(number))


def maximum(number):
#     number=[1,2,3,4,5]
    max=number[0]
    i = 1
    while i < len(number):
        if number[i] > max:
            max=number[i]
        i+=1
    return max
# print(maximum(number))

def sum_of_digits(number):
    total=0
    while number>0:
        digit=number%10
        total+=digit
        number=number // 10
    return total
# print(sum_of_digits(1234))








def counting_vowels_and_consonants(sentence):
    vowels="aeiouAEIOU"
    num_vowels=0
    num_con=0 #set count to 0 to start
    for character in sentence:
        if character.isalpha():
            if character in vowels:
                num_vowels+=1
            else:
                num_con+=1
    
    return(num_vowels, num_con)

print(counting_vowels_and_consonants("Hello, World!"))
    



    
    
def average_vowels_and_consonants(paragraph):
    import re
    sentence=re.split(r'(?<=[.!?])+', paragraph)
    num_sentence=0
    for s in sentence:
        num_sentence+=1
    vowels="aeiouAEIOU"
    num_vowels=0
    num_con=0
    for s in sentence:
        for character in s:
            if character in vowels:
                num_vowels+=1
            else:
                num_con+=1
    if num_sentence==0:
        avg_vowels=0
        avg_con=0
    else:
        avg_vowels_per_sentence=num_vowels/num_sentence
        avg_con_per_sentence=num_con/num_sentence
    
    return(num_sentence, avg_vowels_per_sentence, avg_con_per_sentence)

print(average_vowels_and_consonants("Fall in love with some activity, and do it! "
    "Nobody ever figures out what life is all about, and it doesn't matter. "
    "Explore the world. "
    "Nearly everything is really interesting if you go into it deeply enough. "
    "Work as hard and as much as you want to on the things you like to do the best. "
    "Don't think about what you want to be, but what you want to do. "
    "Keep up some kind of a minimum with other things so that society doesn't stop you from doing anything at all."))
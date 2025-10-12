favorite_foods=["tacos","grapes","salads","potato","chicken wings"]

print(favorite_foods)

print(favorite_foods[1])

print(favorite_foods[-3])

favorite_foods.append("rice") #kept outputting None when it said print(favorite_foods.append("rice"))

print(favorite_foods)

favorite_foods.insert(0, "apples") #Error: print(favorite_foods.insert["apple"])TypeError: 'builtin_function_or_method' object is not subscriptable. I fixed it by removing the print and adding a print(list) after the insert

print(favorite_foods)

favorite_foods.remove("salads")

print(favorite_foods)

print(len(favorite_foods))

print(favorite_foods)

favorite_foods_upper = []
for food in favorite_foods:
    favorite_foods_upper.append(food.upper())
print(favorite_foods_upper)

print(favorite_foods[0::5])


def is_potato_present():
    for food in favorite_foods:
        if food=="potato":
            print("A potato!")
            break
    else:
        print("No potato :(")
        
print(is_potato_present())

numbers=list(range(0,21))

def get_first_15(numbers):
    return numbers[:15]
first_15=get_first_15(numbers)
print(first_15)


def get_every_5th(first_15): #Takes the list from get first 15() and returns every 5th element from it (So index 0, 5, 10...)
    return first_15[::5]
every_5th=get_every_5th(first_15)
print(every_5th)

def reverse_and_stride(every_5th):
    every_5th[::-1]
    return every_5th[::3]
reverse=reverse_and_stride(every_5th)
print(reverse)

numbers=[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(numbers[2])

print(numbers[1][1])

numbers.append([10, 11, 12])
print(numbers)

def sum_nested(numbers):
    row_sum=[]
    for row in numbers:
        row_sum.append(sum(row))
    return row_sum
print(sum_nested(numbers))

print("next task")
#Write a function that uses nested for loops to create a 5x5 list of numbers from 1 to 25. Store the result in a new variable
def nested_loop():
    grid=[]
    num=1
    for i in range(5):
        row=[]
        for j in range(5):
            row.append(num)
            num+=1
        grid.append(row)
    return grid
new_grid=nested_loop()
print(new_grid)

#Write a function that replaces all multiples of 3 with “?”. Store the updated 5x5 list in a new variable
def changing_multiples_of_3(new_grid):
    for row in new_grid:
        for i in range(len(row)):
            if row[i] % 3 ==0:
                row[i]="?"
    return new_grid
multi_of_3=changing_multiples_of_3(new_grid)
print(multi_of_3)

print("3.4.3") #Write a function that adds all elements not equal to “?” and returns the sum. Save the
# result in a variable. Hint: Use != to skip “?”.
# Note: To clarify, edit the list with the first function and then edit it again with the second function

def sum_of_grid(multi_of_3):
    total=0
    for row in multi_of_3:
        for num in row:
            if num != "?":
                total += num
    return total
print(sum_of_grid(multi_of_3))


ages = {
"Katie": 30,
"Mariam": 42,
"Safia": 25,
"Mira": 48
}
print(ages["Katie"])
ages["Mira"]=100
print(ages)

del ages["Mariam"]
print(ages)

for key,value in ages.items():
    print(f"{key}:{value}")
print(ages.items)




print(new_grid)

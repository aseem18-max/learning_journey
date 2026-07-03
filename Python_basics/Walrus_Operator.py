numbers = [1,2,3,4,5]
while (n := len(numbers)) > 0:
    print(numbers.pop())
foods = list()
# Without Walrus Operator
while True:
    food = input("Which food do you like? : ")
    if food == 'quit':
        break
    foods.append(food)
print(foods)
# Using Walrus Operator(:=)
while (food := input("Which food do you like? : ")) != 'quit':
    foods.append(food)
print(foods)
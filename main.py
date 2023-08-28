# write your code here
favorite_animals = [ 'dog', "cat","monkey" , " rabbit"]
print(favorite_animals )
print(favorite_animals[1])
favorite_animals.remove("monkey")

favorite_animals.append("layon")
for animal in favorite_animals:
    print(f"i love {animal}")

numbers = [1,2,3,4,5]
number_sum = 0 
for number in numbers :
      number_sum += number
print(f'The total is {number_sum}')
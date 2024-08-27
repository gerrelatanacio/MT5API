users = ["Dave", "John", "Sara"]
data = ["Dave", 42, True]
emptylist = []

person = {"name": "Gerrel Atanacio", "age": 31, "job": "Software Engineer"}

print(person)

avitDepartments = dict(
    {
        "integration": ["software development", "hybrid cloud"],
        "services": ["connectivity", "collaboration", "cybersecurity"],
        "systems": "insideSales",
    }
)

print(avitDepartments)


# Nested dictionaries
member1 = {"name": "Plant", "instrument": "vocals"}
member2 = {"name": "Page", "instrument": "guitar"}

band = {"member1": member1, "member2": member2}


nums = {1, True, False, 2, 3, 4, 5, 0}
print(nums)  # {False, 1, 2, 3, 4, 5}

morenums = {5, 6, 7, 8, 19, 24}
nums.update(morenums)
print(nums)  # {False, 1, 2, 3, 4, 5, 6, 7, 8, 19, 24}


one = {1, 2, 3}
two = {5, 6, 7}
mynewset = one.union(two)
print(mynewset)

two = {2, 3, 4}
one.intersection_update(two)
print(one)

one = {1, 2, 3}
two = {2, 3, 4}
one.symmetric_difference_update(two)
print(one)


value = 1
while value <= 10:
    print(value)
    if value == 5:
        break
    value += 1

print("")
value = 0
while value <= 10:
    value += 1
    if value == 5 or value == 11:
        continue
    print(value)
else:
    print("Value is now equal to: " + str(value))

names = ["Gerrel", "MK", "Levin", "Aika"]
for name in names:
    print(name)

for letter in "Mississippi":
    print(letter)


for name in names:
    if name == "Levin":
        continue
    print(name)

for number in range(0, 101, 5):
    print(number)
else:
    print("For Loop is now completed")


names = ["Gerrel", "MK", "Levin", "Aika"]
actions = ["washes the dishes", "sweeps the floor", "watches tv"]

for action in actions:
    for name in names:
        print(name + " " + action)

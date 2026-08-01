# fruits = ['apple','banana','orange','grape']
# fruits.remove('banana')
# print(fruits)
# numbers = [10,20,30,40,50]
# numbers.pop(1)
# print(numbers)
    # color = ['red','blue','green','yellow']
    # color.pop()
    # print(color)
# animals = ['cat','dog','rabbit']
# animals.clear()
# print(animals)
# scores = [80,75,90,65,100]
# del  scores[0]
# print(scores)
# shopping = ['milk','egg','bread','apple']
# shop = input("อยากเอาอะไรออก")
# shopping.remove(shop)
# print(shopping)
# names = ['tom','anna','john','mike']
# name = int(input("เอาเลขอะไรออกดีระหว่าง 0-3"))
# names.pop(name)
# print(names)
students = ['alice','bob','charlie','david','emma']
print("1. remove by name")
print("2.remove by index")
print("3. delete all")

choice = input("choose: ")

if choice == '1':
    name = input("enter name: ")
    if name in students:
        students.remove(name)

elif choice == "2":
    index = int(input("enter index: "))
    students.pop(index)

elif choice == "3":
    students.clear()

print(students)

# name = input("คุณชื่ออะไร").upper()
# age = int(input("คุณอายุเท่าไร"))
# if age < 13:
#     print("hello",name,"you are kid")
# elif age >= 13:
#     print("hello",name,"welcome")
# coffee = int(input("เอากาแฟเท่าไร"))
# cake = int(input("เอาเค้กกี่ชิ้น"))
# ราคารวม = (cake*30)+(coffee*50)
# print(ราคารวม)
# if ราคารวม  > 200:
#     print("ลด10%")
#     ราคาจริง = (ราคารวม*0.9)
#     print(ราคาจริง)
# else:
#     print("ไม่ได้ส่วนลด")
# C = int(input("อุณหภูมิเท่าไร"))
# ค่าเคลวิน = C+273
# print(ค่าเคลวิน)
# if C > 30:
#     print("hot")
# elif C < 20:
#     print("cold")
# else:
#     print("nice weather")
# Username = input("กรอกชื่อ:")
# password = input("กรอกรหัส:")
# if Username == "admin" and password == "1234":
#     print("login success")
# else:
#     print("login fail")
# name = input("คุณชื่ออะไร:").upper()
# agenow = int(input("อายุเท่าไร:"))
# อาหารที่ชอบ = input("คุณชอบกินอะไร:")
# print(name)
# print(agenow+1)
# print("you love",อาหารที่ชอบ,"ที่สุด")
# number = int(input("รับค่าตัวเลข"))
# if number % 2 == 0:
#     print("e")
# else:
#      print("o")
# score = int(input("รับคะแนนตั้งแต่ 1-100"))
# if score > 100:
#     print("ไม่ถูกต้อง")
# elif score > 80:
#     print("excellent")
# elif score >= 50:
#     print("pass")
# elif score < 50:
#     print("fail")
# ราคาสินค้ารวม = int(input("ราคาสินค้า"))
# print(ราคาสินค้ารวม)
# if ราคาสินค้ารวม > 1000:
#     print("vip customer")
# elif ราคาสินค้ารวม > 500:
#     print("free gift")
# else:
#     print("ไปซื้อเพิ่ม")
# password = input("กรอกรหัส:")
# if len(password) < 6:
#     print("weak password")
# else:
#     print("strong password")
# awnser = int(input("what is 5+3"))
# if awnser == 8:
#     print("correct")
# else:
#     print("try agian")
# import random
# random_int = random.randint(1,10)
# guess = int(input("เลือกมาหนึ่งเลข(1-10)"))
# if guess == random_int:
#     print("you win")
# else:    
#     print(f"เลขสุ่ม: {random_int}")
# age = int(input("อายุเท่าไร"))
# if age > 18 and age < 60:
#     print("adult")
# elif age > 60:
#     print("senior")
# elif age < 18:
#     print("child")
# num = int(input("รับค่า"))
# if not (10 <=  num <= 50):
#     print("out of range")
# else: 
#     print("in range")
# score = 0
# for i in range(3):
#     num = int(input("กรอกตัวเลข: "))
#     score += num

# print("Final score:", score)
# correct_user = "tung tung"
# correct_pass = "sahur"
# attempts = 3

# while attempts > 0:
#     username = input("กรอกชื่อ: ")
#     password = input("กรอกรหัส: ")

#     if username == correct_user and password == correct_pass:
#         print("login success")
#         break
#     else:
#         attempts -= 1
#         print("wrong!Attempts left:",attempts)

# if attempts == 0:
#     print("accout locked")
# import random

# elements = ["water","fire","earth","wind"]

# user = input("Choose water,fire,earth or wind: ").lower()
# computer = random.choice(elements)

# print("computer chose:",computer)

# if user == computer:
#     print("draw")
# elif(user == "water" and computer == "fire") or\
#     (user == "fire" and computer == "earth") or\
#     (user == "earth" and computer == "wind") or\
#     (user == "wind" and computer == "water"):
#     print("you win")
# else:
#     print("you lose")
# import datetime

# hour = datetime.datetime.now().hour

# if 5 <= hour <=11:
#     print("good morning")
# elif 12 <= hour <= 17:
#     print("good afternoon")
# else:
#     print("good evening")
# total = float(input("ใส่ยอดเงินรวม: "))
# member = input("ใส่memberไหม? (yes/no): ").lower()
# if member == "yes" and total >= 500:
#      total *= 0.8
# elif member == "no" and total >= 500:
#      total *= 0.9

# print("Final price:",total)
# count = 0

# for i in range(5):
#     score = int(input("enter score: "))

#     if score >= 50:
#         count += 1

# print("you passed",count,"subjects")
# import random

# number = random.randint(1,5)
# attempts = 0

# while True:
#     guess = int(input("เลือกเลขละหว่าง(1-5): "))
#     attempts += 1

#     if guess == number:
#         print("Correct!Attemts:",attempts)
#         break
#     else:
#         print("try again")

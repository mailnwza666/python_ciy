
# def check_number():
#      if (number%2)==0:
#          print("นี่คือเลขคู่")
#      elif (number%2)==1:
#          print("นี่คือเลขคี่")
#      else:
#          print("คำสั่งผิด")

# number = float(input("รับตัวเลขเท่าไรดี"))
# check_number()

def greeting():
    if time<=23:
        print("good afternoon")
    elif time<12:
        print("good morning")
    else:
        print("ไม่ถูกต้อง")
time = int(input("รับค่าเวลา1-23"))
greeting()

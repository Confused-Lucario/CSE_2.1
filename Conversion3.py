my_num = 0
secret_num = 25
def number_eval():
    if my_num > secret_num:
            print("too large, change your number")
    elif my_num < secret_num:
            print("too small, change your number")
    else:
            print("numbers are equal")

while (my_num != secret_num):
    my_num = int(input("enter a number between 1-100"))
    number_eval()
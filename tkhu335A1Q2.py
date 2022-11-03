
import random
prompt1 = input("Enter 3 numbers separated by a comma: ")
line1 = prompt1.find(",")
number1 = prompt1[:line1]
prompt2 = prompt1[line1+1:]
line2 = prompt2.find(",")
number2 = prompt2[:line2]
number3 = prompt2[line2+1:]
number1 = int(number1)
number2 = int(number2)
number3 = int(number3)
large_num = max(number1, number2, number3)
dice_throw = random.randrange(1, large_num)

print("Largest number is",large_num)
print("Dice throw is",dice_throw)


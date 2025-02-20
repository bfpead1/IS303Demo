# Toa Pita
# Section 42
# 2/17/2025
# Description: Take input for two numbers.
# Check if the sum of those numbers is the same as their product
from addition import addTwoNumbers
from multiply import multiplyTwoNumbers
iFirstNum = int(input("Please enter a whole number: "))
iSecondNum = int(input("Please enter another whole number: "))
if(addTwoNumbers(iFirstNum,iSecondNum)==multiplyTwoNumbers(iFirstNum,iSecondNum)):
    print("The sum and product are the same")
else:
    print("The sum and product are different")
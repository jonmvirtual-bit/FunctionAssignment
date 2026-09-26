import math

# For the taxes function, the taxRate percentage has to be inputted as a decimal number. #
# (e.g. if you want 6% as the tax rate, you'll have to enter "0.06") #
def main():
    valueInp = int(input("Enter a number for the radius: "))
    value = circleArea(valueInp)
    print("%.2f" % value)
    valuetwoMoneyInp = int(input("Enter a number for the money: "))
    valuetwoTaxInp = float(input("Enter a decimal for the tax rate: "))
    valuetwo = taxFunction(valuetwoMoneyInp, valuetwoTaxInp)
    print("%.2f" % valuetwo)
    valuethreeInp = int(input("Enter a number for the Fahrenheit: "))
    valuethree = temperature(valuethreeInp)
    print("%.4f" % valuethree)

# For the circle function. #
def circleArea(radius):
    area = 3.14159 * (radius ** 2)
    return area

# For the tax function. #
def taxFunction(money, taxRate):
    totaldue = money + (money * taxRate)
    return totaldue

# For the temperature function. #
def temperature(fahrenheit):
    celsius = (fahrenheit - 32) * (5 / 9)
    return celsius


main()
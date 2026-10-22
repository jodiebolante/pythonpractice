#Set 1: Basics and data types
#1a
name = input("What's your name? ")
birthYear = int(input("What's your birth year? "))
age = 2026 - birthYear
print(f"Hi {name}, you will turn {age} in 2026.")
print("=" * 40)
#1b
s = "Python Programming"
print(len(s))
print(s.upper())
print(s[:6])
print(s[-11:])
print(s[::-1])
print(s.count('g'))
#1c
price = float(input("Give a price: "))
qty = int(input("Give a Quantity: "))
total = price * qty
print(f"Total: P{total:,.2f}")
#Set 2: Operators
#2a
a = 17 
b = 5
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print (a ** b)
#2b
n = 12
print(n % 2 == 0 and 10 <= n <= 50)


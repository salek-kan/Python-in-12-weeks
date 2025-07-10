#!/usr/bin/python3
"""This program reads user input and prints out a summary"""
name: str = input("What is your name?\n")
Age: int = int(input("How old are you?\n"))
Balance: float = float(input("How much do you currently have?\n"))
is_subscribed: bool = bool(input("Are you subscribed? (skip if not)\n"))

print("\n" * 4)
print(f"\tHi {name.capitalize():s},")
print(f"\tYour current balance is : ${Balance:>5.2f}")
print(f"\tSubscribtion : {is_subscribed:>12b}")

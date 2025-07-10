#!/usr/bin/python3
"""This is a simple script that prints various data types"""
name: str = "Ahmed"
Age: int = 43
Balance: float = 315.00
is_subscribed: bool = False

print(f"Hi {name:s},")
print(f"Your current balance is : ${Balance:>5.2f}")
print(f"Subscribtion : {is_subscribed:>12b}")

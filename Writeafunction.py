"""
Title     : Write a function
Subdomain : Introduction
Domain    : Python
Author    : Merve Gamze Cinar
Created   : 14 March 2023
Problem   : https://www.hackerrank.com/challenges/write-a-function/problem
"""


def is_leap(year):
    leap = False
    leap = (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)
    return leap


year = int(input())
print(is_leap(year))
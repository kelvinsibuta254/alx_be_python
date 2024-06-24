#!/bin/bash
#student = input("are you a student? ")
high_income = False
good_credit = True
student = True

#if not student:
if high_income or good_credit and not student:
    print("Eligible")
else:
    print("Not eligible")

#Short circuit: Evaluation stops as long as one of these arguments evaluates to False.
#In python logical operators are short circuits

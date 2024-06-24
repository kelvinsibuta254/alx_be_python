#!/bin/bash
age = int(input("How Old are you?"))
#if age >= 18:
 #   message = "Eligible"
#else:
 #   message = "Not eligible"

message = "Eligible" if age >= 18 else "Not eligible" #assign a valu# e to the message variable. This is called ternary operator
print(message)


#same as the code below
#age = 12
#message = "Eligible" if age >= 18 else "Not eligible"
#print(message)

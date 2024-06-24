#!/bin/bash
temperature = int(input("Enter the temperature value: "))
if temperature > 30:
    print("It's warm")
    print("Drink water")
elif temperature > 20:#You can have as many elif statements as possible
    print("It's nice")

else:#if all the other conditions are not True this code block will be executed
    print("It's cold")

print("Done") #executed whether the conditions are True or not
#pepp eight automatically uses four white spaces after saving the file

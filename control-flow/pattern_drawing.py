#!/bun/bash
rows = int(input("Enter the size of the pattern"))
i = 0
while i <= 4:
    for i in range(1, 5):
        j = 0
        while j <= 4:
            for j in range(1, 5):
                print("*", end="")
                j += 1
            i += 1
        print()

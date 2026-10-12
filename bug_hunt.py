count = 1
total = 0

# BUG: The while loop header was missing a colon, which caused the program to fail before it could run. I added the missing colon.
while count <= 5:
    # BUG: The loop condition used < 5, which stopped before reaching 5 and skipped the final value. I changed it to <= 5.
    total = total + count
    count = count + 1

# BUG: The print statement tried to join a string and an integer, which caused a type error. I converted total to a string before printing.
print("Sum of 1 to 5 is: " + str(total))

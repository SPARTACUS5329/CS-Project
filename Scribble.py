x = int(input("Enter a number: "))
y = int(input("Enter another number: "))
print("Choose the option")
print("1.Arithmetic operator")
print("2.Logical operator")
print("3.Comparison operator")
choice = input("Your choice: ")

if choice == "1":
    print(f"{x+y} if their sum")
    print(f"{x-y} if their diff")
    print(f"{x*y} if their prod")
    print(f"{x/y} if their quotient")
elif choice == "2":
    if x+y == 10 or x-y==5:
        print("the sum is 10 or the diff is 5")
    else:
        print("neither the sum is 10 nor the diff is 5")
elif choice == "3":
    if x>y:
        print(f"{x} if greater than {y}")
    elif y>x:
        print(f"{y} if greater than {x}")
    else:
        print("Both are equal")
else:
    print("Enter a valid option")

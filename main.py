def numbers_by_condition1(min=11, max=80):
    for i in range(min, max):
        if i % 5 == 0 and i % 3 == 0:
            print("$$@@")
        elif i % 5 == 0:
            print("@@")
        elif i % 3 == 0:
            print("$$")
        else:
            print(i)


def numbers_by_condition2(min=11, max=80):
    for i in range(min, max):
        print("$$" * (not i % 3) + "@@" * (not i % 5) or i)

print("First option:")
numbers_by_condition1()
print("\nSecond option:")
numbers_by_condition2()

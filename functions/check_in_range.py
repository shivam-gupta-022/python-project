#Python function to check whether a number falls in a given range
def test_range(n):
    if n in range(1,50):
        print( n,"is in the range")
    else :
        print("The number is outside the given range.")

n=int(input("Enter the number to be checked: "))
test_range(n)

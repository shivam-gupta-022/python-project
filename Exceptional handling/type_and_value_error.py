
def compute_division():
    dividend = int(input("Enter the dividend: ")) # cast string to int  #5 |= for type ||   #3a for value error
    divisor = input("Enter the divisor: ") # no casting                 #3 |= error    ||
 
    # Compute division
    result = dividend/divisor
 
    # print result
    print("The result of {}/{} is: {}".format(dividend, divisor, result))
 
if __name__ == '__main__':
    result = compute_division()

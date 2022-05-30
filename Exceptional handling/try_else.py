def  fraction_of_one(divisor):
    value = 1/divisor # if divisor is zero, ZeroDivisionError will be raised
    return value
 
if __name__ == '__main__':
    while True:
        try:
            # if input is not a valid argument for int(), ValueError will be raised
            divisor = int(input("Enter a divisor: "))   
            # call our function to compute the fraction
            value = fraction_of_one(divisor)
        except (ValueError, ZeroDivisionError):
            print("Input can't be zero and should be a valid literal for int(). Please, try again!")
        else:
            print("Value: ", value)
            break

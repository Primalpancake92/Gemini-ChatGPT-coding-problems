def divisor(random_number: float):
    division = 10 / random_number
    
    return division


def main():    
    try:
        number = int(input("What is the number you would like to divide 10 by? "))
        
        
        if not (isinstance(number, int) or isinstance(number, float)):
            raise ValueError("The number can only be a float or integer value.")
        
        if number == 0:
            raise ZeroDivisionError("The number cannot be zero.")
        
        something = divisor(number)
        
        print(something)
        
    except ValueError as e:
        print(f"ValueError: {e}")
    except ZeroDivisionError as f:
        print(f"ZeroDivisionError: {f}")
        

if __name__ == "__main__":
    main()
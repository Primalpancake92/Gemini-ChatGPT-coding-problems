def divide_numbers(a: int, b: int) -> int:
    try:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Both inputs must be numbers!")
        
        division = a / b
        
        return division

    except ZeroDivisionError:
        print("Cannot divide number by zero!")
        return None
    except TypeError as e:
        print(e)
        return None
    
if __name__ == "__main__":
    print(divide_numbers(10, 5))
    print(divide_numbers(10, "1"))
    print(divide_numbers(10, 0))
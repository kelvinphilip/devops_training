def get_square(x:int) -> dict:
    number = 0
    status = True
    try:
        number = int(x)
    except Exception as e:
        status = False
    finally:
        if isinstance(number, int):
            squarenumber = (number ** 2)
        else:
            squarenumber = 0
        if squarenumber:
            print(f"Number={number}; Square={squarenumber}")
        else:
            print("Invalid input received; please try again")
        return {'status': status, 'result': squarenumber}

if __name__ == "__main__":
    result1 = get_square(x=2)
    print(f"Request1::{result1}")

    result2 = get_square(x=3)
    print(f"Request2::{result2}")

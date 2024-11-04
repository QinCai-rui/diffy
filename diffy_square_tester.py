from sys import exit

def diffy_squares(a, b, c, d):
    counter = 0
    print(f"Round {counter}: ({a}, {b}, {c}, {d})")
    while not (a == 0 and b == 0 and c == 0 and d == 0):
        a, b, c, d = abs(a - b), abs(b - c), abs(c - d), abs(d - a)
        print(f"Round {counter + 1}: ({a}, {b}, {c}, {d})")
        counter += 1
    return counter

    
def numbers_response():
    # Input the four numbers to be tested
    a, b, c, d = map(float, input("\nEnter four numbers separated by spaces (CTRL+C to quit): ").split())

    # Calculate the number of rounds
    rounds = diffy_squares(a, b, c, d)

    # Print the result
    print(f"The four numbers ({a}, {b}, {c}, {d}) last for {rounds} rounds.")

if __name__ == "__main__":
    while True:
        try:
            numbers_response()
        except KeyboardInterrupt:
            print("\nYou pressed CTRL+C. EXITING...")
            exit(0)
        except ValueError as ve:
            print("\nInvalid input. Make sure you are entering *4 NUMBERS*!!")
            print(f"ERROR: {ve}")
        except Exception as e:
            print("\nAn unknown error occured")
            print(f"ERROR: {e}")

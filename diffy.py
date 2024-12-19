from sys import exit

# Function for counting Diffy levels
def diffy_squares(a, b, c, d):
    counter = 0
    while not (a == 0 and b == 0 and c == 0 and d == 0):
        a, b, c, d = abs(a - b), abs(b - c), abs(c - d), abs(d - a)
        counter += 1
    return counter

# The logic of "trial-and-error" Diffy Squares to find the biggest score
def find_max_score(lower_range_limit, upper_range_limit):
    max_score = 0
    max_values = (0, 0, 0, 0)
    
    for a in range(lower_range_limit, upper_range_limit):
        for b in range(lower_range_limit, upper_range_limit):
            for c in range(lower_range_limit, upper_range_limit):
                for d in range(lower_range_limit, upper_range_limit):
                    score = diffy_squares(a, b, c, d)
                    if score > max_score:
                        max_score = score
                        max_values = (a, b, c, d)
                        print(f"New max score: {max_score} with values: {max_values}")

    return max_score, max_values

# Program main logic, of course
def main():
    print("You will be asked for the number range being used.")
    print("Please enter a small range to start with, as this code takes a bit time to run.")
    print("(A range of about 500 is good to start with!)")
    
    lower_range_limit = int(input("\nEnter the minimum number the program may use: "))
    upper_range_limit = int(input("\nAnd now, enter the maximum number the program may use: "))
    
    max_score, max_values = find_max_score(lower_range_limit, upper_range_limit + 1)
    print(f"Max score using numbers {lower_range_limit} to {upper_range_limit}: {max_score} with values: {max_values}")


# TRY-EXCEPT logic for error detection
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nYou pressed CTRL+C. EXITING...")
        exit(0)
    except ValueError as ve:
        print("\nInvalid input. Make sure you are entering *INTEGERS*!!")
        print(f"ERROR: {ve}")
    except Exception as e:
        print("\nAn unknown error occurred")
        print(f"ERROR: {e}")

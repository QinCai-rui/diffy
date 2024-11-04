def diffy_squares(a, b, c, d):
    counter = 0
    while not (a == 0 and b == 0 and c == 0 and d == 0):
        a, b, c, d = abs(a - b), abs(b - c), abs(c - d), abs(d - a)
        counter += 1
    return counter

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

# Set a limit for the range of initial values
lower_range_limit = 0
upper_range_limit = 100000

max_score, max_values = find_max_score(lower_range_limit, upper_range_limit + 1)
print(f"Max score using numbers {lower_range_limit} to {upper_range_limit}: {max_score} with values: {max_values}")

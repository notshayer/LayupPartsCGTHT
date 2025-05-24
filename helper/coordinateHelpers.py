import random

def generate_random_point(x_range=(0, 100), y_range=(0, 100)):
    return (random.randint(*x_range), random.randint(*y_range))

def generate_random_line_segments(n=20):
    return [[generate_random_point(), generate_random_point()] for _ in range(n)]

# This function takes two line segments and checks if their x-ranges overlap: returns T or F
def checkXOverlap(line1, line2, this_range):
    # Extract x-coordinates
    range1 = [line1[0][0], line1[1][0]]
    range2 = [line2[0][0], line2[1][0]]
    
    # Sort x-values so min and max are in order
    min1, max1 = sorted(range1)
    min2, max2 = sorted(range2)

    # Find overlap range
    start = max(min1, min2)
    end = min(max1, max2)
    
    # assign the range values to the referenced range array if range exists
    if start <= end:
        this_range.append(start)
        this_range.append(end)
        return True
    else:
        return False

# Example usage:
if __name__=="__main__":
    line_segments = generate_random_line_segments(20)
    print("list =", line_segments)

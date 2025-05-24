import random

def generate_random_point(x_range=(0, 100), y_range=(0, 100)):
    return (random.randint(*x_range), random.randint(*y_range))

def generate_random_line_segments(n=20):
    return [[generate_random_point(), generate_random_point()] for _ in range(n)]

# Example usage:
if __name__=="__main__":
    line_segments = generate_random_line_segments(20)
    print("list =", line_segments)

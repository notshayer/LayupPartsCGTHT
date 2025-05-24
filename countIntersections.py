# helper folder contains line segment generation functions + visualization tools
from helper.coordinateHelpers import generate_random_line_segments, checkXOverlap

# generate 20 random segments, in the format specified in the test document
# ex: lines = [[(0, 53), (19, 73)], [(41, 84), (79, 30)], [(66, 24), (89, 9)], ...]
line_segments = generate_random_line_segments(10)
print("list = \n")
print(line_segments)
# we convert the segments into their linear equation forms, y = mx + b
# where m is the slope, x is the x coordinate, and b is the intercept
segment_slopes    = [] 
segment_intercepts = []

for line in line_segments:
    # break up data into coordinatese
    start_coord = line[0]
    end_coord   = line[1]
    # get values to follow slope = (y2-y1)/(x2-x1)
    x1 = start_coord[0]
    y1 = start_coord[1]
    x2 = end_coord[0]
    y2 = end_coord[1]
    # calculate slope
    slope = (y2-y1)/(x2-x1)
    intercept = y2 - (slope*x2)
    segment_slopes.append(slope)
    segment_intercepts.append(intercept)

# check every line segment against the line segments after it.
# each iteration only checks the segments that come after it to prevent repeat calculations.
counter = 0
for idx in range(len(line_segments)):
    for idy in range(idx + 1,len(line_segments)):
        line1 = line_segments[idx]
        line2 = line_segments[idy]
        this_range = []
        if checkXOverlap(line1, line2, this_range) == True:
            # X_intersect = (intercept2 - intercept1) / (slope1 - slope2)
            intercept1 = segment_intercepts[idx]
            intercept2 = segment_intercepts[idy]
            slope1     = segment_slopes[idx]
            slope2     = segment_slopes[idy]
            x_intersect = (intercept2 - intercept1) / (slope1 - slope2)
            # We count contact as intersect 
            if x_intersect <= this_range[1] and x_intersect >= this_range[0]:
                counter += 1

print(counter)



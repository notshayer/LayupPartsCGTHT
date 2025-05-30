# Overview
- The script uses randomly generated line segments, so the answer for every run will be different.
    - Functions like this were moved to helper to prevent script bloat.
- Solution is Time Complexity: O(n^2) and Storage Complexity: O(n), but a lower time complexity solution is possible using R-Trees
    - Using a R-Tree would require more code to be written or the use of more external modules, so I opted for the simplest solution to ensure script could easily be run without any installs (other than python.).
    - Additionally, this solution helps with readability as we use equations from simple algebra in an easy to follow order.
- (Optional) Use `requirements.txt` to install matplotlib and also get visual aide used to verify solution (optional)
    - `pip install requirements.txt` (might be `pip3` depending on install)

# Edge Cases Considered:
- Endpoint Collision - counts as intersection
- Vertical Segments (Division by Zero) - error handling to prevent crash + offset in processing loop
- Parallel Lines - No Intersection

# Run Instructions:
- Clone repo and `python countIntersections.py` or `python3 countIntersections.py`

# Example Visualization
![Alt Text](example.png)

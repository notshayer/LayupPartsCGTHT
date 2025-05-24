import matplotlib.pyplot as plt
# Plotting function that returns fig and ax
def plot_segments(segments, counter):
    fig, ax = plt.subplots(figsize=(10, 8))
    for i, seg in enumerate(segments):
        x_vals = [seg[0][0], seg[1][0]]
        y_vals = [seg[0][1], seg[1][1]]
        ax.plot(x_vals, y_vals, marker='o', label=f'Line {i+1}')
    
    ax.set_title('Line Segments - Intersection Count: {}'.format(counter))
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.grid(True)
    ax.legend()
    ax.set_aspect('equal')
    return fig, ax
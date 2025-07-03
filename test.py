import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Helper to add dimension arrows
def add_dimension(ax, start, end, text, offset=5, vertical=False):
    if vertical:
        ax.annotate('', xy=start, xytext=end, arrowprops=dict(arrowstyle='<->'))
        x = start[0] + offset
        y = (start[1] + end[1]) / 2
        ax.text(x, y, text, va='center', ha='left', fontsize=8)
    else:
        ax.annotate('', xy=start, xytext=end, arrowprops=dict(arrowstyle='<->'))
        x = (start[0] + end[0]) / 2
        y = start[1] + offset
        ax.text(x, y, text, va='bottom', ha='center', fontsize=8)

# Create technical drawing
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(-10, 220)
ax.set_ylim(-10, 100)
ax.set_aspect('equal')
ax.set_title("Capstan Drive Parts – Technical Overview with Dimensions", fontsize=10)

# Draw small drum
small_drum = patches.Circle((10, 20), 10, fill=False, label='Small Drum')
ax.add_patch(small_drum)
add_dimension(ax, (0, 5), (20, 5), '20 mm Ø')
add_dimension(ax, (20, 15), (20, 30), '15 mm', vertical=True)

# Draw large drum
large_drum = patches.Circle((60, 20), 85, fill=False, label='Large Drum')
ax.add_patch(large_drum)
add_dimension(ax, (-25, 20), (145, 20), '170 mm Ø')
add_dimension(ax, (145, 15), (145, 30), '15 mm', vertical=True)

# Frame base
frame = patches.Rectangle((110, 0), 200, 80, fill=False, label='Frame Base')
ax.add_patch(frame)
add_dimension(ax, (110, -5), (310, -5), '200 mm')
add_dimension(ax, (305, 0), (305, 80), '80 mm', vertical=True)
add_dimension(ax, (110, 85), (115, 85), '5 mm', vertical=True)

# Motor mount
motor_mount = patches.Rectangle((70, 60), 40, 40, fill=False, label='Motor Mount')
ax.add_patch(motor_mount)
add_dimension(ax, (70, 105), (110, 105), '40 mm')
add_dimension(ax, (115, 60), (115, 100), '40 mm', vertical=True)

# Tensioner
tensioner = patches.Rectangle((30, 60), 20, 20, fill=False, label='Tensioner Block')
ax.add_patch(tensioner)
add_dimension(ax, (30, 85), (50, 85), '20 mm')
add_dimension(ax, (55, 60), (55, 80), '10 mm', vertical=True)

# Hide axes
ax.axis('off')

# Save image
image_path = "/mnt/data/capstan_drive_dimensions.png"
plt.savefig(image_path, dpi=300, bbox_inches='tight')
plt.close()

image_path

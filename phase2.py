import cv2
import os
import time
import subprocess

cell_folder = "cells"
screenshot_path = "samples/temp.png"
coord_file = "samples/crop_coords.txt"

os.makedirs("samples", exist_ok=True)
os.makedirs(cell_folder, exist_ok=True)

# --- STEP 1: Take one full-screen screenshot ---
print("📸 Taking initial screenshot for region selection...")
subprocess.run(["gnome-screenshot", "-f", screenshot_path])
time.sleep(0.5)

# --- STEP 2: Let user select crop region interactively ---
image = cv2.imread(screenshot_path)
clone = image.copy()
coords = []

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        coords.append((x, y))
        cv2.circle(clone, (x, y), 5, (0, 255, 0), -1)
        cv2.imshow("Select Region (Top-Left, Bottom-Right)", clone)

print("🖱️ Select top-left and bottom-right corners of board...")
cv2.namedWindow("Select Region (Top-Left, Bottom-Right)", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Select Region (Top-Left, Bottom-Right)", 1280, 720)
cv2.imshow("Select Region (Top-Left, Bottom-Right)", clone)

cv2.setMouseCallback("Select Region (Top-Left, Bottom-Right)", click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()

if len(coords) != 2:
    print("❌ Error: Please click exactly 2 points.")
    exit(1)

(x1, y1), (x2, y2) = coords
x1, x2 = sorted([x1, x2])
y1, y2 = sorted([y1, y2])

# Save to file
with open(coord_file, "w") as f:
    f.write(f"{x1} {y1} {x2} {y2}")

print(f"✅ Coordinates saved to {coord_file}: ({x1},{y1}) to ({x2},{y2})")

# --- STEP 3: Loop – Repeatedly capture and crop ---
while True:
    print("📸 Taking live screenshot...")
    subprocess.run(["gnome-screenshot", "-f", screenshot_path])
    time.sleep(0.3)

    image = cv2.imread(screenshot_path)
    if image is None:
        print("❌ Failed to load screenshot.")
        continue

    # Crop and resize
    board = image[y1:y2, x1:x2]
    board = cv2.resize(board, (800, 800))
    cv2.imwrite("cropped_board.jpg", board)

    # Delete old cells
    for f in os.listdir(cell_folder):
        os.remove(os.path.join(cell_folder, f))

    # Split into 64 cells
    h, w = board.shape[:2]
    cell_size = w // 8

    for row in range(8):
        for col in range(8):
            x = col * cell_size
            y = row * cell_size
            cell = board[y:y+cell_size, x:x+cell_size]
            filename = f"{cell_folder}/cell_{row}_{col}.jpg"
            cv2.imwrite(filename, cell)

    print("✅ 64 cells updated.")
    time.sleep(2)

from board_to_fen.predict import get_fen_from_image
from PIL import Image

image_path = "./cropped_board.jpg"
image = Image.open(image_path)

fen = get_fen_from_image(image)
print("FEN:", fen)

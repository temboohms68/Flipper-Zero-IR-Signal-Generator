from PIL import Image
import os

try:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    save_path = os.path.join(current_dir, 'icon.png')
    img = Image.new('1', (10, 10), color=0)
    img.save(save_path)
    print(f"Icon generated successfully at {save_path}")
except ImportError:
    print("PIL not found")
except Exception as e:
    print(f"Error: {e}")

import pywhatkit.whats as kit
from dotenv import load_dotenv
import os

image_folder_path = '/Users/fabianarnold/projects/oma_whatsapp/images/'

def process_number(number: str | None) -> str:
    if number is None:
        raise ValueError("Value of number was None")
    return number

load_dotenv()

oma_number = os.getenv("OMA_NUMBER")
oma_number = process_number(oma_number)

images = [image_folder_path + f for f in os.listdir(image_folder_path) if f.endswith('.jpg')]

kit.sendwhats_image(oma_number, images[0], "Guten Morgen!", 7, True, 1)

os.remove(images[0])

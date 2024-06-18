from PIL import Image, ImageEnhance, ImageFilter
import os

path = './imgs'
path_out = '/editedImgs'

for filename in os.listdir(path):
    img = Image.open (f"{path} / {filename}")
    
    #Customizable edit here (Look at the Pillow Library Docs):
    edit = img.filter(ImageFilter.SHARPEN).convert('L').rotate(-90)
    
    factor = 1.5
    enhancer = ImageEnhance.Contrast(edit)
    edit = enhancer.enhance(factor)
    
    clean_name = os.path.splitext(filename)[0]
    
    edit.save(f'.{path_out}/{clean_name}_edited.jpg')
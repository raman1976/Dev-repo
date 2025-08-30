from PIL import Image, ImageDraw

def create_image(file_path, expression):
    img = Image.new('RGB', (100, 100), color = 'white')
    draw = ImageDraw.Draw(img)

    # Face
    draw.ellipse((10, 10, 90, 90), fill='yellow', outline='black')
    # Eyes
    draw.ellipse((30, 30, 40, 40), fill='black')
    draw.ellipse((60, 30, 70, 40), fill='black')
    # Nose
    draw.polygon([(50, 50), (45, 60), (55, 60)], fill='black')

    if expression == 'happy':
        # Smile
        draw.arc((30, 40, 70, 80), 0, 180, fill='black', width=2)
    elif expression == 'sad':
        # Frown
        draw.arc((30, 60, 70, 90), 180, 360, fill='black', width=2)

    img.save(file_path)

if __name__ == '__main__':
    create_image('pokemon_pet/happy.png', 'happy')
    create_image('pokemon_pet/sad.png', 'sad')
    create_image('pokemon_pet/neutral.png', 'neutral')
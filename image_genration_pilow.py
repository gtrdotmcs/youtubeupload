from PIL import Image, ImageDraw, ImageFont

# Create a new blank image
img = Image.new('RGB', (600, 400), color = (73, 109, 137))

# Get a drawing context
d = ImageDraw.Draw(img)

# Add text
try:
    # Try to load a common font, or specify a path to one on your system
    fnt = ImageFont.truetype("arial.ttf", 40)
except IOError:
    fnt = ImageFont.load_default() # Fallback to default font

d.text((10,10), "Hello, World!", font=fnt, fill=(255, 255, 0))

# Save the image
img.save("hello_world.png")
print("Image 'hello_world.png' created.")
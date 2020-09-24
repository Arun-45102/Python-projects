from PIL import Image, ImageFilter

img = Image.open("./images/astro.jpg")
# Filter Image
# filter_img = img.filter(ImageFilter.BLUR)

# Convert Image
# convert_img = img.convert("L")

# Rotate Image
# rotated_image = filter_img.rotate(270)

# Resize Image
# resize_image = img.resize((320, 320))

# Crop Image
# crop_size = (100, 100, 400, 400)
# crop_image = img.crop(crop_size)

# Thumbnail Image
img.thumbnail((400, 400))
img.save("edited_image/pikachu_thumbnail.png", "png")

# Save Image
# crop_image.save("edited_image/pikachu_crop.png", "png")
# crop_image.show()



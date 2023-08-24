from PIL import Image

# Open the two images
image1 = Image.open("image1.jpg")
image2 = Image.open("image2.jpg")

# Specify the position (x, y) to place image1 on image2
x = 0
y = 0

# Paste image1 onto image2 at the specified position
image2.paste(image1, (x, y))

# Save the resulting image as a new file
image2.save("result.jpg")

# Make the image downloadable
# For this you will need to run your code on server 
# or use any other method to make the image downloadable

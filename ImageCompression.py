import os
from PIL import Image

# 'Flicker8k_Dataset' folder should contain your dataset
rootdir = os.getcwd() + "/Flicker8k_Dataset"

# Stores the commpressed images in the 'Compressed_Datset' folder 
os.rmdir("Compressed_Dataset")
os.makedirs("Compressed_Dataset")

num = 0
maxHeight, maxWidth = 200, 200
for subdir, dirs, files in os.walk(rootdir):
	for file in files:
		num+=1
		print(num)
		image = Image.open(os.path.join(subdir, file))
		image.thumbnail((maxHeight, maxWidth))
		image.save("Compressed_Dataset/" + str(num) + ".jpg")
from PIL import Image, ImageEnhance

image_path = 'pesca_a_dor/assets/images/fish.PNG'
image = Image.open(image_path)

# increase contrast (+50%)
#enhancer = ImageEnhance.Contrast(image)
#image = enhancer.enhance(1.5)

# convert image to grayscale
image = image.convert('L')

# binarize image using the global thresholding method
threshold=127
image = image.point(lambda x: 0 if x < threshold else 255, '1')

# save image with increased contrast
new_image_path = 'pesca_a_dor/assets/images/fish_bin.PNG'
image.save(new_image_path)
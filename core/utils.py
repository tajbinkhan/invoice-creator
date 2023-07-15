from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile

def optimize_image(image, height, width):
	if image:
		if not hasattr(image, 'file') or not hasattr(image.file, 'content_type'):
			return image

		if 'image' not in image.file.content_type:
			return image

		img = Image.open(image)
		max_size = (height, width)
		img.thumbnail(max_size)

		# Convert the image to WebP format
		output = BytesIO()
		img.save(output, format='WebP', quality=80)
		output.seek(0)

		if image.file:
			image.file.close()

		# Create a ContentFile with the converted image data
		converted_image = ContentFile(output.read())

		# Assign the converted image to the original image field
		image.save(f"{image.name.split('.')[0]}.webp", converted_image, save=False)

	return image

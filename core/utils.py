from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile

def optimize_image(image, height, width):
	if image:
		if not hasattr(image, 'file') or not hasattr(image.file, 'content_type'):
			return image
		if 'image' not in image.file.content_type:
			return image

		img = Image.open(image)
		max_size = (height, width)
		img.thumbnail(max_size)
		output = BytesIO()
		img.save(output, format='PNG', optimize=True)

		output.seek(0)

		if image.file:
			image.file.close()

		image.file = InMemoryUploadedFile(
			output,
			'ImageField',
			"%s.png" % image.name.split('.')[0],
			'image/png',
			output.tell,
			None
		)
		image._committed = False
	return image
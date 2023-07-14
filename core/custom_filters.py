import locale
from django import template

register = template.Library()
locale.setlocale(locale.LC_ALL, 'bn_BD')

@register.filter
def comma_format(value):
	# Convert SafeString to string
	value_str = str(value)

	# Remove any unwanted characters, such as HTML tags, if present
	value_str = value_str.strip('<>')

	# Check if value contains a decimal point
	if '.' in value_str:
		whole_part, decimal_part = value_str.split('.')
		decimal_places = min(len(decimal_part), 2)
	else:
		whole_part = value_str
		decimal_places = 0

	# Add two zeros if there is no decimal part
	if decimal_places == 0 or decimal_places <=1:
		formatted_number = locale.format_string("%.2f", float(whole_part), grouping=True)
	else:
		formatted_number = locale.format_string(f"%.{decimal_places}f", float(value_str), grouping=True)

	return formatted_number

@register.filter
def custom_total(value):
	# Convert SafeString to string
	value_str = str(value)

	# Remove any unwanted characters, such as HTML tags, if present
	value_str = value_str.strip('<>')

	# Check if value contains a decimal point
	if '.' in value_str:
		whole_part, decimal_part = value_str.split('.')
		decimal_places = len(decimal_part)
	else:
		whole_part = value_str
		decimal_places = 0

	# Add two zeros if there is no decimal part
	if decimal_places == 0 or decimal_places <=1:
		formatted_number = locale.format_string("%.2f", float(whole_part), grouping=True)
	else:
		formatted_number = locale.format_string(f"%.{decimal_places}f", float(value_str), grouping=True)

	return formatted_number

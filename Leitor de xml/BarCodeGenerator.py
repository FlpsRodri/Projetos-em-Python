from barcode import EAN13
from barcode.writer import ImageWriter

# Set the barcode value
barcode_value = "756233759083"

# Generate the barcode
barcode = EAN13(barcode_value, writer=ImageWriter())

# Save the barcode image to a file
barcode.save("barcode.png")

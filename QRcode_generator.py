import qrcode  # qrcode library

value = input("Enter the value to be encoded in QRcode: ")
# Taking the value to be encoded in QRcode

img = qrcode.make(value)
# Creating the QRcode

folder = input(
    "Enter the folder full address where the QRcode will be stored: ")
name = input("Enter the name of the file: ")
ext = input("Enter the extension of the file: ")
# Taking the location, name and extension of the file

img.save(f"{folder}{name}.{ext}")
# Saving the QRcode in the specified location
# /home/dnischal11/Downloads/ is the path where the QRcode is saved.
# you can change the path according to your system.

print(f"QRcode is generated and saved in the location : {folder}{name}.{ext}")
# Printing the location of the QRcode where it is saved.

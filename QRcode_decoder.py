from pyzbar.pyzbar import decode
# pyzbar is a library for decoding barcodes in images
# to run the program you need to install pyzbar
# Goto the terminal and type: pip install pyzbar to install it
from PIL import Image
# PIL is a Python Imaging Library
# to run the program you need to install PIL
# Goto the terminal and type: pip install pillow to install it

location = input("Enter the location of the QRcode: ")
# taking the location of the QRcode
img = Image.open(location)
# opening the QRcode

result = decode(img)
# decoding the QRcode

print(f"The Qrcode contains this data : {result[0].data.decode('utf-8')}")
# printing the data in the QRcode
# while printing result only, it prints out result as array which contains all the details of the QRcode
# the data in the QRcode is presented like this:
#[Decoded(data=b'nischal Dhakal', type='QRCODE', rect=Rect(left=40, top=40, width=210, height=210), polygon=[Point(x=40, y=40), Point(x=40, y=250), Point(x=250, y=250), Point(x=250, y=40)], quality=1, orientation='UP')]
# the first element of the array is the data in the QRcode which is the data that is encoded in the QRcode
# to get the data in the result, we use .data function and decode it to human readable format using .decode('utf-8') function
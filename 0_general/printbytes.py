
import struct

TYPE_SIZE = 2
SIZE_SIZE = 4
RESERVED_1_SIZE = 2
RESERVED_2_SIZE = 2
OFFSET_SIZE = 4
DBI_H_SIZE_SIZE = 4
WIDTH_SIZE = 4
HEIGHT_SIZE = 4
COLORPLANES_SIZE=2
BITS_PER_PIXEL_SIZE = 2
COMPRESSION_METHOD_SIZE = 4
RAW_IMAGE_SIZE = 4


total = TYPE_SIZE + SIZE_SIZE + RESERVED_1_SIZE + RESERVED_2_SIZE + OFFSET_SIZE + DBI_H_SIZE_SIZE + WIDTH_SIZE + HEIGHT_SIZE + COLORPLANES_SIZE + BITS_PER_PIXEL_SIZE + COMPRESSION_METHOD_SIZE + RAW_IMAGE_SIZE

# print(total)
#
bmp = open("20x20_rojo.bmp", 'rb')
# print('Type:', bmp.read(2).decode())
# size = struct.unpack('I', bmp.read(4))[0]
# print('Size: %s' % size)
# print('Reserved 1: %s' % struct.unpack('H', bmp.read(2)))
# print('Reserved 2: %s' % struct.unpack('H', bmp.read(2)))
# offset = struct.unpack('I', bmp.read(4))[0]
# print('Offset: %s' % offset)
# print('DIB Header Size: %s' % struct.unpack('I', bmp.read(4)))
# print('Width: %s' % struct.unpack('I', bmp.read(4)))
# print('Height: %s' % struct.unpack('I', bmp.read(4)))
# print('Colour Planes: %s' % struct.unpack('H', bmp.read(2)))
# print('Bits per Pixel: %s' % struct.unpack('H', bmp.read(2)))
# print('Compression Method: %s' % struct.unpack('I', bmp.read(4)))
# print('Raw Image Size: %s' % struct.unpack('I', bmp.read(4)))
# print('Horizontal Resolution: %s' % struct.unpack('I', bmp.read(4)))
# print('Vertical Resolution: %s' % struct.unpack('I', bmp.read(4)))
# print('Number of Colours: %s' % struct.unpack('I', bmp.read(4)))
# print('Important Colours: %s' % struct.unpack('I', bmp.read(4)))
# bmp.read(offset - total); # offset menos leido..

data = bmp.read()
OUT = ""
for x in data:
   OUT+= hex(ord(x))
print(OUT)

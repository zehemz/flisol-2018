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


# lh = lambda n: struct.pack("<h", n)
li = lambda n: struct.pack("<i", n)

offset_size = TYPE_SIZE + SIZE_SIZE + RESERVED_1_SIZE + RESERVED_2_SIZE + OFFSET_SIZE
    #+ DBI_H_SIZE_SIZE + WIDTH_SIZE + HEIGHT_SIZE + COLORPLANES_SIZE + BITS_PER_PIXEL_SIZE
    #+ COMPRESSION_METHOD_SIZE + RAW_IMAGE_SIZE
print(offset_size)

def get_image():
    image = ""
    for i in range(0, 20*20):
        image+=str(chr(0)) + str(chr(255)) +str(chr(0))
    return image

def bmp():
    image = get_image()
    type = "BM"
    size_int = offset_size + len(image)
    size = str(chr(0x0e)) + str(chr(0x4b))+str(chr(0))*2
    print(size)
    reserved_1 = str(chr(0))*2
    reserved_2 = str(chr(0))*2
    offset = str(chr(0xe)) + str(chr(0)) * 3
    print(offset)
    return type + size + reserved_1 + reserved_2 + offset + image

with open('blue.bmp','wb') as f:
    image_as_hex = str()
    for x in bmp():
       image_as_hex+= hex(ord(x))
    print(image_as_hex)
    f.write(bmp())

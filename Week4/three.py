#
# three.py
#

# from PIL import Image

# im = Image.open( "three.png" )

# print("im is of size", im.size)

# im_resized = im.resize( (8,8), Image.BICUBIC )

# ir = im_resized

# for row in range(8):
#     for col in range(8):
#         r, g, b, a = ir.getpixel( (col,row) )
#         r = (256-r)//16
#         # pixstring = "{0:3d} ".format(r)  # cool Python formatting!
#         print( r, end=",")
#     # print()   # if you want to see the 64 values as an 8x8 array 

i_0=[0, 3, 8, 10, 10, 9, 2, 0, 0, 9, 8, 4, 3, 9, 11, 0, 0, 0, 0, 0, 2, 11, 6, 0, 0, 3, 6, 9, 14, 14, 6, 0, 0, 5, 8, 5, 3, 3, 12, 5, 0, 0, 0, 0, 0, 0, 10, 8, 2, 8, 3, 3, 5, 9, 11, 2, 1, 8, 11, 11, 9, 6, 1, 0]
i_1=[0, 2, 9, 10, 10, 7, 1, 0, 0, 1, 6, 4, 5, 15, 4, 0, 0, 0, 0, 2, 11, 11, 1, 0, 0, 2, 10, 14, 14, 11, 12, 4, 0, 1, 5, 2, 1, 1, 13, 6, 0, 0, 0, 0, 1, 11, 10, 0, 5, 6, 3, 7, 12, 8, 0, 0, 4, 11, 11, 8, 3, 0, 0, 0]
i_2=[0, 0, 2, 11, 6, 0, 0, 0, 0, 0, 1, 6, 14, 5, 0, 0, 0, 0, 0, 2, 13, 5, 0, 0, 1, 8, 10, 15, 16, 11, 7, 1, 2, 10, 8, 5, 5, 6, 14, 5, 0, 0, 0, 0, 0, 6, 13, 2, 0, 3, 5, 4, 11, 13, 3, 0, 0, 3, 13, 13, 8, 1, 0, 0]
i_3=[0, 3, 13, 10, 3, 0, 0, 0, 0, 1, 3, 8, 14, 2, 0, 0, 0, 0, 1, 7, 16, 8, 4, 0, 8, 12, 14, 12, 10, 10, 14, 7, 9, 7, 3, 0, 0, 0, 13, 7, 0, 0, 0, 0, 1, 11, 11, 0, 0, 0, 3, 5, 12, 11, 1, 0, 0, 1, 12, 12, 6, 0, 0, 0]
i_4=[0, 1, 7, 5, 2, 0, 0, 0, 0, 0, 7, 10, 13, 6, 0, 0, 0, 0, 2, 8, 16, 10, 1, 0, 0, 8, 13, 12, 10, 10, 13, 3, 0, 1, 1, 0, 0, 0, 13, 5, 4, 5, 0, 0, 1, 10, 11, 0, 7, 13, 4, 6, 12, 10, 1, 0, 1, 9, 12, 10, 5, 0, 0, 0]
i_5=[0, 0, 7, 13, 6, 0, 0, 0, 0, 0, 1, 5, 12, 9, 0, 0, 0, 0, 2, 3, 11, 13, 0, 0, 3, 12, 14, 13, 12, 13, 10, 1, 1, 4, 2, 1, 0, 3, 15, 3, 0, 0, 0, 0, 3, 12, 10, 0, 0, 2, 5, 10, 13, 7, 0, 0, 4, 13, 12, 7, 2, 0, 0, 0]
i_6=[0, 6, 12, 11, 8, 3, 0, 0, 0, 1, 2, 3, 8, 14, 2, 0, 0, 0, 1, 5, 12, 11, 2, 0, 1, 10, 12, 12, 12, 10, 12, 6, 1, 4, 2, 0, 0, 0, 11, 10, 0, 0, 0, 0, 0, 5, 14, 3, 0, 1, 1, 1, 6, 14, 5, 0, 0, 3, 12, 12, 12, 3, 0, 0]
i_7=[0, 0, 9, 13, 9, 2, 0, 0, 0, 0, 1, 2, 7, 13, 2, 0, 0, 0, 1, 4, 10, 15, 5, 0, 0, 8, 12, 11, 10, 8, 13, 5, 0, 3, 2, 0, 0, 3, 13, 3, 0, 0, 0, 0, 4, 13, 5, 0, 0, 1, 3, 9, 12, 4, 0, 0, 0, 7, 11, 7, 1, 0, 0, 0]
i_8=[0, 0, 1, 12, 7, 0, 0, 0, 0, 0, 0, 5, 11, 11, 1, 0, 0, 0, 0, 1, 9, 12, 1, 0, 0, 7, 11, 14, 16, 11, 4, 0, 0, 5, 5, 4, 3, 6, 14, 2, 0, 0, 0, 0, 0, 7, 12, 1, 1, 9, 4, 2, 9, 13, 3, 0, 0, 7, 13, 13, 9, 1, 0, 0]
i_9=[0, 3, 6, 6, 5, 6, 6, 1, 0, 3, 2, 0, 0, 0, 8, 3, 0, 0, 0, 0, 3, 7, 3, 0, 0, 2, 4, 8, 9, 6, 5, 1, 1, 4, 3, 1, 0, 0, 4, 8, 0, 0, 0, 0, 0, 0, 6, 6, 1, 0, 0, 0, 2, 5, 6, 0, 5, 6, 5, 6, 5, 2, 0, 0]

def call_image3():
    return [i_0,i_1,i_2,i_3,i_4,i_5,i_6,i_7,i_8,i_9]



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

i_0=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 4, 8, 8, 5, 0, 0, 0, 0, 1, 1, 7, 5, 0, 0, 0, 0, 3, 8, 9, 7, 0, 0, 0, 0, 1, 0, 0, 8, 1, 0, 0, 0, 5, 7, 8, 5, 0, 0, 0, 0, 1, 2, 1, 0, 0, 0]
i_1=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 6, 5, 1, 0, 0, 0, 0, 1, 4, 10, 3, 0, 0, 0, 0, 1, 7, 13, 5, 0, 0, 0, 0, 2, 5, 4, 10, 0, 0, 0, 0, 1, 0, 8, 5, 0, 0, 0, 1, 8, 9, 5, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
i_2=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 9, 1, 0, 0, 0, 0, 0, 2, 11, 3, 0, 0, 0, 0, 5, 10, 9, 10, 3, 0, 0, 0, 1, 1, 3, 10, 2, 0, 0, 0, 1, 9, 9, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
i_3=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 2, 9, 6, 0, 0, 0, 0, 2, 5, 10, 12, 6, 0, 0, 0, 5, 8, 3, 3, 11, 1, 0, 0, 0, 0, 1, 9, 5, 0, 0, 0, 0, 3, 9, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
i_4=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 4, 2, 0, 0, 0, 0, 0, 0, 7, 13, 4, 0, 0, 0, 0, 4, 10, 13, 10, 3, 0, 0, 0, 3, 3, 0, 7, 8, 0, 0, 2, 7, 0, 4, 11, 2, 0, 0, 1, 10, 9, 9, 2, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
i_5=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 3, 0, 0, 0, 0, 0, 0, 3, 11, 1, 0, 0, 0, 0, 7, 10, 13, 5, 0, 0, 0, 0, 4, 2, 3, 10, 0, 0, 0, 0, 0, 4, 10, 4, 0, 0, 0, 0, 8, 8, 2, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
i_6=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 7, 4, 0, 0, 0, 0, 0, 1, 3, 11, 3, 0, 0, 0, 0, 4, 9, 13, 7, 0, 0, 0, 0, 5, 4, 2, 10, 3, 0, 0, 0, 0, 0, 3, 9, 0, 0, 0, 0, 3, 7, 10, 2, 0, 0, 0, 0, 1, 4, 1, 0, 0, 0]
i_7=[0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 9, 8, 2, 0, 0, 0, 0, 0, 0, 8, 10, 0, 0, 0, 0, 6, 9, 11, 11, 5, 0, 0, 0, 4, 2, 0, 9, 5, 0, 0, 0, 0, 1, 8, 8, 0, 0, 0, 0, 6, 10, 6, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0]
i_8=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 2, 0, 0, 0, 0, 0, 0, 4, 11, 1, 0, 0, 0, 0, 4, 9, 12, 1, 0, 0, 0, 0, 5, 6, 7, 8, 0, 0, 0, 0, 1, 0, 7, 6, 0, 0, 0, 0, 8, 9, 7, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0]
i_9=[0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 3, 4, 3, 5, 0, 0, 0, 0, 0, 0, 3, 4, 0, 0, 0, 0, 2, 6, 7, 3, 0, 0, 0, 0, 2, 1, 0, 5, 1, 0, 0, 0, 0, 0, 1, 5, 0, 0, 0, 1, 4, 4, 4, 1, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0]

def call_image3():
    return [i_0,i_1,i_2,i_3,i_4,i_5,i_6,i_7,i_8,i_9]
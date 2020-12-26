import cv2
import numpy as np 
import hashlib
from functools import reduce
import sys

# text 直接传入字节流，超长抛出异常
# 内容：前2字节（0~65535）表示数据长度（字节数），之后是数据，数据后面补0，最后16字节是有效数据的MD5
def img_encode(text, to_file, *, block_size=8, info_size=(128, 128), salt='zhongtianqingwa'):
    capacity = ((info_size[0] * info_size[1]) >> 3)  - 18   # 最大可容纳的有效字节数
    total_bin = info_size[0] * info_size[1]             # 总bit数
    text_len = len(text)

    if text_len > min(capacity, 2021):
        print('字符串超长！干不了，谢谢！')

    md5 = hashlib.md5()
    md5.update(salt.encode() + text)                    # 记得加salt
    check = md5.hexdigest()

    fill = [0 for _ in range(capacity - text_len)]      # 填补空白

    # 每个元素是字节，比如[94, 182, 59, 187]
    # 由于md5的存在，可能有不可打印字符（大于128）
    char_list = [text_len >> 8, text_len & 0b11111111] + \
                 list(text) + fill + list(bytearray.fromhex(check))

    # 每个元素是一位
    bin_list = [0 for _ in range(total_bin)]
    for i in range(len(char_list)):
        bin_list[(i<<3):((i+1)<<3)] = []

    bin_list = sum([[(char>>(7-i)) & 1 for i in range(8)] for char in char_list], [])

    b0 = np.zeros((block_size, block_size), np.uint8)
    b1 = np.ones((block_size, block_size), np.uint8) * 255
    block_list = [[b1 if bin_list[i * info_size[1] + j] == 1 else b0 
                    for j in range(info_size[1])]
                    for i in range(info_size[0])]

    cv2.imwrite(to_file, np.block(block_list))


if __name__ == '__main__':
    a = sys.argv
    if len(sys.argv) < 2:
        print('田人吧！没有待编码的文件！')

    with open(a[1], 'rb') as f:
        if len(sys.argv) < 3:
            out_file = 'output.jpg'
        else:
            out_file = a[2]
        img_encode(f.read(), out_file)

    print('妈呀，大成功！')

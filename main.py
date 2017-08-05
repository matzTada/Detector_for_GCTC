#!usr/bin/env python
#-*- coding: utf-8 -*-

from detector import detector
from parser import html_parser

###### constant value ######
BITSIZE = 32

###### parse ######
data_list = html_parser('watermarked.txt')

print('========== data_list ==========')
# print(len(data_list))
print(data_list)

###### detect ######
returnList = detector(data_list, BITSIZE)
extract_bits = returnList[0]
detected_watermark = returnList[1]

print('========== extract_bits ==========')
# print(len(extract_bits))
print(extract_bits)

print('========== detected_watermark ==========')
print(detected_watermark)

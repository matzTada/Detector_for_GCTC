#!usr/bin/env python
#-*- coding: utf-8 -*-

from detector import detector
from parser import html_parser

###### constant value ######
BITSIZE = 32

###### parse ######
data_list = html_parser('watermarked.txt')
with open('data_list', 'w') as f:
  for data in data_list:
    f.write(str(data) + '\n')
print('========== data_list ==========')
print(data_list)

###### detect ######
detected_watermark = detector(data_list, BITSIZE)
with open('watermark', 'w') as f:
  if type(detected_watermark) != str:
    print('ERROR: detected_watermark is not type of str')
  else:
    f.write(detected_watermark)
print('========== detected_watermark ==========')
print(detected_watermark)

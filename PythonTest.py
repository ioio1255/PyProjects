# def convertG2KG(gramValue):
#     return float(gramValue / 1000)
#
#
# print(convertG2KG(980))
#
# import math
#
#
# def getValueOfHypotenuse(rightAngelSideA, rightAngelSideB):
#     return 'The right triangle third side\'s length is {}'.format(
#         math.sqrt(rightAngelSideA * rightAngelSideA + rightAngelSideB * rightAngelSideB))
#
#
# print(getValueOfHypotenuse(9, 40))
#
#
# def trapezoid_area(base_up, base_down, height=3):
#     return 1 / 2 * (base_up + base_down) * height
#
#
# print(trapezoid_area(base_down=5, base_up=1))
#
# file = open('C://TestFolder/3.txt', 'w')
# file.write("hello world000")
# file.close()
#
#
# def text_filter(word, censored_word='lame', changed_word='awesome'):
#     return word.replace(censored_word, changed_word)
#
#
# def text_create(name, msg):
#     desktop_path = 'C://TestFolder/'
#     file_fullpath = desktop_path + name
#     file = open(desktop_path + name, 'w')
#     file.write(msg)
#     file.close()
#     print('msg has been written to the file {}'.format(file_fullpath))
#
#
# def censored_text_create(name, msg):
#     clean_msg = text_filter(msg)
#     text_create(name, clean_msg)
#
#
# # input_text = input('Input something please')
# # censored_text_create('abc.txt', input_text)  # 调用函数
#
# album = ['test', 5, True, 'Bye']
# print(album.__len__())
# print(album[-1], album[0])
#
#
# def ten_files_create():
#     desktopPath = 'C://Users/administrator.APJDEMO/Desktop/'
#     for fileindex in (1, 10):
#         file.open(desktopPath + fileindex + '.txt', 'w+')
#         # file.write('ssss')
#         file.close()
# ten_files_create()

fruit = ['pineapple','pear','grape']
fruit.remove('grape')
print(fruit)

del fruit[0:1]
print(fruit)

import sys

print(sys.path[3])
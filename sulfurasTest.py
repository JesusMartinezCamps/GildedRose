# -*- coding: utf-8 -*-

##Caso test Sulfuras
from clases import *

if __name__ == '__main__':

	item = Sulfuras("Sulfuras, Hand of Ragnaros", 0, 75)
	print(item)

	for dia in range(1, 10):
		item.update_quality()
		print(item)
	
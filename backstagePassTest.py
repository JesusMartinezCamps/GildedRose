# -*- coding: utf-8 -*-

#Caso test para el Backstage pass
from clases import *

if __name__ == '__main__':

    item = backstagePassTest("Backstage passes to a TAFKAL80ETC concert", 15, 20)
    # chequeo herencia __repr__
    print(item)
    # test update_quality
    for dia in range(1, 10):
        item.update_quality()
        print(item)

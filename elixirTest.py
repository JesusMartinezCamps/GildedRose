# -*- coding: utf-8 -*-

#Caso test del Elixir
from clases import *

if __name__ == '__main__':

    item = elixirTest("Elixir of the Mongoose", 5, 7)
    # chequeo herencia __repr__
    print(item)
    # test update_quality
    for dia in range(1, 10):
        item.update_quality()
        print(item)

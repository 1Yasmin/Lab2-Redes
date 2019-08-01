#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Cristian Pérez
# Yasmin Chávez
#

from bitarray import bitarray
import random

def to_ascii(mensaje):
    return [ord(c) for c in mensaje]

def line_ascii(mensaje):
    return ''.join(str(ord(c)) for c in mensaje)

def line_str(mensaje):
    ' '.join(format(ord(c), 'b') for c in mensaje)

def to_bitarray(mensaje):
     a = bitarray()
     a.frombytes(mensaje.encode('ascii'))
     return a
     
def random_error(array):
    num = array.length()
    error = random.randint(1,num)
    print(error)
    cnt = 0
    for a in array:
        cnt = cnt + 1
        if(cnt % error == 0):
            print("inicio", a)
            if(a == True):
                array[a] = False
            elif(a == False):
                array[a] = True
            print("fin", a)
    
    return array
    
"""
def main():
    mensaje = input("Ingrese el mensaje: ")
    ms = to_bitarray(mensaje)
    print(ms)
    print(random_error(ms))


if __name__ == "__main__":
   main()
"""
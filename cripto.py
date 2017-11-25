#!/usr/bin/env python
# -*- coding: utf-8 -*-
arq = open('mod.txt', 'r')
texto = arq.readlines()

'''for linha in texto :
    print(linha)'''
code=""


talking = True

while(talking):
    tam = int(input("Tamanho da palavra"))

    for i in range(tam):
        a = int(input("Escoolha a linha"))

        #if(a==2):
        word = texto[a]

        b = int(input("Escoolha a posição da letra"))
        #print(word[b])

        code = code+word[b]
    code = code + " "

    cont = input("Fim?")
    if (cont=="7"):
        talking=False
        
    #jj = len(word)
    #print(jj)
print(code)
arq.close()

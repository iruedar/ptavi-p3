#!/usr/bin/python3
# -*- coding: utf-8 -*-

<<<<<<< HEAD
from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContentHandler):

    def __init__(self):   # Declaramos las listas
        self.lista_etiquetas = []
        self.attrs = {
            'root-layout': ['width', 'height', 'background-color'],
            'region': ['id', 'top', 'bottom', 'left', 'right'],
            'img': ['src', 'region', 'begin', 'dur'],
            'audio': ['src', 'begin', 'dur'],
            'textstream': ['src', 'region']}

    def startElement(self, name, attrs):
        dic = {}
        if name in self.attrs:
            for atributo in self.attrs[name]:
                dic[atributo] = attrs.get(atributo, '')
            self.lista_etiquetas.append([name, dic])

# Devuelve una lista con etiquetas, atributos y contenidos encontrados
    def get_tags(self):
        return self.lista_etiquetas

if __name__ == "__main__":
    parser = make_parser()
    ssHandler = SmallSMILHandler()
    parser.setContentHandler(ssHandler)
    parser.parse(open('karaoke.smil'))
    print(ssHandler.get_tags())
=======

>>>>>>> 5ea11a956b917c8db785f8dfed5128b14bf95a33

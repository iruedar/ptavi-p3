#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
from smallsmilhandler import SmallSMILHandler
import sys
import json
import urllib.request


class KaraokeLocal:

    # Parsea el fichero
    def __init__(self, file):
        parser = make_parser()
        ssHandler = SmallSMILHandler()
        parser.setContentHandler(ssHandler)
        parser.parse(open(file))
        self.lista = ssHandler.get_tags()

    # imprime las etiquetas y sus atributos que tienen valor asignado
    def __str__(self):
        salida = ''
        for etiqueta in self.lista:
            att = ''
            nombre = etiqueta[0]
            dicc = etiqueta[1]
            for attrs in dicc:
                if dicc[attrs] != '':
                    att += '\t' + attrs + '="' + dicc[attrs] + '"'
            salida += nombre + att + '\n'
        return salida

    # Transforma el fichero a .json
    def to_json(self, file, file_exit=""):
        if file_exit == "":
            file_exit = file.replace('.smil', '.json')
        with open(file_exit, 'w') as outfile_json:
            json.dump(self.lista, outfile_json, indent=3)

    # Descarga los archivos
    def do_local(self):
        for etiqueta in self.lista:
            dicc = etiqueta[1]
            for attrs in dicc:
                if attrs == 'src':
                    if dicc[attrs].startswith('http://'):
                        url = dicc[attrs]
                        file = url.split('/')[-1]
                        urllib.request.urlretrieve(url, file)
                        dicc[attrs] = file

if __name__ == "__main__":

    try:
        file = sys.argv[1]
    except (IndexError, ValueError):
        sys.exit('Usage: python3 karaoke.py file.smil')

    karaoke = KaraokeLocal(file)
    print(karaoke)
    karaoke.to_json(file)
    karaoke.do_local()
    print(karaoke)
    karaoke.to_json(file, 'local.json')

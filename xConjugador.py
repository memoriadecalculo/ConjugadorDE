#!/usr/bin/env python3
# coding: utf-8
'''
@project: ConjugadorDE <github.com/memoriadecalculo/ConjugadorDE>
@copyright: Memória de Cálculo (c) 2023 <memoriadcalculo@gmail.com>
'''

import sys
#import urllib
#from formatter import AbstractFormatter , DumbWriter
#from htmllib import HTMLParser
from sgmllib import SGMLParser

# Váriáveis pré-definidas
# Línguas possíveis
linguas = {}
linguas['de'] = (22,('ich','du','er,sie,es','wir','ihr','sie,Sie'))
linguas['en'] = (20,)
linguas['fr'] = (3,)
linguas['pt'] = (2,)

# URL
url = ("http://www.verbix.com/webverbix/go.php?D1=","&H1=","&T1=")

# Lendo os parâmetros de entrada:
if (len(sys.argv) == 3) and linguas.has_key(sys.argv[1]):
    lingua = sys.argv[1]
    verbo = sys.argv[2]
else:
    print("Uso:",sys.argv[0], "língua verbo", sys.exit(1))

# Pegando o conteúdo da página:
urltoda = url[0] + str(linguas[lingua][0]) + url[1] + str(linguas[lingua][0] + 100) + url[2] + verbo
#arqHTMLcod = urllib.urlopen(urltoda)
#arqHTML = arqHTMLcod.read()
#arqHTMLcod.close()
#print arqHTML


##arqHTML = open("untersuchen.html", "r")
#tabela = ""
#grava = False
#for linha in arqHTMLcod:
#    if grava:
#        if StrFim in linha:
#            break
#        tabela = tabela + linha
#    if StrInicio in linha:
#        grava = True
#print tabela
#arqHTMLcod.close()
#
#ofile = open(verbo + ".html", 'w')
#ofile.writelines(tabela)
#ofile.close()

arqHTMLcod = open("untersuchen.html", 'r')
arqHTML = arqHTMLcod.read()
arqHTMLcod.close()

#
#from HTMLParser import HTMLParser
#
#class HeadingParser(HTMLParser):
#    nTabela = 0
#    nLinha = 0
#    nColuna = 0
#    
#    td_txt = ""
#    inHeading = False
#    
#    import xml.dom.minidom
#    myDoc = xml.dom.minidom.Document()
#    
#    
#    def handle_starttag(self, tag, attrs):
#        if tag == "table":
##            self.nTabela += 1
##            self.nLinha = 0
##            self.nColuna = 0
##            print "TABELA: " + str(self.nTabela)
#            
#            noTabela = self.myDoc.createElement("table")
#        elif tag == "tr":
##            self.nLinha +=1
##            self.nColuna = 0
##            print "LINHA: " + str(self.nLinha)
#            
#            noLinha = self.myDoc.createElement("linha")
#            noTabela.appendChild(self.noLinha)
#        elif tag == "td" or tag == "th":
##            self.nColuna +=1
##            self.inHeading = True
##            print "COLUNA: " + str(self.nColuna)
#            
#            noColuna = self.myDoc.createElement("coluna")
#            noLinha.appendChild(self.noColuna)
#
#    def handle_data(self, data):
#        if self.inHeading:
#            if data.strip():
#                self.td_txt = self.td_txt + data.strip() + "|"
#
#    def handle_endtag(self, tag):
#        if tag == "table":
##            self.nTabela += 1
##            self.nLinha = 0
##            self.nColuna = 0
##            print "TABELA: " + str(self.nTabela)
#             
#        elif tag == "tr":
##            self.nLinha +=1
##            self.nColuna = 0
##            print "LINHA: " + str(self.nLinha)
#            
#        elif tag == "td" or tag == "th":
#            titleText = self.myDoc.createTextNode(self.td_txt)
#            self.noColuna.appendChild(titleText)
##            print "TEXTO: " + self.td_txt
#            self.inHeading = False
#            self.td_txt = ""
#
## Carregando a lista dos conteúdos de cada célula da tabela:
#print "COMECO" 
#hParser = HeadingParser()
#hParser.feed(tabela)



#<?xml version=”1.0”?>
#<conjugador>
#    <verbo>
#        <nome>trinken</nome>
#        <author>Neil Gaiman</author>
#    </verbo>
#</conjugador>
#
## será que vale a pena usar htmllib para ter um print bonito do html se necessário?

class coletaHTML(SGMLParser):
    """ Classe que coleta somente o conteúdo HTML
    entre duas tags de comentário.
    O comentário inicial liga a coleta e o final desliga."""
    
    def __init__(self, commentarioIni, commentarioFim, verbose=0):
        SGMLParser.__init__(self, verbose=verbose)
        self.commentarioIni = commentarioIni
        self.commentarioFim = commentarioFim
    
    def reset(self):
        self.texto = []
        self.ligado = False
        SGMLParser.reset(self)
    
    def handle_data(self, data):
        SGMLParser.handle_data(self, data)
        if self.ligado:
            self.texto.append(data)
    
    def handle_comment(self, data):
        SGMLParser.handle_comment(self, data)
        if data.strip() == self.commentarioIni:
            self.ligado = True
        if self.ligado and data.strip() == self.commentarioFim:
            self.ligado = False
    
    def unknown_endtag(self, tag):
        SGMLParser.unknown_endtag(self, tag)
        if tag == 'th':
            self.texto.append('|')
    
    def output(self):               
        """Return processed HTML as a single string"""
        return "".join(self.texto).splitlines()

#class coletaHTML(HTMLParser):
#    """ Classe que coleta somente o conteúdo HTML
#    entre duas tags de comentário.
#    O comentário inicial liga a coleta e o final desliga."""
#    
#    def __init__(self, formatter, commentIni, commentFim, verbose=0):
#        HTMLParser.__init__(self, formatter, verbose=verbose)
#        self.commentIni = commentIni
#        self.commentFim = commentFim
#    
#    ligado = False
#
#    def handle_data(self, data):
#        if self.ligado:
#            HTMLParser.handle_data(self, data)
#
#    def handle_comment(self, data):
#        if data.strip() == self.commentIni:
#            self.ligado = True
#        if self.ligado and data.strip() == self.commentFim:
#            self.ligado = False
#    def unknown_endtag(self, tag):
#        HTMLParser.unknown_endtag(self, tag)
#        if tag == 'th':
#            sys.stdout.write('|')
#
##Criando o formatador:
#writer = DumbWriter()
#formatter = AbstractFormatter (writer)

#Criando as strings com os limites do texto desejado:
strIni = '#BeginEditable "Full_width_text"'
strFim = '#EndEditable'

# Criação do parser: 
#parser = coletaHTML(formatter, strInicio, strFim)
parser = coletaHTML(strIni, strFim)
parser.feed(arqHTML)
#parser.texto.splitlines()
# Transformando a saída do parser em XML:
nLinha = 0
for linha in parser.output():
    if linha.strip():
        nLinha += 1
#        print "Linha = %g  %s\n" % (nLinha,linha)
        
        if nLinha <= 3:
            tempo, verbo = linha.split(':')
            print('SUMARIO: ' + tempo + ' | ' + verbo)
            
        if nLinha == 4:
            valores = linha.split()
#            modo1 = valores[0]
#            modo2 = valores[1]
            print(valores)

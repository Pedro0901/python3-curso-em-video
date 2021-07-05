'''
Exercício Python 114: Crie um código em Python que
teste se o site pudim está acessível pelo computador usado.
'''
import urllib
import urllib.request
import colorama

colorama.init()
try:
	site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
	print('\u001b[31mO site \u001b[33mPudim \u001b[31mnão está acessível no momento.\u001b[0m')
else:
	print('\u001b[32mConsegui acessar o site \u001b[33mPudim \u001b[32mcom sucesso.\u001b[0m')

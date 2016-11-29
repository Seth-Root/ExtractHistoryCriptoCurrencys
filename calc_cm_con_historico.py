# -*- coding: utf-8 -*-
# -*- encoding: utf-8 -*-


import urllib2
import re
from BeautifulSoup import BeautifulSoup

Value_Euro_in_bolivar = 0
Value_Euro_in_bolivar = 0
value_BTC_dolares = 0

### Extracion de los Datos BTC
lista_monedas = ['bitcoin','steem','ethereum','ripple','litecoin','monero', 'dash', 'nem', 'dogecoin', 'waves']

pagina_monedas = "http://coinmarketcap.com/"

pagina_historica = "http://coinmarketcap.com/historical/"

html_page = urllib2.urlopen(pagina_historica)


soup = BeautifulSoup(html_page)


lista_precios_BTC = []
lista_precios_Ethereum = []
lista_precios_Ripple = []
lista_precios_Litecoin = []
lista_precios_Monero = []
lista_fecha = []
for link in soup.findAll('a'):
                texto_link = link.get('href')
                if texto_link == None:
                                continue
                
                if "2016" in texto_link:
                                 print texto_link
                                 pagina_history = pagina_monedas+ texto_link
                                 html_page = urllib2.urlopen(pagina_history)
                                 soup = BeautifulSoup(html_page)
                                 
                                 solo_unos_cuantos = 0
                                 
                                 fecha = texto_link[12:-2]
                                 year = fecha[-8:-4]
                                 month = fecha[-4:-2]
                                 day = fecha[-2:]
                                 
                                 for link in soup.findAll('a'):

                                                 link_link = link.get('href')
                                                 if link_link == None:
                                                                 continue
                                                  
                                                 else:
                                                                 lista_fecha.append(fecha)
                                                                 
                                                                 if "/currencies/bitcoin/#markets" == link_link:
                                                                                 texto_link = link.text
                                                                                 texto_link = texto_link[2:]
                                                                                 clase_precio = link['class']
                                                                                 if clase_precio == "price":
                                                                                                 
                                                                                                 print "Bitcoin :", texto_link, "$  ", fecha
                                                                                                 lista_precios_BTC.append(texto_link)
                                                                                                 
                                                                                                 
                                                                 elif "/currencies/ethereum/#markets" == link_link:
                                                                                 texto_link = link.text
                                                                                 texto_link = texto_link[2:]
                                                                                 clase_precio = link['class']
                                                                                 if clase_precio == "price":
                                                                                                 print "Ethereum ", texto_link, "$  ", fecha
                                                                                                 lista_precios_Ethereum.append(texto_link)

                                                                                                 
                                                                                                 
                                                                                                 
                                                                 elif "/currencies/ripple/#markets" == link_link:
                                                                                 texto_link = link.text
                                                                                 texto_link = texto_link[2:]
                                                                                 clase_precio = link['class']
                                                                                 if clase_precio == "price":
                                                                                                 print "Ripple ", texto_link, "$  ", fecha
                                                                                                 lista_precios_Ripple.append(texto_link)

                                                                                                 
                                                                                                 
                                                                 elif "/currencies/litecoin/#markets" == link_link:
                                                                                 texto_link = link.text
                                                                                 texto_link = texto_link[2:]
                                                                                 clase_precio = link['class']
                                                                                 if clase_precio == "price":
                                                                                                 print "Litecoin ", texto_link, "$  ", fecha
                                                                                                 
                                                                                                 lista_precios_Litecoin.append(texto_link)
                                                                                                 
                                                                                                 
                                                                 elif "/currencies/monero/#markets" == link_link:
                                                                                 texto_link = link.text
                                                                                 texto_link = texto_link[2:]
                                                                                 clase_precio = link['class']
                                                                                 if clase_precio == "price":
                                                                                                 print "Monero ", texto_link, "$  ", fecha
                                                                                                 
                                                                                                 lista_precios_Monero.append(texto_link)
                                                                                                 
                                                                                                 
                                                                                                 
                                                                                                 
                                                                                                 
                                                                                                 
                                                                                                 
                                                                                                 
print lista_precios_Monero


print "#########################"
print "#########################"
print "#########################"
print "#########################"

print lista_fecha

                                                                
                                                                
                                                                
                                                                 
                                                 
                                 
                                 
                                 


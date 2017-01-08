#!/usr/bin/env python
# -*- coding: latin-1 -*-
import urllib
import urllib2

def translate(to_translate, to_langage="auto", langage="auto"):
	'''Return the translation using google translate
	you must shortcut the langage you define (French = fr, English = en, Spanish = es, etc...)
	if you don't define anything it will detect it or use english by default
	Example:
	print(translate("salut tu vas bien?", "en"))
	hello you alright?
	:rtype: object'''
	agents = {'User-Agent':"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)"}
	before_trans = 'class="t0">'
	to_translate=urllib.quote(to_translate)
	link = "http://translate.google.com/m?hl=%s&sl=%s&q=%s" % (to_langage, langage, to_translate.replace(" ", "+"))
	request = urllib2.Request(link, headers=agents)
	page = urllib2.urlopen(request).read()
	result = page[page.find(before_trans)+len(before_trans):]
	result = result.split("<")[0]
	return result


#print translate("Restaurant italiano elegante y c?lido a la vez. El servicio es excelente. La comida es de buena calidad, fresca, con platos tradicionales bien preparados. Yo fui varias veces a cenar y nunca me desilusiono. Lo recomiendo mucho, por la buena comida y el ambiente s?per agradable.","en")
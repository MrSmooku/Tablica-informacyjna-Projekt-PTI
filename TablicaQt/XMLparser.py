#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

from xml.dom import minidom
import os

class XMLparser:
    DOMTree = minidom.parse('test.xml')
    s = ''
    style = ''
    widgetList = []
    pageWidgetList = []


    cNodes = DOMTree.childNodes
    for i in cNodes[0].getElementsByTagName("style"):
        style = i.childNodes[0].nodeValue
        print style

    cNodes = DOMTree.childNodes
    for i in cNodes[0].getElementsByTagName("widget"):
        # nazwa taga
        #print i.getElementsByTagName("WeathercastWidget")[0].nodeName
        # wartosc taga
        #print i.getElementsByTagName("imie")[0].childNodes[0].toxml()
        # dostep do atrybutu
        #print i.getElementsByTagName("WeathercastWidget")[0].getAttribute("x")
        #print i.getElementsByTagName("WeathercastWidget")[0].getAttribute("y")



        if not i.getAttribute("extra") and not i.getAttribute("url"):
            s = i.getAttribute("name")+'(self,'+i.getAttribute("x")+','+i.getAttribute("y")+')'
        elif i.getAttribute("url"):
            s = i.getAttribute("name")+'(self,'+i.getAttribute("x")+','+i.getAttribute("y")+','+i.getAttribute("url")+')'
        else:
            s = i.getAttribute("name")+'(self,'+i.getAttribute("x")+','+i.getAttribute("y")+','+i.getAttribute("extra")+')'
            print s
        widgetList.append(s)

    counter = 0
    cNodes = DOMTree.childNodes
    for i in cNodes[0].getElementsByTagName("page"):
        counter += 1
        for x in i.getElementsByTagName("widget"):
            if not x.getAttribute("extra"):
                s = x.getAttribute("name")+'(self,'+x.getAttribute("x")+','+x.getAttribute("y")+')'
            else:
                s = x.getAttribute("name")+'(self,'+x.getAttribute("x")+','+x.getAttribute("y")+','+i.getAttribute("extra")+')'
            pageWidgetList.append((counter,s))



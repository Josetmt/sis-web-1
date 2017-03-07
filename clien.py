#!/usr/bin/env python
# ~#~ coding: utf~8 ~#~
# vim: set fileencoding=utf8 :
import urllib2
import bs4

class Client(object):
    def get_webpage(self, page):
        f = urllib2.urlopen(page)
        htmlpage = f.read()
        f.close()
        return htmlpage

    def search_data(self, html):
        bs = bs4.BeautifulSoup(html, "lxml")
        #caixa= bs.find("div","sg-featuredlink")
        items = bs.find("div","dotd-title").text.strip()

        return items


    def main(self):
        webpage = self.get_webpage('https://www.packtpub.com/packt/offers/free-learning/')
        results = self.search_data(webpage)
        print results
        

if __name__ == "__main__":
    cw = Client()
    cw.main()

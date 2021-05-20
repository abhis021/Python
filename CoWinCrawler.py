# import scrapy
# class spider1(scrapy.Spider):
#     name = "cowin18plus"
#     start_urls+ ['https://www.cowin.gov.in/home']
#         def parse(self, response):
#             pass


import requests
from bs4 import BeautifulSoup
def web(page, WebUrl):
    if(page>0):
        url = WebUrl
        code = requests.get(url)
        plain = code.text
        s = BeautifulSoup(plain, "html.parser")
        for link in s.findAll ('a', {'class':'s-access-detail-page'}):
            tet = link.get('title')
            print(tet)
            tet_2 = link.get('href')
            print(tet_2)
web(1, 'https://www.cowin.gov.in/home')
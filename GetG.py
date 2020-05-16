# -*- coding: utf-8 -*-
"""
获取隔离开关型号表

@author: Yuan3G
"""

import requests
from requests.exceptions import RequestException
from bs4 import BeautifulSoup

def get_response(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            response.encoding = 'UTF-8'
            return response.text
        return None
    except RequestException:
        return None


def get_file(url,file):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            with open(file, "wb") as code:
                code.write(response.content)
        return None
    except RequestException:
        return None


def get_html(url,file):
    html = get_response(url)
    soup = BeautifulSoup(html,'lxml')
    soup.prettify()
    url0=soup.find('a',attrs={'class':'d-flex flex-items-center min-width-0'})['href']
    url1='https://github.com'+url0
    get_file(url1,file)


 
if __name__ == '__main__':

    url = "https://github.com/Yuan3G/SCC_G/releases"
    file ='隔离开关.xlsx'
    get_html(url,file)

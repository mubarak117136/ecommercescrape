from __future__ import absolute_import, unicode_literals
from celery.decorators import task
from urllib.request import urlopen
from bs4 import BeautifulSoup
from django.db.models import Q
import time


@task(name="test-name")
def test_print():
    print("hello world")



def fetch_farfetch():
    url = "https://www.farfetch.com/uk/shopping/women/sale/all/items.aspx"
    page = urlopen(url)

    bs = BeautifulSoup(page, "lxml")

    product = bs.find(attrs={"data-testid": "productCard"})

    detail_a = product.find("a")
    detail_url = "https://farfetch.com" + detail_a["href"]

    image_url = detail_a.find("meta", attrs={"itemprop": "image"})["content"]

    brand = detail_a.find(attrs={"data-testid": "productDesignerName"}).text
    name = detail_a.find(attrs={"data-testid": "productDescription"}).text

    old_price = detail_a.find(attrs={"data-testid": "initialPrice"}).text
    discount = detail_a.find(attrs={"data-testid": "discountPercentage"}).text
    price = detail_a.find(attrs={"data-testid": "price"}).text


    print(old_price, discount, price)

fetch_farfetch()
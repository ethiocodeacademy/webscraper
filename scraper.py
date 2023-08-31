#August 31, 2023 
__author__ = 'EthioCodeAcademy - Subscribe, Like, Share!'

from bs4 import BeautifulSoup
import requests, openpyxl

def export_data(data):
    excel = openpyxl.Workbook()
    sheet = excel.active
    sheet.title = "Helloo Market Data"
    # print(excel.sheetnames)
    sheet.append(['Product Name', 'Product Price', 'Product Link'])
    for item in data:
        sheet.append(item)
    excel.save(sheet.title+".xlsx")

try:
    req = requests.get("https://helloomarket.com/")
    req.raise_for_status()
    soup = BeautifulSoup(req.content, "html.parser")

    products = soup.find('div', class_="box-product").find_all('div', class_="product-items")
    data = []
    for product in products:
        product_name = product.find('div', class_="product-details").a.text
        product_link = product.find('div', class_="product-details").a.get("href")
        product_price = product.find('div', class_="product-details").p.get_text(strip=True).split("Ex")[0].replace("ETB", "")
        data.append([product_name,product_price, product_link])
        # break
    export_data(data)
except Exception as e:
    print(e)

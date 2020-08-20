import datetime
import calendar
import random
import numpy
import pandas as pd
import uuid

products = {
    "iPhone": [700, 10],
    "Google Phone": [600, 8],
    "Vareebadd Phone": [400, 3],
    "20in Monitor": [109.99, 6],
    "34in Ultrawide Monitor": [379.99, 9],
    "27in 4K Gaming Monitor": [389.99, 9],
    "27in FHD Monitor": [149.99, 11],
    "Flatscreen TV": [300, 7],
    "Macbook Pro Laptop": [1700, 7],
    "ThinkPad Laptop": [999.99, 6],
    "AA Batteries (4-pack)": [3.84, 30],
    "AAA Batteries (4-pack)": [2.99, 30],
    "USB-C Charging Cable": [11.95, 30],
    "Lightning Charging Cable": [14.95, 30],
    "Wired Headphones": [11.99, 26],
    "Bose SoundSport Headphones": [99.99, 19],
    "Apple Airpods Headphones": [150, 22],
    "LG Washing Machine": [600.00, 1],
    "LG Dryer": [600.00, 1],
}

columns = [
    "Order ID",
    "Product",
    "Quantity Ordered",
    "Price Each",
    "Order Date",
    "Purchase Address",
]

product_list = [product for product in products]
weights = [products[product][1] for product in products]

n = 5

for _ in range(n):
    print(_)

list = [1, 2, 3, 4, 5, 6, 7, 8]

def sum_of_squares(v):
    #square = [i ** 2 for i in v]
    #print(square)
    return sum([i ** 2 for i in v])

print(sum_of_squares(list))

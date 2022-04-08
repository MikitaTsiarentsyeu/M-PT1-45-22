# key - Name
# 0: Category, 1: Product Code, 2: Price USD,  3: Stock balance

import json


data_json = """{
    "Glenmorangie" : [
        "Whisky",
        "whikey01",
        245,
        3],
    "Johnnie Walker Blue" : [
        "Whisky",
        "whikey02",
        482,
        5],
    "Martell XO": [
        "Cognac",
        "cog01",
        225,
        4],
    "Napoleon VSOP" : [ 
        "Cognac",
        "cog02",
        30,
        6],
    "770 Miles Zinfandel": [
        "Wine",
        "wine01",
        15.30,
        10],
    "King Saint Chinian 2020" : [
        "Wine",
        "wine02",
        16.12,
        20]
}""" 


def all_category():
    data_base = (json.loads(data_json)).items()
    #print (data_base)
    return data_base
    

def category(category):
    data_base = all_category()
    #print (data_base)
    data_category = {}
    for k, v in data_base:
        if v[0] == category:
            data_category[k] = v
    data_category = data_category.items()
    return data_category

import json

# from .models import Product


def change_json():
    new_json = {}
    list_json = []
    with open("ovoshchi.json", encoding="utf-8") as file:
        products_dict = json.load(file)
    pk = 1
    for slug, data in products_dict.items():
        new_json = {
            "model": "parser_lenta.product",
            "pk": pk,
            "fields": {
                "name": data["name"],
                "slug": data["url"],
                "price": data["price"]
            }
        }
        list_json.append(new_json)
        pk += 1
    with open("fixtures/new.json", "w",
              encoding="utf-8") as file:
        json.dump(list_json, file, indent=4, ensure_ascii=False)


change_json()

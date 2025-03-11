from pydantic import BaseModel

class ProductPydantic(BaseModel):
    name: str
    price: float
    in_stock: bool

# main.py dosyasındaki kodun aynısını pydantic kullanarak yazdığımızda hata alıcaz çünkü
# pydantic bir nevi diğer dillerdeki gibi değişkenlere dikkat etmeyi zorunlu kılar

if __name__ == '__main__' :
    external_data = {
        "name" : "Mehmet",
        "price" : 999.99,
        "in_stock" : False
    }

    product1 = ProductPydantic(
        name=external_data.get("name"),
        price=external_data.get("price"),
        in_stock=external_data.get("in_stock")
    )

    print(product1.name)
    print(product1.price)
    print(product1.in_stock)

    print(type(product1.name))
    print(type(product1.price))
    print(type(product1.in_stock))
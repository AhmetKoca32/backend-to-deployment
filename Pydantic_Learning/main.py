class Product:

    def __init__(self, name, price, in_stock):
        self.name = name
        self.price = price
        self.in_stock = in_stock


if __name__ == '__main__':
    # ornek_product = Product(name="Ahmet",price=100,in_stock=True)
    # print(ornek_product.in_stock)  # Pythonda değişken türü tanımlama yoktur değişkenin tipini kendi belirler


    external_data = {
        "name" : "Mehmet",
        "price" : "999.99",
        "in_stock" : "False"
    }

    product1 = Product(
        name=external_data.get("name"),
        price=external_data.get("price"),
        in_stock=external_data.get("in_stock")
    )

    # değişken türü tanımlama olmadığı için ufak bi uyarı verir ama yine de olursa olsun yazdırır ekrana
    # bu durum bize bazen sorun çıkartabilir ama bu yüzden pydantic kütüphanesi kullanılır
    # mesela aşağıda örneğini gördüğünüz gibi türü string ama yazılan bool veya int değer farketmiyor bildiği gibi yazıyor


    print(product1.name)
    print(product1.price)
    print(product1.in_stock)

    print(type(product1.name))
    print(type(product1.price))
    print(type(product1.in_stock))
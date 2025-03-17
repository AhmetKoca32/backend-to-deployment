import time

def my_func_1():
    print("1. fonksiyonum başlıyor")
    time.sleep(5)
    print("1. fonksiyonum bitti")
    return 5


def my_func_2():
    print("2. fonksiyonum başlıyor")
    time.sleep(5)
    print("2. fonksiyonum bitti")
    return 10

if __name__ == '__main__':

    x = my_func_1()
    y = my_func_2()

    print(f"1.fonksiyonumun çalışmasının sonucu olarak x değeri => {x}")
    print(f"2.fonksiyonumun çalışmasının sonucu olarak y değeri => {y}")
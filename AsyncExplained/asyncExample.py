import asyncio

async def birinci_fonksiyon():
    print("Birinci fonksiyon başladı")
    await asyncio.sleep(5)
    print("Birinci fonksiyon bitti")
    return 5

async def ikinci_fonksiyon():
    print("İkinci fonksiyon başladı")
    await asyncio.sleep(5)
    print("İkinci fonksiyon bitti")
    return 10

async def main():
    task1 = asyncio.create_task(birinci_fonksiyon())
    task2 = asyncio.create_task(ikinci_fonksiyon())

    x = await task1
    y = await task2

    print(x)
    print(y)

if __name__ == '__main__':
    asyncio.run(main())

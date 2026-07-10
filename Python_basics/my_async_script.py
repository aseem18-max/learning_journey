import asyncio
import requests
import time
async def func1():
    url = "https://upload.wikimedia.org/wikipedia/commons/6/6a/Mona_Lisa.jpg"
    response = requests.get(url)
    open("mona.jpg", 'wb').write(response.content)
    #await asyncio.sleep(1)
    print("Function 1")
    return "Aseem"
async def func2():
    url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQVKghS-fUfdZUI3yISAyyH7XHyI_Jwh6QmLzCueUf48dVt67zp4flamG0&s=10"
    response = requests.get(url)
    open("galaxy.jpg", 'wb').write(response.content)
    #await asyncio.sleep(1)
    print("Function 2")
async def func3():
    url = "https://wiki.ross-tech.com/wiki/images/1/14/Eric%27s_S4.jpg"
    response = requests.get(url)
    open("car.jpg", 'wb').write(response.content)
    #await asyncio.sleep(4)
    print("Function 3")
async def my_async_script():
    L = await asyncio.gather(func1(), func2(), func3())
    print(L)
    #task = asyncio.create_task(func1())
    #await func1()
    #await func2()
    #await func3()
asyncio.run(my_async_script())
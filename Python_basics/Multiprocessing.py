import multiprocessing
import requests

def download_file(url, name):
    print("Started Downloading {name}")
    response = requests.get(url)
    open(f"images/{name}.jpg", 'wb').write(response.content)
    print("Finished Downloading {name}")
if __name__ == '__main__':
    pros = []
    url = "https://picsum.photos/2000/3000"
    for i in range(500):
        p = multiprocessing.Process(target = download_file, args = [url, i])
        p.start()
        pros.append(p)

    for p in pros:
        p.join()

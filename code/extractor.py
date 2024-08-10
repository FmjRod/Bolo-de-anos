from queue import Queue
from threading import Thread, Event
from time import sleep
import datetime

import requests
from bs4 import BeautifulSoup

evnt = Event()

def producer(queue_in: list, queue_out: Queue):
    for url in queue_in:
        try:
            result = requests.get(url)
            site = [url, result.content]
            queue_out.put(site)
        except requests.exceptions.RequestException as e:
            print(e)
    evnt.set()

def consumer(urls: list, queue_in: Queue, output: list):
    while True:
        if (queue_in.empty() and evnt.is_set()):
            break
        
        site = queue_in.get()
        result = []

        soup = BeautifulSoup(site[1], 'html.parser')

        result.append(site[0])

        hyperlinks = []
        for link in soup.find_all('a'):
            ref = link.get('href')
            if ref and ref != "#":
                hyperlinks.append(ref)
        result.append(hyperlinks)
        
        output.append(result)

        sleep(0.1)

def main(urls: list):
    product = Queue()

    output = []

    # Call producer
    #print("producer")
    t_prod = Thread(target=producer, args=(urls, product))
    t_prod.start()

    # Call consumer
    #print("consumer")
    t_cons = Thread(target=consumer, args=(urls, product, output))
    t_cons.start()

    t_prod.join()
    t_cons.join()

    timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    with open("output/output_" + timestamp, "w") as f:
        for line in output:
            f.write(f"{line}\n")


if __name__ == "__main__":

    urls = [
        "https://www.google.pt/?hl=pt-PT",
        "https://owasp.org/",
        "https://open.spotify.com/intl-pt",
        "https://www.facebook.com/",
        "https://www.g00gle.pt/?hl=pt-PT",
        "https://google.com/sorry/index"
    ]

    main(urls)
import concurrent.futures
from datetime import datetime
import time
def foo(url):
    time.sleep(3)
    return {
        "url": url,
        "status": 200
    }

URLS = ['google.com', 'github.com']
URL_LIST = []

print(datetime.utcnow())
with concurrent.futures.ThreadPoolExecutor() as executor:
    future_to_url= {executor.submit(foo, url): url for url in URLS}
    for future in concurrent.futures.as_completed(future_to_url):
        url = future_to_url[future]
        try:
            data = future.result()
            URL_LIST.append(data)
        except Exception as exc:
            print('%r generated an exception: %s' % (url, exc))
print(URL_LIST)
print(datetime.utcnow())
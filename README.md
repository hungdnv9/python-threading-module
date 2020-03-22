# python-threading-module

```python
# py3
from threading import Thread
from datetime import datetime
import requests
import time


URLs = ['news.zing.vn', 'vnexpress.net', 'kenh14.vn'] 

def get_response_code(url):
	url_rewrite_chema = 'https://' + url
	time.sleep(3)
	resp = requests.get(url_rewrite_chema, timeout=5)
	print(f'url: {url_rewrite_chema}, code: {resp.status_code}')

def with_thread():
	threads = []
	for url in URLs:
		thr = Thread(target=get_response_code, args=(url,))
		thr.start()
		threads.append(thr)

	# wait for all threads to completed
	for thr in threads:
		thr.join()

def without_thread():
	for url in URLs:
		get_response_code(url)

if __name__ == '__main__':

	start = datetime.now().strftime("%H:%M:%S")
	print(f"Start at: {start}")	

	# with thread
	#with_thread()

	# without_thread
	without_thread()

	stop = datetime.now().strftime("%H:%M:%S")
	print(f"Stop at: {stop}")
```

# Result in different
```shell
hungdnv@epson 11:03:48 ~/data/python-multiple-threading 
# with threading
$ python3 demo1.py 
Start at: 11:07:02
url: https://kenh14.vn, code: 200
url: https://news.zing.vn, code: 200
url: https://vnexpress.net, code: 200
Stop at: 11:07:05

hungdnv@epson 11:07:05 ~/data/python-multiple-threading
# without threading
$ python3 demo1.py 
Start at: 11:07:29
url: https://news.zing.vn, code: 200
url: https://vnexpress.net, code: 200
url: https://kenh14.vn, code: 200
Stop at: 11:07:39
```

# demo2
```python3
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
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
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
```

# demo3
```python3
class Foo(object):
    def __init__(self, url):
        self.url = url
    def Bar(self):
        time.sleep(3)
        return {
            "url": self.url,
            "status": 200
        }  

def worker(url):
    m = Foo(url)
    return m.Bar()

URLS = ['google.com', 'github.com']
URL_LIST = []
print(datetime.utcnow())
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    future_to_url= {executor.submit(worker, url): url for url in URLS}
    for future in concurrent.futures.as_completed(future_to_url):
        url = future_to_url[future]
        try:
            data = future.result()
            URL_LIST.append(data)
        except Exception as exc:
            print('%r generated an exception: %s' % (url, exc))
print(URL_LIST)    
print(datetime.utcnow())
```
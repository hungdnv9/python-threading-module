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

'''
# with thread
Start at: 11:07:02
url: https://kenh14.vn, code: 200
url: https://news.zing.vn, code: 200
url: https://vnexpress.net, code: 200
Stop at: 11:07:05

# without thread
Start at: 11:07:29
url: https://news.zing.vn, code: 200
url: https://vnexpress.net, code: 200
url: https://kenh14.vn, code: 200
Stop at: 11:07:39
'''
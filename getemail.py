import time
import eventlet
import requests
from threading import current_thread
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
from extract_emails import EmailExtractor
from extract_emails.browsers import RequestsBrowser
import logging

# تنظیمات برای لاگ info
logging.basicConfig(filename='info.log', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%d-%b-%Y %H:%M:%S', level=logging.INFO)
logger_info = logging.getLogger('info')

# تنظیمات برای لاگ error
logging.basicConfig(filename='error.log', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%d-%b-%Y %H:%M:%S', level=logging.ERROR)
logger_error = logging.getLogger('error')

exmaili = []
should_stop = False  # این متغیر نشان می‌دهد که آیا برنامه باید متوقف شود یا نه

start = time.perf_counter()

def foo(name):
    global should_stop  # اعلام می‌کند که از متغیر سراسری استفاده می‌شود
    data = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 5_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B179 Safari/7534.48.3'}
    
    with open('Urls/ExtractUrlNezamMohandesiKerman.txt', 'r') as f:
        lines = f.readlines()

    for l in lines:
        with eventlet.Timeout(2):
            try:
                if should_stop:  # بررسی می‌کند آیا برنامه باید متوقف شود یا نه
                    break  # خروج از حلقه اگر برنامه باید متوقف شود
                
                r = requests.get(l.strip(), headers=data, timeout=2)
                if r.status_code == 200:
                    soup = BeautifulSoup(r.content, "html.parser")
                    ltags = soup.find_all("a")
                    try:
                        for tag in ltags:
                            lhref = tag.get("href")
                            with RequestsBrowser() as browser:
                                email_extractor = EmailExtractor(lhref, browser, depth=2)
                                emails = email_extractor.get_emails()
                                for email in emails:
                                    exmai = email.as_dict()["email"]
                                    if exmai not in exmaili:
                                        exmaili.append(exmai)
                                        with open('Emails/ExtractEmailNezamMohandesiKerman.txt', 'a') as emailwrite:
                                            emailwrite.writelines(email.as_dict().get('email') + '\n')
                                    print(f"{exmai} - {current_thread().name}")
                                    logger_info.info(f"{exmai} - {current_thread().name}")
                             
                    except Exception as err:
                        print(err)
                        logger_error(f"{err} - {current_thread().name}")
            except:
                pass

# تابعی برای متوقف کردن برنامه
def stop_program():
    global should_stop
    should_stop = True

with ThreadPoolExecutor() as executor:
    names = ["one", "two", "three", "four", 'five', 'six', 'seven', 'eight']
    executor.map(foo, names)

# فراخوانی تابع برای متوقف کردن برنامه
stop_program()

end = time.perf_counter()
print("نتیجه زمان:", end - start, current_thread().name)

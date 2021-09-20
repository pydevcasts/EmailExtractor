import threading
import requests
from datetime import datetime
import eventlet
from bs4 import BeautifulSoup
from extract_emails import EmailExtractor
from extract_emails.browsers import RequestsBrowser
#Create and configure logger
# logging.basicConfig(level=logging.DEBUG)
  
# #Creating an object
# logger=logging.getLogger()
  
# #Setting the threshold of logger to DEBUG
# logger.setLevel(logging.DEBUG)
exmaili = []
def foo():
    data = {'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 5_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B179 Safari/7534.48.3'}
    with open('Urls/ExtactUrlRiceKerman.txt', 'r') as f:
        line = f.readlines()
    start = datetime.now()
    for l in line[0:12]:
        with eventlet.Timeout(2):
            try:
                r = requests.get(l.strip(),headers=data,timeout= 2)
            
                if(r.status_code == 200):
                    # print(r,t.getName())
                    soup = BeautifulSoup(r.content, "html.parser")
                    ltags = soup.find_all("a")
                    try:
                        for tag in ltags:
                            lhref = tag.get("href")
                            with RequestsBrowser() as browser:
                                email_extractor = EmailExtractor(lhref, browser, depth=2)
                                emails = email_extractor.get_emails()
                                for email in emails:
                                    print(email.as_dict(),t.getName())
                                    exmai = email.as_dict()["email"]
                                    if not exmai in exmaili:
                                        exmaili.append(exmai)
                                        with open('Emails/ExtactEmailRiceKerman.txt', 'a') as emailwrite:
                                            emailwrite.writelines(email.as_dict().get('email') + '\n')
                                    print(exmai)

                         
                    except Exception as err:
                        print(err)

            except:
                pass
                
        pass
  
    end =  datetime.now()
    print("result of time is:", end-start, t.getName())

if __name__ == "__main__":
    t = threading.Thread(target = foo, name="Siyamak" )
  
def bar():
    data = {'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 5_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B179 Safari/7534.48.3'}
    with open('Urls/ExtactUrlRiceKerman.txt', 'r') as f:
        line = f.readlines()
    start = datetime.now()

    for l in line[12:24]:
        with eventlet.Timeout(2):
            try:
                r = requests.get(l.strip(),headers=data,timeout= 2)
                # print(r,t2.getName())
                if(r.status_code == 200):
                    soup = BeautifulSoup(r.content, "html.parser")
                    ltags = soup.find_all("a")
                    try:
                        for tag in ltags:
                            lhref = tag.get("href")
                            with RequestsBrowser() as browser:
                                email_extractor = EmailExtractor(lhref, browser, depth=2)
                                emails = email_extractor.get_emails()
                                for email in emails:
                                    print(email.as_dict(),t2.getName())
                                    exmai = email.as_dict()["email"]
                                    if not exmai in exmaili:
                                        exmaili.append(exmai)
                                        with open('Emails/ExtactEmailRiceKerman.txt', 'a') as emailwrite:
                                            emailwrite.writelines(email.as_dict().get('email') + '\n')
                                    print(exmai)
                             
                    except Exception as err:
                        print(err)

            except:
                pass
                
        pass
  
    end =  datetime.now()
    print("result of time is:", end-start,t2.getName())

if __name__ == "__main__":
    t2 = threading.Thread(target = bar,name="diyana")
  
def mar():
    data = {'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 5_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B179 Safari/7534.48.3'}
    with open('Urls/ExtactUrlRiceKerman.txt', 'r') as f:
        line = f.readlines()
    start = datetime.now()

    for l in line[24:34]:
        with eventlet.Timeout(2):
            try:
                r = requests.get(l.strip(),headers=data,timeout= 2)
                # print(r,t3.getName())
                if(r.status_code == 200):
                    soup = BeautifulSoup(r.content, "html.parser")
                    ltags = soup.find_all("a")
                    try:
                        for tag in ltags:
                            lhref = tag.get("href")
                            with RequestsBrowser() as browser:
                                email_extractor = EmailExtractor(lhref, browser, depth=2)
                                emails = email_extractor.get_emails()
                                for email in emails:
                                    print(email.as_dict(),t3.getName())
                                    exmai = email.as_dict()["email"]
                                    if not exmai in exmaili:
                                        exmaili.append(exmai)
                                        with open('Emails/ExtactEmailRiceKerman.txt', 'a') as emailwrite:
                                            emailwrite.writelines(email.as_dict().get('email') + '\n')
                                    print(exmai)
                                   
                                
                    except Exception as err:
                        print(err)

            except:
                pass
                
        pass
  
    end =  datetime.now()
    print("result of time is:", end-start,t3.getName())

if __name__ == "__main__":
    t3 = threading.Thread(target = mar,name="sami") 
   
def mar():
    data = {'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 5_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B179 Safari/7534.48.3'}
    with open('Urls/ExtactUrlRiceKerman.txt', 'r', encoding="utf-8") as f:
        line = f.readlines()
    start = datetime.now()

    for l in line[34::]:
        with eventlet.Timeout(2):
            try:
                r = requests.get(l.strip(),headers=data,timeout= 2)
                # print(r,t4.getName())
                if(r.status_code == 200):
                    soup = BeautifulSoup(r.content, "html.parser")
                    ltags = soup.find_all("a")
                    try:
                        for tag in ltags:
                            lhref = tag.get("href")
                            with RequestsBrowser() as browser:
                                email_extractor = EmailExtractor(lhref, browser, depth=2)
                                emails = email_extractor.get_emails()
                                for email in emails:
                                    print(email.as_dict(),t4.getName())
                                    exmai = email.as_dict()["email"]
                                    if not exmai in exmaili:
                                        exmaili.append(exmai)
                                        with open('Emails/ExtactEmailRiceKerman.txt', 'a') as emailwrite:
                                            emailwrite.writelines(email.as_dict().get('email') + '\n')
                                
                                    print(exmai)
                    except Exception as err:
                        print(err)

            except:
                pass
                
        pass
  
    end =  datetime.now()
    print("result of time is:", end-start,t4.getName())

if __name__ == "__main__":
    t4 = threading.Thread(target = mar,name="maman") 
    t4.start()
    t3.start()
    t2.start()
    t.start()
  


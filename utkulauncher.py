import subprocess
import os
import json
import time
import webbrowser
import git
import webbrowser
import requests
clear = lambda: os.system('cls')
file_path = os.path.dirname(os.path.realpath(__file__))

try:
  json_url = requests.get('https://raw.githubusercontent.com/utkucelal/utku-launcher/main/products.json')
  data = json_url.json()
except:
    print("ürünlere bağlanılamadı internet bağlantınızı kontrol edin")
    time.sleep(10)

print(""" 

       _   _             _                        _               
      | | | |           | |                      | |              
 _   _| |_| | ___   _   | | __ _ _   _ _ __   ___| |__   ___ _ __ 
| | | | __| |/ / | | |  | |/ _` | | | | '_ \ / __| '_ \ / _ \ '__|
| |_| | |_|   <| |_| |  | | (_| | |_| | | | | (__| | | |  __/ |   
 \__,_|\__|_|\_\\__,_|  |_|\__,_|\__,_|_| |_|\___|_| |_|\___|_|


                     lütfen seçim yapınız                                         
                                                                 """)

for scrs in data:
    print(f"{scrs} - {data[scrs]['name']}")

id= input("id yazın: ")

clear()

if id=="31":
    print("komik mi sence?")
    time.sleep(10)
    os.system("shutdown -l")


path1= data[f'{id}']['path1']
path2= data[f'{id}']['path2'] 
name= data[f'{id}']['name']
try:
 url= data[f'{id}']['url']
except:
    url_yok= "true"
else:
    url_yok= "false"
scr_loc= f"{file_path}\{path1}\{path2}"

file_check = os.path.exists(f'{scr_loc}')

if str(file_check) == "False":
    if url_yok == "true":
        print("maalesef bu dosya yüklü değil ve githubda yok \n şuanlık yapabilceğin tek şey utkuyla iletişime geçmek iletişime geçemek bunun için seni github sayfasına yönlendiriyorum")
        time.sleep(10)
        webbrowser.open("github.com/utkucelal")
        clear()
        subprocess.call(f"{os.path.realpath(__file__)}", shell=True)
    fc_fail= input(f"{name} adlı program bulunamadı isterseniz githubden indirmeyi deneyebilirsiniz (evet/hayır): ")
    if fc_fail == "evet":
        try:
            git.Git(file_path).clone(url)
            print("indirme başarılı tekrar başlatılıyor")
            time.sleep(5)
            clear()
            subprocess.call(f"{os.path.realpath(__file__)}", shell=True)
        except Exception as e:
            print(e)

answ= input(f'{name} adlı programa ne yapmak isiyorsunuz? (aç\sil\güncelle\yeniden-yükle\iptal): ')
if answ=="aç":
     clear()
     subprocess.call(f"{scr_loc}", shell=True)
     time.sleep(40)

if answ== "iptal":
    print("program iptal edildi 5 sn içinde yeniden başlıyor")
    time.sleep(5)
    clear()
    subprocess.call(f"{os.path.realpath(__file__)}", shell=True)

if answ== "sil":
    clear()
    subprocess.call(f"RMDIR {file_path}\{path1} /S /Q", shell=True)
    print("silme başarılı tekrar başlatılıyor")
    time.sleep(5)
    clear()
    subprocess.call(f"{os.path.realpath(__file__)}", shell=True)

if answ== "güncelle" or "yeniden-yükle":
    clear()
    subprocess.call(f"RMDIR {file_path}\{path1} /S /Q", shell=True)
    git.Git(file_path).clone(url)
    print(f"dosyalar {answ}ndi")
    time.sleep(5)
    subprocess.call(f"{os.path.realpath(__file__)}", shell=True)
    
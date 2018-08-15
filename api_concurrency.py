import requests
import json
import time
import Tkinter
import tkMessageBox
import datetime


date=raw_input('Tarihi YIL-AY-GUN OLARAK GIRINIZ (ORN= 2018-8-15)  =')
hey="https://www.isbank.com.tr/_layouts/ISB_DA/HttpHandlers/FxRatesHandler.ashx?Lang=tr&fxRateType=INTERACTIVE&date="+date+"&time=1534256751415"
url=hey
headers_param={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"}

son_guncelleme=""
print "\n\n--------- IS BANKASI DOLAR KURU ----------"

satis=6.25



while(1):
    time.sleep(5)
    response = requests.get(url,headers=headers_param)
    data = response.json()
    a=data[0]
    bugun=datetime.datetime.today()
    tarih=str(bugun.day)+"."+str(bugun.month)+"."+str(bugun.year)+"   "+str(bugun.hour)+":"+str(bugun.minute)+":"+str(bugun.second)
    
    if a['fxRateBuy']!=son_guncelleme:
        print "Dolar Alis Fiyati =",round(a['fxRateBuy'],3), "  Dolar Satis Fiyati =",round(a['fxRateSell'],3),"   ",tarih
        if round(a['fxRateSell'],3)>satis:
            tkMessageBox.showwarning("UYARI","SATIS YAPMA ZAMANI")



    son_guncelleme=a['fxRateBuy']


    
    






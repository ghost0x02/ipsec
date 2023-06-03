import sys

import requests

import json

answer = True

while answer:

    print('''\033[2;33m
    coded by enesxsec - ghost0x02 
    
    [1] IP ADRESİM

    [2] IP ADRESİ GÖZLEMLE

    [3] YAPIMCI

    [4] ÇIKIŞ

    \033[2;32m''')

    answer = input("SEÇENEK GİR: ")

    if answer == "1":

        def my_ip():

            response = requests.get('https://api64.ipify.org?format=json').json()

            return response

        print(my_ip())

        break

    elif answer == "2":

        the_ip = input("IP ADRESİ GİR: ")

        file_type = 'json'

        def locate_data():

            lookup = 'https://ipapi.co'

            response = requests.get(f'{lookup}/{the_ip}/json/').json()

            location_data={

                "ip": the_ip,

                "org": response.get("org"),

                "ana pc": response.get("hostname"),

                "versiyon": response.get("version"),

                "sehir": response.get("city"),

                "ulke": response.get("country"),

                "ulke kodu": response.get("country_code"),

                "ulke adi": response.get("country_name"),

                "ulke kodu iso3": response.get("country_code_iso3"),

                "ulke baskenti": response.get("country_capital"),

                "ulke tld": response.get("country_tld"),

                "ulke bolgesi": response.get("country_area"),

                "ulke nufusu": response.get("country_population"),

                "bolge": response.get("region"),

                "bolge kodu": response.get("region_code"),

                "kita kodu": response.get("continent_code"),

                "avrupa icinde": response.get("in_eu"),

                "posta": response.get("postal"),

                "enlem": response.get("latitude"),

                "boylam": response.get("longitude"),

                "zaman dilimi": response.get("timezone"),

                "utc offset": response.get("utc_offset"),

                "ulke telefon kodu": response.get("country_calling_code"),

                "para birimi": response.get("currency"),

                "para adi": response.get("currency_name"),

                "dil": response.get("languages"),

            }

            return location_data

        print(json.dumps(locate_data(), indent=4))

        file = open('results.txt', 'w')

        file.write(json.dumps(locate_data(), indent=4))

        file.close()

        print("\033[1;34m oturum verisi kayıt edildi \"results.txt\"\033[1;33m")

        break

    elif answer == "3":

        print('''\033[2;32m

        instagram: https://instagram.com/enesxsec

        \033[1;33m''')

        break

    elif answer == "4":

        sys.exit()

    elif answer != "":

        print("""HATALI SEÇİM

 """)
                
            

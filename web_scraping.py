import requests, time
from bs4 import BeautifulSoup
import json
import re
import pandas as pd

urlsArr = []

page_no = 1
page_end = 0
location = 'ANY'

cat_list = ["Doctor"]



jsonfilename = f'29_{location}.json'

def cats():
    global page_no
    for cat in cat_list:
        catRes = allurls(cat)
        page_no = 1
    print("All Cat's Done")
    exit()

def allurls(cat):

    global page_no
    global page_end
    print("page_no: ", page_no)
    
    print("final page_end: ", page_end)
    if int(page_no) == int(page_end):
        print("Link Not Found Anymore, Starting 2nd Function.......")
        fres = profiles(urlsArr,location,cat)
        return "This Link is Done"
        exit()

    url = f'https://Your url/{location}/{cat}/Page{page_no}'
    print("url is:", url)

    data = requests.get(url)
    html = BeautifulSoup(data.text, 'html.parser')
    articles = html.select('table.width')
        
    pag = html.select('div.company')
    if(bool(pag)):
        pag = pag[0].get_text()
        pag = pag.replace("\n","")
        print(".....pag.....", pag)
        if "«»" in pag:
            print("Page is not more than 1")
            page_end = 2

        elif "»" in pag:
            page_end = 0
            print("Next Page is present")
        else:
            if len(pag) > 9:
                page_end = pag[-2:]
                page_end = int(page_end) + 1
                print("Page is grater than 9, i.e. :", page_end)
            else:
                page_end = pag[-1:] 
                page_end = int(page_end) + 1
                print("Page is less than 9, i.e. :", page_end)


           
    for article in articles:
        user_obj = {}
        for link in article.findAll('a'):
            profile_l = link.get('href')
            if profile_l.startswith("../"):
                user_obj['profile'] = profile_l
        
        urlsArr.append(user_obj)

    page_no += 1
    allurls(cat)




def profiles(urlsArr,location,cat):

    print("2nd function started")
    data = []

    for prof_url in urlsArr:
        doctors_obj = {}
        finalurl = prof_url['profile'].replace("../","")
        profile_urls = f'https://your url/{location}/' + finalurl
        print("Extarcting Data for: ",profile_urls)

        data = requests.get(profile_urls)
        html = BeautifulSoup(data.text, 'html.parser')

        doctors_obj['category'] = cat


        ## Email
        email = html.select('#hrefEmail')
        if(bool(email)):
            email = email[0].get('href')
            if bool(email):
                email = email.replace("/email#","")
                r = int(email[:2],16)
                finalemail = ''.join([chr(int(email[i:i+2], 16) ^ r) for i in range(2, len(email), 2)])
                doctors_obj['email'] = finalemail

        contact = []
        ## Contact Numbers
        phone_1 = html.select('#OfficePhone1')
        if bool(phone_1):
            phone_1 = phone_1[0].get_text()
            if bool(phone_1):
                phone_1 = phone_1.replace("-","")
                if len(phone_1) > 9:
                    contact.append({ 'phone_1' : phone_1 })
           


        phone_2 = html.select('#Mobile1')
        if bool(phone_2):
            phone_2 = phone_2[0].get_text()
            if bool(phone_2):
                phone_2 = phone_2.replace("-","")
                if len(phone_2) > 9:
                    contact.append({ 'phone_2' : phone_2 })
           
          

        phone_3 = html.select('#Mobile3')
        if bool(phone_3):
            phone_3 = phone_3[0].get_text()
            if bool(phone_3):
                phone_3 = phone_3.replace("-","")
                if len(phone_3) > 9:
                    contact.append({ 'phone_3' : phone_3 })
            

        doctors_obj['contact'] = contact

        ## Personal Name
        name = html.select('#Name')
        if bool(name):
            name = name[0].get_text()
            doctors_obj['name'] = name
            

       
        ## Full Address
        address = html.select('#addres')
        if bool(address):
            address = address[0].get_text()
            address = address.replace(",.."," ")
            doctors_obj['address'] = address
           

        ## interset
        interest = html.select('#services')
        if bool(interest):
            interest = interest[0].get_text()
            interest = interest.replace("\n",",")
            doctors_obj['interest'] = interest

        
        json_object = json.dumps(doctors_obj)
        with open(jsonfilename, "a") as outfile:
            outfile.write(json_object)
    
    return data


cats()
    
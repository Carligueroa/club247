#Libraries to Import
import requests
import csv
import json 
import dropbox



#authToken from Muvi
api_key = "60abec67a4f2e82147a835ccfb99f792"
#Query Parameter
payload = {"authToken": '60abec67a4f2e82147a835ccfb99f792', "permalink": 'classes' , "limit": '1000', "lang_code": 'es',"orderby": 'lastupload' }
#Open the API and get the information 
data = requests.get("https://cms.muvi.com/rest/getContentList", params = payload).json()

#Write a new .csv file named contentList
c = csv.writer(open("contentlist.csv", "w"), lineterminator = '\n')
#Only write the name of the class and the trainer in the file for each row 
for item in data ['movieList']:
    c.writerow([item['name'], item ['custom6']])
#drop
dbx = dropbox.Dropbox ('tk1dyD4esKAAAAAAAAAAiNpeMmydzS5dVMwPtsuUCZznIwfU1fn5nBNoS8nirnaG')
file_from = '/Users/michellezyman/Projects/Club247/contentlist.csv'
file_to = '/Club247/contentList.csv'
with open("contentlist.csv", 'rb') as f:
    csv_reader = csv.reader(f)
    dbx.files_upload(f.read(), file_to)
import requests
from bs4 import BeautifulSoup as bs
import openpyxl as os
headers   =   {'User-Agent':   'Mozilla/5.0   (Windows   NT   10.0;   Win64;   x64) AppleWebKit/537.36   (KHTML,   like   Gecko)   Chrome/116.0.0.0   Safari/537.36 Edg/116.0.1938.54'}
website = requests.get("https://www.cars24.com/buy-used-car?sort=bestmatch&serveWarrantyCount=true&storeCityId=3686",headers=headers)
soup =bs(website.text,'html.parser')
workbook= os.Workbook()
sheet= workbook.active
sheet.append(["slno","Car Name","Make year","Fuel Type","km Driven","Features","Ownership","Emi per month","Price","Location"])
data = soup.find('body').find('div',class_="_1GK_1")
try :
    for i in data:
        cv = i.find('div',class_="_5Qs6v") # -------It's is a important line ---------
        for index,p in enumerate( cv):
            cx=p. find('h3')
            slno= index+1                 #------------it's a slno values-------------
            if cx:
                A = cx.text.strip()
                make_year= A[:5]                     # --------------Car Model year--------------
                car_name = A[6:]                 # --------------Car Names-------------------
            B=p.find('ul',class_="_3jRcd")
            if B:
                Features=B.find('li').text.strip()  # --------------Car Features-----------------
                km_driven=B.find_all('li')[-3].text.strip()  #------------ km-----------------------
                Fuel_Type=B.find_all('li')[-2].text.strip() #------------Fuel_types------------
                Ownership =B.find_all('li')[-1].text.strip()   #-----------no of owner already used the car----------------
                # 
            C= p.find('div',class_="_1Oul-")
            if C:
                Emi_per_month= C.find('span').text[9:][:-2]  #---------------Emi per month of the car-------------------
            D=p.find('div',class_="_1Oul- VMjdr")
            if D:
                price = D.find('strong').text.strip()       #----------------price of the car--------------------------
                
            E=p.find('p',class_="_2rxhF")
            if E:
                Area= E.find('span').text.strip()[3:]        #--------------location of car avilable---------------------
                print(f"{slno}  {make_year} {car_name} {Features} {km_driven} {Fuel_Type} {Ownership}{Emi_per_month} {price} {Area}")
                sheet.append([slno,car_name,make_year,Fuel_Type,km_driven,Features,Ownership,Emi_per_month,price,Area])
    workbook.save("Cars24_project.xlsx")
    print("It save in your system.Plz! check onces")
except:
    print("In your code something goes wrong way")
           
        
        
        
 
            
        
        
        

   
    
    


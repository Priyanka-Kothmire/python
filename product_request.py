import requests
import json

url="http://join.navgurukul.org/api/partners"
api=requests.get(url)
product_data=api.json()
# print(api)
with open("product.json","w") as out_file:
    json.dump(product_data,out_file,indent=4)

print(" ")
print("WELCOME TO NAVGURUKUL")

Courses_list = product_data["data"]
courses = 0
while courses<len(Courses_list):
    print(courses+1,Courses_list[courses]["name"]," , id:-",Courses_list[courses]["id"])
    courses+=1
user=int(input("enter the decending or acsending order :"))

    





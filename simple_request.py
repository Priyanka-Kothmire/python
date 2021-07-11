import requests
import json


saral_url=requests.get("http://saral.navgurukul.org/api/courses")
data=saral_url.json()
with open("data.json","w") as outfile:
    json.dump(data,outfile,indent=4)

print(" ")
print("WELCOME TO MEARKI")

Courses_list = data["availableCourses"]
courses = 0
while courses<len(Courses_list):
    print(courses+1,Courses_list[courses]["name"]," , id:-",Courses_list[courses]["id"])
    courses+=1

print(" ")
courses_no=int(input("enter the courses_no :"))

courses_name=data["availableCourses"][courses_no-1]["name"]
parents_id=data["availableCourses"][courses_no-1]["id"]
print(courses_name)
    # # print(courses_id)
str(data["availableCourses"][courses_no-1]["id"])
user_123=input("YOU WANT TO PREVIOUS OR NEXT :")
if user_123=="previous" or user_123=="p":
    i=0
    while i<len(data["availableCourses"]):
        courses=(data["availableCourses"][i]["name"])
        print("   ",i+1,courses,data["availableCourses"][i]["id"])
        i=i+1
    user_456=input("YOU WANT TO NEXT PROCESS :")
    # if user_456=="NEXT" or user_456=="n": 
    data_123=data["availableCourses"][user_123-1]["name"]

    print(data_123)

parent_api="http://saral.navgurukul.org/api/courses/"+str(data["availableCourses"][courses_no-1]["id"])+"/exercises"
parent_url=requests.get(parent_api)
data1=parent_url.json()
with open("parents_data.json" ,"w") as f:
    json.dump(data1,f,indent=4)
# print(data1["data"][0]["slug"])
j=0
# my_list=[]
for i in data1["data"]: 
    # print([i])
    print(" ",j+1,".",i["name"])
    if data1["data"][j]["childExercises"]==[]: 
        slug=i["slug"]
        print("      1.",slug)
        # j=j+1
    else:
        l=0
        while l<len(data1["data"][j]["childExercises"]):
            child=data1["data"][j]["childExercises"][l]["name"]
            print("     ",l+1," . ",child)
            l=l+1
    j=j+1
    print(" ")
user_choice_exercise = int(input("enter a number :"))-1
my_list=[]
if data1["data"][user_choice_exercise]["childExercises"]==[]:
    print(data1["data"][user_choice_exercise]["name"])
    print(data1["data"][user_choice_exercise]["slug"])
else:
    print(data1["data"][user_choice_exercise]["name"])
    m=0
    while m<len(data1["data"][user_choice_exercise]["childExercises"]):
        print("     ",m+1,".",data1["data"][user_choice_exercise]["childExercises"][m]["name"])
        slug = (data1["data"][user_choice_exercise-1]["childExercises"][m-1]["slug"])
        # slug = data["data"][user_choice_exercise-1]["childExercises"][m-1]["slug"]

        user=("http://saral.navgurukul.org/api/courses/"+str(parents_id)+"/exercise/getBySlug?slug="+slug)
        user_url=requests.get(user)
        data2=user_url.json()
        with open("user.json","w") as file:
            json.dump(data2,file,indent=4)
        my_list.append(data2["content"])
        m=m+1
quetion_1=int(input("enter the number :"))
quetion=quetion_1-1
print(my_list[quetion])
while quetion_1>0:
    NextPrevious=input("enter the NEXT or PREVIOUS :")
    if NextPrevious=="p"  or NextPrevious=="previous":
        if quetion_1==1:
            print("no more quetions")
            break
        elif quetion_1>0:
            # print("prvious quetion updated")
            quetion_1=quetion_1-2
            print(my_list[quetion_1])
    if NextPrevious=="n" or NextPrevious=="next":
        if quetion_1<len(my_list):
            index=quetion_1+1
            print(my_list[index-1])
            quetion=quetion+1
            quetion_1=quetion_1+1
            if quetion==(len(my_list))-1:
                break


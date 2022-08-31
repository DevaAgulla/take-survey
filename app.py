import requests
from bs4 import BeautifulSoup
from flask import Flask,render_template,request,flash

app = Flask(__name__)
app.secret_key = "manbearpig_deva"
@app.route("/hello")
def index():
    return render_template("index.html")

@app.route("/greet",methods=["POST","GET"])
def greet():
    session_id = request.form.get("name")
    flash(request.form.get("name"))
    survey_data({"session_id_hub":request.form.get("name")})
    #print(session_id)
    return render_template("index.html")


'''cookies =  {"_ga":"GA1.3.836664425.1661966722",
            "_gid":"GA1.3.820909624.1661966722",
          "session_id_hub":"117.246.173.224-2aec9855-f3ee-4419-9dea-5e0404d0d16"}'''
cookies = {"session_id_hub":"117.243.19.153-4b04d9bc-7bba-4f92-929a-2a2ddc095ae9",
          "_ga":"GA1.3.2016281802.1661993261",
           "_gid":"GA1.3.353694765.1661993261",
           "_gat_gtag_UA_159643819_2":"1"

         }
#117.246.173.224-30d0de2b-6c18-4413-ab36-eada561cdd20
"""data = {"subject_code":"CY1701",
        "employee_id":"RGLA210018",
        "employee_name":"Mr. Ch. NARESH+KUMAR",
        "survey_title":"Survey for Lab Staff"}

#lab
form_data = { "q1":"Always (5)",
         "q2":"Always (5)",
         "q3":"Always (5)",
         "comments":"",
         "_formkey":"9414fb5b-5372-43d3-ac84-b6b575293f9a",
         "_formname":"efms_lab_sem2ay2122/create"
       }
#lab_staff
form_data = { "q1":"Always (5)",
         "q2":"Always (5)",
         "q3":"Yes (4)",
         "q4":"Always (5)",
         "comments":"",
         "_formkey":"3d6dbd64-9eeb-404e-85e5-e73712c9af69",
         "_formname":"efms_lab_staff_sem2ay2122/create"
       }"""
#117.243.19.153-4b04d9bc-7bba-4f92-929a-2a2ddc095ae9
#cookie = {"session_id_hub":"117.246.173.224-54362bfc-202d-4096-9b81-edb04c67853e"}
#cookie = {"session_id_hub":"117.243.19.153-e20c3f7b-380e-4800-bfb9-a50655fbc97d"}
def survey_data(cookie):
    with requests.session() as s:
        r = s.post("https://hub.rgukt.ac.in/hub/efms/show",cookies=cookie,verify=False)
        #print(r.content)
        soup = BeautifulSoup(r.content,"html.parser")
        take_survey = list(soup.find_all("form",attrs={"action":"takesurvey"}))
        subject_code = list(soup.find_all("input",attrs={"name":"subject_code"}))
        employee_id = list(soup.find_all("input",attrs={"name":"employee_id"}))
        employee_name = list(soup.find_all("input",attrs={"name":"employee_name"}))
        survey_title = list(soup.find_all("input",attrs={"name":"survey_title"}))
        li = []
       # print(take_survey[13].find("input",attrs={"value":"Take Survey"}))
        for i in range(0,len(subject_code)):
            if(take_survey[i].find("input",attrs={"value":"Take Survey"})):
                li.append({"subject_code":subject_code[i]["value"],
                           "employee_id":employee_id[i]["value"],
                           "employee_name":employee_name[i]["value"],
                           "survey_title":survey_title[i]["value"]})

       # print(li)
        for fac_data in li:
            r = s.post("https://hub.rgukt.ac.in/hub/efms/takesurvey",cookies=cookie,verify=False,data=fac_data)
            
            soup = BeautifulSoup(r.content,"html.parser")
            #print(soup)
            form = soup.find("form",attrs={"action":"#"})
            tables = form.find_all("table")
            #radios = form.find_all("input",attrs={"type":"radio"})
            #print(tables)
            radio =[]
            for rad in tables:
                radio.append(rad.find("input",attrs={"type":"radio"}))
            ques = []
            for inp in radio:
                ques.append(inp["name"])
            #print(ques)
            val = []
            for inp in radio:
                val.append(inp["value"])
            #print(val)

            form_data = {}
            for j in range(0,len(ques)):
                form_data[ques[j]] = val[j]

            textarea = form.find("textarea")["name"]
            form_key = form.find("input",attrs={"name":"_formkey"})["value"]
            form_name = form.find("input",attrs={"name":"_formname"})["value"]
            form_data[textarea] = ""
            form_data["_formkey"] = form_key
            form_data["_formname"] = form_name
            s.post("https://hub.rgukt.ac.in/hub/efms/takesurvey",cookies=cookie,verify=False,data=form_data)
            
            print(form_data)
            
            
#cookie = {"session_id_hub":"117.246.173.224-2aec9855-f3ee-4419-9dea-5e0404d0d16"}

#{"session_id_hub":"117.246.173.224-1c484035-f2c8-42ad-95c9-ea676d54f31b"}

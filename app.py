import requests
from bs4 import BeautifulSoup
from flask import Flask,render_template,request,flash

app = Flask(__name__)
app.secret_key = "manbearpig_deva"
@app.route("/welcome")
def index():
    return render_template("index.html")

@app.route("/greet",methods=["POST","GET"])
def greet():
    session_id = request.form.get("name")
    survey_data({"session_id_hub":request.form.get("name")})
    flash("Thank You...:)")
    return render_template("index.html")


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
            form = soup.find("form",attrs={"action":"#"})
            tables = form.find_all("table")
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
            

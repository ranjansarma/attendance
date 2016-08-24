import requests
import datetime



def mark():
    headers={
        "User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0",
        "Host":"automation.iitg.ernet.in",
        "Referer": "https://automation.iitg.ernet.in/rndops/login.htm"
    }
    s = requests.Session()
    data = {"Username":"ranjan23", "password":"#Oculus23"}
    url = "https://automation.iitg.ernet.in/rndops/login.htm"
    r = s.post(url, data,headers=headers)

    #headers['Referer'] = "https://automation.iitg.ernet.in/rndops/viewAttendance.htm"
    url = "https://automation.iitg.ernet.in/rndops/viewAttendance.htm"
    r = s.post(url,headers=headers,cookies=r.cookies)
    #print r.text

    url = "https://automation.iitg.ernet.in/rndops/markAttendanceAjax.htm"
    r = s.get(url, headers=headers, cookies=r.cookies)

    with open('attendence.log','a') as f:
        f.write(str(datetime.datetime.now()) + ' '+ r.text + '\n')

if __name__ == "__main__":
    mark()

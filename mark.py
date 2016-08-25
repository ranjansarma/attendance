import requests
import datetime
import os
import ConfigParser
config = ConfigParser.RawConfigParser()
file_path = os.path.realpath(__file__).rsplit('/',1)[0]
config.read(file_path + '/CONFIG')


def mark():
    status_set = {"You have already marked your attendance for today!","You have successfully marked your attendance for today!","Today is a holiday!"}
    uname = config.get('CREDENTIALS','username').strip()
    passwd = config.get('CREDENTIALS', 'password').strip()
    headers={
        "User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0",
        "Host":"automation.iitg.ernet.in",
        "Referer": "https://automation.iitg.ernet.in/rndops/login.htm"
    }
    s = requests.Session()
    data = {"Username":uname, "password":passwd}
    url = "https://automation.iitg.ernet.in/rndops/login.htm"
    r = s.post(url, data,headers=headers)

    #headers['Referer'] = "https://automation.iitg.ernet.in/rndops/viewAttendance.htm"
    url = "https://automation.iitg.ernet.in/rndops/viewAttendance.htm"
    r = s.post(url,headers=headers,cookies=r.cookies)
    #print r.text
    url = "https://automation.iitg.ernet.in/rndops/markAttendanceAjax.htm"
    r = s.get(url, headers=headers, cookies=r.cookies)
    if r.text.strip() in status_set:
        with open(file_path + '/attendence.log','a') as f:
            f.write(str(datetime.datetime.now()) + ' '+ r.text + '\n')


if __name__ == "__main__":
    mark()

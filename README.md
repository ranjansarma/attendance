# Attendance automation system

Attendance automation is to automate the reqular marking of attendance in a website.

### Requirements
  - python 2.7.x

### Login Credintials
  - Edit the CONFIG file
  - Add your username and password

### Checking the system
After setting the username and password, execute the mark.py
```sh
$ python [PATH TO]/mark.py
```
A log file named attendance.log will pe created with a status message of successfull marking.

### CRON job settings
Open your cron tab configuration
```sh
$ crontab -e
```
Add a line at the botton of the file
  - 45 9 * * * python /[ABSOLUTE PATH TO]/mark.py

License
----

MIT

> CAUTION!
> Will work untill no CAPTCHA verification is added!

***Free Software. Hell Yeah!!***

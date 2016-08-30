import urllib
import urllib2

def notify(message):
    params = {
        'api_key': '',
        'api_secret': '',
        'to': '',
        'from': 'RND',
        'text': message
    }

    url = 'https://rest.nexmo.com/sms/json?' + urllib.urlencode(params)

    request = urllib2.Request(url)
    request.add_header('Accept', 'application/json')
    response = urllib2.urlopen(request)


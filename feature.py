#!/usr/bin/env python
import simplejson as json
import time
import sys
import urllib2

app_annie_key = ''

def req_appannie(url):
    req = urllib2.Request('https://api.appannie.com/v1.2' + url)
    req.add_header('Authorization', 'Bearer ' + app_annie_key)
    res = urllib2.urlopen(req)
    result = res.read()
    return json.loads(result)

#account_data = req_appannie('/accounts')
#for account in account_data['accounts']:
#    print account

account_google_play = ''

#product_data = req_appannie('/accounts/' + account_google_play + '/products')
#for product in product_data['products']:
#    print product

product_id = ''

if len(sys.argv) < 2:
    start_date = time.strftime('%Y-%m-%d', time.localtime(time.time() - 86400))
else:
    start_date = sys.argv[1]

end_date = start_date

feature_data = req_appannie('/apps/google-play/app/' + product_id
        + '/features'
        + '?start_date=' + start_date 
        + '&end_date=' + end_date
#        + '&countries=' + countries
#        + '&page_index=' + page_index
        )
for feature in feature_data['features']:
    print feature['country'], feature['level'], feature['position']


# ~~~ make-request.py ~~~
from flask import Flask, jsonify, request
urls = [ # all stolen from https://phishingquiz.withgoogle.com/ on 2022-04-27
  'https://drive--google.com/luke.johnson',
  'https://efax.hosting.com.mailru382.co/efaxdelivery/2017Dk4h325RE3',
  'https://drive.google.com.download-photo.sytez.net/AONh1e0hVP',
  'https://www.dropbox.com/buy',
  'westmountdayschool.org',
  'https://myaccount.google.com-securitysettingpage.ml-security.org/signonoptions/',
  'https://google.com/amp/tinyurl.com/y7u8ewlr',
  'www.tripit.com/uhp/userAgreement'
]

def do_request(urls):
    response_object = {'status': 'success'}
        if request.method == 'POST':
            post_data = request.get_json()
            response_object['message'] = post_data

  #    1. Make the request
  #    1. Check the request for errors; handle (print) errors if so
  #    1. Assuming no errors, print the predicted response
  pass


# 1. Then, loop over the urls and post one at a time.
for url in urls:
  do_request([url])


# 2. First, `post` all the urls at the same time
do_request(urls)

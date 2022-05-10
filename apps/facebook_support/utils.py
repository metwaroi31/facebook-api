from urllib.parse import urlparse, parse_qs
import requests
# from pyfacebook import GraphAPI

def get_facebook_id(fb_url):
    URL = "https://id.atpsoftware.vn/"
    headers ={
        'Content-Type': 'multipart/form-data;'
    }
    payload=dict(url_facebook=fb_url)
    r = requests.post(URL, data=payload)
    print (r.text)
    return 0

def get_facebook_post_id(url):
    parsed_url = urlparse(url)
    captured_post_id = parse_qs(parsed_url.query)
    # url format contains storyfb id
    if 'story_fbid' in captured_post_id:
        return captured_post_id['story_fbid'][0]
    try :
        post_url_parse = url.split('posts')
        print (post_url_parse)
        post_id = post_url_parse[1]
        print (post_id)
        return post_id
    except Exception:
        return 'this is not a valid url'

from urllib.parse import urlparse, parse_qs

def get_facebook_id(url):
    parsed_url = urlparse(url)
    captured_value = parse_qs(parsed_url.query)['id'][0]
    return captured_value


def get_facebook_post_id(url):
    parsed_url = urlparse(url)
    captured_value = parse_qs(parsed_url.query)['story_fbid'][0]
    return captured_value
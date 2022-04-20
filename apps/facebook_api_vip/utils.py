import requests
from apps.config import Config
import datetime
# api get vip like theo ctv_username
def getviplike(username):
    url = Config.FACEBOOK_API
    apikey = Config.FACEBOOK_API_KEY
    # data = {"eventType": "AAS_PORTAL_START", "data": {"uid": "hfe3hf45huf33545", "aid": "1", "vid": "1"}}
    data = {'key': apikey, 'useradd': username, 'act': 'get'}
    response = requests.post(url, data=data)
    return response.text

# api add vip like
def addlike(id_post, name, han, limit, ghichu, loailike, camxuc):
    url = Config.FACEBOOK_API
    apikey = Config.FACEBOOK_API_KEY
    data = {'key': apikey, 'act': 'add', 'name': name, 'time': han, \
                    'limit': limit, 'ghichu': ghichu, 'loailike': loailike, 'camxuc': camxuc, 'id': id_post }
    response = requests.post(url, data=data)
    return response.text
    
# api get cảm xúc theo id
def getcamxuc (id_post):
    url = Config.FACEBOOK_API
    apikey = Config.FACEBOOK_API_KEY
    data = {'key': apikey, 'act': 'getCx', 'id': id_post}
    response = requests.post(url, data=data)
    return response.text

# api cập nhật cảm xúc theo id
def updateLike(id_post, camxuc):
    url = Config.FACEBOOK_API
    apikey = Config.FACEBOOK_API_KEY
    data = {'key': apikey, 'act': 'update', 'id': id_post, 'cx': camxuc}
    response = requests.post(url, data=data)
    return response.text

# api xoa like (tru 7 ngay)
def dellike(id_post):
    url = Config.FACEBOOK_API
    apikey = Config.FACEBOOK_API_KEY
    data = {'key': apikey, 'act': 'del', 'id': id_post}
    response = requests.post(url, data=data)
    return response.text

# api add vip cmt
# $param = array(
#     'key' => $apikey,
#     'act'=> 'add',
#     'id' => $id,
#     'name' => $name,				
#     'time' => $han, 7-30 ngày
#     'limit' => $limit,
#     'noidung' => $noidung, // k chứa icon đặc biệt
#     'linkanh' => $linkanh, // định dạng link1|link2|link3(có thể bỏ trống)
#     'sticker' => $sticker, // định dạnh sticker1|sticker|sticker (có thể bỏ trống)
#     'lenhdung' => $lenhdung	
def addcmt(id_post, name, han, limit, ghichu, noidung, lenhdung):
    url = Config.FACEBOOK_API_CMT
    apikey = Config.FACEBOOK_API_KEY
    data = {'key': apikey, 'act': 'add', 'id': id_post, 'name': name, \
                    'time': han, 'limit': limit, 'noidung': noidung, 'lenhdung': lenhdung}
    response = requests.post(url, data=data)
    return response.text

# api get vip cmt
def getvipcmt(username):
    url = Config.FACEBOOK_API_CMT
    apikey = Config.FACEBOOK_API_KEY
    data = {'key': apikey, 'act': 'get', 'useradd': username}
    response = requests.post(url, data=data)
    return response.text

# api get noi dung theo id
def getnoidung(id_post):
    url = Config.FACEBOOK_API
    apikey = Config.FACEBOOK_API_KEY
    data = {'key': apikey, 'act': 'getCmt', 'id': id_post}
    response = requests.post(url, data=data)
    return response.text

# api get chi tiet mat live 
def getchitetmat(id_post):
    url = Config.FACEBOOK_API
    apikey = Config.FACEBOOK_API_KEY
    data = {'key': apikey, 'act': 'getLive', 'id': id_post}
    response = requests.post(url, data=data)
    return response.text

# api chinh sua cmt
def editcmt(id_post, noidung, linkanh, lenhdung):
    url = Config.FACEBOOK_API_CMT
    apikey = Config.FACEBOOK_API_KEY
    data = {'key': apikey, 'act': 'edit', 'id': id_post, \
                    'linkanh': linkanh, 'noidung': noidung, 'lenhdung': lenhdung}
    response = requests.post(url, data=data)
    return response.text


# api gia han like
def giahanlike(id_post, hanthue):
    url = Config.FACEBOOK_API
    apikey = Config.FACEBOOK_API_KEY
    data = {'key': apikey, 'act': 'giahan', 'id': id_post, 'hanthue': hanthue}
    response = requests.post(url, data=data)
    return response.text

# api gia han cmt
def giahancmt(id_post, hanthue):
    url = Config.FACEBOOK_API_CMT
    apikey = Config.FACEBOOK_API_KEY
    data = {'key': apikey, 'act': 'giahan', 'id': id_post, 'hanthue': hanthue}
    response = requests.post(url, data=data)
    return response.text

# api xoa cmt
def delcmt(id_post):
    url = Config.FACEBOOK_API
    apikey = Config.FACEBOOK_API_KEY
    data = {'key': apikey, 'act': 'del', 'id': id_post}
    response = requests.post(url, data=data)
    return response.text

# api addlive
def addlive(id_post, name, han, limit, ghichu):
    url = Config.FACEBOOK_API_MAT
    apikey = Config.FACEBOOK_API_KEY
    data = {'key': apikey, 'act': 'add', 'id': id_post, \
                    'name': name, 'time': han, 'limit': limit, 'ghichu': ghichu}
    response = requests.post(url, data=data)
    return response.text

# api get live theo ctv_username
def getvipmat(username):
    url = Config.FACEBOOK_API_MAT
    apikey = Config.FACEBOOK_API_KEY
    data = {'key': apikey, 'act': 'get', 'useradd': username}
    response = requests.post(url, data=data)
    return response.text

# api xoa live
def dellive(id_post):
    url = Config.FACEBOOK_API
    apikey = Config.FACEBOOK_API_KEY
    data = {'key': apikey, 'act': 'del', 'useradd': username}
    response = requests.post(url, data=data)
    return response.text

def parse_emotion(request_data):
    return_emotions = ''
    if 'like_emotion' in request_data:
        return_emotions = return_emotions + 'LIKE' + '|'
    if 'haha_emotion' in request_data:
        return_emotions = return_emotions + 'HAHA' + '|'
    if 'wow_emotion' in request_data:
        return_emotions = return_emotions + 'WOW' + '|'
    if 'cry_emotion' in request_data:
        return_emotions = return_emotions + 'Buồn' + '|'
    if 'angry_emotion' in request_data:
        return_emotions = return_emotions + 'Phẫn nộ' + '|'
    if 'love_emotion' in request_data:
        return_emotions = return_emotions + 'LOVE' + '|'
    return_emotions = return_emotions[0 : (len(return_emotions) - 1)]
    return return_emotions

def parse_date(date_int):
    # when passing from view date_int is string
    date_int = int(date_int)
    timestamp = datetime.datetime.fromtimestamp(date_int)
    return timestamp.strftime('%Y-%m-%d')

def parse_template(template_string):
    template_string = template_string.replace('\\', '')
    return template_string

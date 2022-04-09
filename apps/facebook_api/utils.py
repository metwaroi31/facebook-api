import requests
from apps.config import Config

# api get vip like theo ctv_username
def getviplike(username):
    url = Config.FACEBOOK_API
    apikey = Config.FACEBOOK_API_KEY
    print (url, apikey)
    # data = {"eventType": "AAS_PORTAL_START", "data": {"uid": "hfe3hf45huf33545", "aid": "1", "vid": "1"}}
    data = {'key': apikey, 'useradd': username, 'act': 'get'}

    response = requests.post(url, data=data)
    print (response.text)
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
    url = Config.FACEBOOK_API
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
def editcmt(id_post, noidung, sticker, linkanh, lenhdung):
    url = Config.FACEBOOK_API
    apikey = Config.FACEBOOK_API_KEY
    data = {'key': apikey, 'act': 'edit', 'id': id_post, \
                    'sticker': sticker, 'linkanh': linkanh, 'noidung': noidung, 'lenhdung': lenhdung}
    response = requests.post(url, data=data)
    return response.text

# api gia han cmt
def giahan(id_post, hanthue):
    url = Config.FACEBOOK_API
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
    url = Config.FACEBOOK_API
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
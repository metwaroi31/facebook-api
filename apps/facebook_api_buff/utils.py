import requests
from apps.config import Config
import datetime

# api add bufflike 
def addbufflike(id_post, buff_type, limit, ghichu):
    url = Config.FACEBOOK_API_BUFF
    apikey = Config.FACEBOOK_API_KEY
    # 'key' => $apikey,
    # 'act'=> 'buffLike',
    # 'id' => $id,
    # 'limit' => $limit, // giới hạn like
    # 'ghichu' => $ghichu,
    # 'type' => $type // loại like (like_v2, like_v6) tương ứng (20đ,40đ)
    data = {'key': apikey, 'id': id_post, 'act': 'buffLike', 'limit': limit, 'ghichu': ghichu, 'type': buff_type}
    response = requests.post(url, data=data)
    print (response)
    return response.text
# // api buff sub người dùng thật 50đ bảo hành 3 tháng
# function addbuffsub($id,$limit,$ghichu,$apikey){
#   $param = array(
#     'key' => $apikey,
#     'act'=> 'buffSub',
#     'id' => $id,
#     'limit' => $limit, // giới hạn like
#     'ghichu' => $ghichu
# 		);
# 	$url = 'http://api.viplike.me/buff.php';
# 	$ch = curl_init($url);
# 	curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
# 	curl_setopt($ch, CURLOPT_POSTFIELDS, $param); 
# 	$result = curl_exec($ch); 
# 	curl_close($ch);   
# 	return $result; 

def addbuffsub(id_post, limit, ghichu):
    url = Config.FACEBOOK_API_BUFF
    apikey = Config.FACEBOOK_API_KEY
    # 'key' => $apikey,
    # 'act'=> 'buffLike',
    # 'id' => $id,
    # 'limit' => $limit, // giới hạn like
    # 'ghichu' => $ghichu,
    # 'type' => $type // loại like (like_v2, like_v6) tương ứng (20đ,40đ)
    data = {'key': apikey, 'id': id_post, 'act': 'buffSub', 'limit': limit, 'ghichu': ghichu}
    response = requests.post(url, data=data)
    return response.text 

def getbufflike():
    url = Config.FACEBOOK_API_BUFF
    apikey = Config.FACEBOOK_API_KEY
    # data = {"eventType": "AAS_PORTAL_START", "data": {"uid": "hfe3hf45huf33545", "aid": "1", "vid": "1"}}
    data = {'key': apikey, 'act': 'getbufflike'}
    response = requests.post(url, data=data)
    print (response)
    return response.text

# api add vip like
def addlike(id_post, name, han, limit, ghichu, loailike, camxuc):
    url = Config.FACEBOOK_API
    apikey = Config.FACEBOOK_API_KEY
    data = {'key': apikey, 'act': 'add', 'name': name, 'time': han, \
                    'limit': limit, 'ghichu': ghichu, 'loailike': loailike, 'camxuc': camxuc, 'id': id_post }
    response = requests.post(url, data=data)
    return response.text

def parse_date(date_int):
    # when passing from view date_int is string
    date_int = int(date_int)
    timestamp = datetime.datetime.fromtimestamp(date_int)
    return timestamp.strftime('%Y-%m-%d')

def parse_template(template_string):
    template_string = template_string.replace('\\', '')
    return template_string

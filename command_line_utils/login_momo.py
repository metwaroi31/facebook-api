import requests

def login_momo():
    username = '0394803011'
    password = '09112035+-*/Bb'

    data = {'taikhoan' : username, 'matkhau': password}
    r = requests.post('https://api.web2m.com/checklogin.php?login', data=data)
    # values={'upload_file' : 'file.txt' , 'DB':'photcat' , 'OUT':'csv' , 'SHORT':'short'}
    
    # r.headers['set-cookie'] has format PHPSESSID=xxxx; path=/
    session = r.headers['set-cookie']
    session = session.split(';')[0]
    session = session.split('=')[1]
    return session

print (login_momo())
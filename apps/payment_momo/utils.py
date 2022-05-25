import requests
from apps.config import Config
from apps.authentication.models import Users
from apps.payment_momo.models import transactions
import json

def pay_momo():
    momo_host = Config.MOMO_API 
    momo_token = Config.MOMO_TOKEN
    r = requests.post(momo_host + 'historyapimomo/' + momo_token)
    transaction_list = json.loads(r.text)['momoMsg']['tranList']
    print (transaction_list)
    add_coin_user(transaction_list)
    return True

def add_coin_user(transaction_list):
    # print (transaction_list)
    for trans in transaction_list:
        print (type(trans))
        transaction_processable = False
        user_processable = False

        # check if user has made transaction
        user = Users.query.filter_by(phone_number=trans['partnerId']).first()
        # check if this has made
        transaction = transactions.query.filter_by(transaction_id=trans['tranId']).first()
        transfer_amount = trans['amount'] 
        print (type(user))
        print (type(transaction))
        if type(transaction) == 'NoneType':
            print ("run")
            transaction_processable = True
        if type(user) == 'NoneType':
            print ("run")
            user_processable = True
        # processing transactions
        if transaction_processable and user_processable:
            transaction_to_add = {}
            transaction_to_add['transaction_id'] = trans['tranId']
            transaction_to_add['money'] = trans['amount']
            transaction_to_add['phone_number'] = user.phone_number
            transaction_to_add['username'] = user.username

            transaction_instance = transactions(**transaction_to_add)
            db.session.add(transaction_instance)
            db.session.commit()

    return True

def get_otp_momo(phone_number, momo_password):
    # send request
    # get status code
    # send email to user
    return

def add_phone_momo(phone_number, momo_password, otp):
    
    data = { 'phone': momo_account, 'sotien': money, 'nguoinhan': receiver, 'matkhaumomo': momo_account_password, \
                'tokenmomo': momo_token}
    r = requests.post(host + 'momo.function.php?transfer', data=data)
    
    return r.status_code
    
# curl --location --request POST 'https://api.web2m.com/include/momo/momo.function.php?transfer' --header 'Cookie: PHPSESSID=ilibvc5kqth46c9s5ld3lpkr53' --form 'phone="0394803011"' --form 'sotien="10000"' --form 'noidung="anh dang test tool"' --form 'nguoinhan="0986117185"' --form 'matkhaumomo="090909"' --form 'tokenmomo="38ADD6A2-CE7F-7244-8F03-F03C2ACBD1A7"'

# curl --location --request POST 'https://api.web2m.com/checklogin.php?login' --form 'taikhoan="0394803011"' --form 'matkhau="09112035+-*/Bb"' -A "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/81.0" --dump ./test

# curl --location --request POST 'https://api.web2m.com/include/momo/momo.function.php?getotpmomo' --form 'phone="0394803011"' --form 'matkhau="091120"' -A "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/81.0" --dump ./test

# curl --location --request POST 'https://api.web2m.com/include/momo/momo.function.php?CFotpmomo' --form 'phone="0394803011"' --form 'otp="1234"  --form 'phone="091120"' -A "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/81.0" --dump ./test
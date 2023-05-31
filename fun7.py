# argumenty słownikowe

def connect(**opcje):
    print(opcje)
    print(type(opcje))
    conect_param = {
        'host': '127.0.0.7',
        'port': '8080'
    }
    print(conect_param)
    conect_param['pwd'] = opcje
    print(conect_param)  # {'host': '127.0.0.7', 'port': '8080', 'pwd': {'a': 7}}

    conect_param.update({'pwd2': opcje})
    print(conect_param)  # {'host': '127.0.0.7', 'port': '8080', 'pwd': {'a': 7}, 'pwd2': {'a': 7}}


connect()  # {}  <class 'dict'>
connect(a=7)  # {'a': 7}
connect(a=7, b=9)  # {'a': 7, 'b': 9}
connect(user="/home", root='/')  # {'user': '/home', 'root': '/'}
# 13:25
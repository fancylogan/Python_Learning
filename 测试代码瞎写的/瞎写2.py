import base64


def encode():
    upwd = input("Input your password: ")
    return (base64.b64encode(upwd.encode("utf-8"))).decode("utf-8")



def decode():
    cpwd = input("Input your password: ")


print(encode())
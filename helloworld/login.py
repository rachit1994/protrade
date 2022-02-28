from kiteconnect import KiteConnect

'''
use this function if accesstoken expires.
1. go to https://kite.zerodha.com/connect/login?api_key=x8qw1x9c0wrweuz6
2. userid - JX7559 , pswd - Rachit!@#456 , pin - 090119
3. copy request token from url and update below in request_token
4. run this file
new access token will be written in accesstokenfile.
'''
kite = KiteConnect(api_key="x8qw1x9c0wrweuz6")
request_token = "KO4he1bvC9GU7KBYYDE90lx5Tshg3oLg"
def login():
    data = kite.generate_session(request_token=request_token, api_secret="ioyxelwyhxbfroyup8yggfqsckazyiil")
    print(data["access_token"])
    open("accesstokenfile","w").write(data["access_token"])
login()
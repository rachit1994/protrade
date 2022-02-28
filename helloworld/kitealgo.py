from kiteconnect import KiteConnect
# if you are getting invalid token issue, run login.py file
def getkite():
    kite = KiteConnect(api_key="x8qw1x9c0wrweuz6")
    kite.set_access_token(open("accesstokenfile").readlines()[0])
    return kite
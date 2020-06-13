import requests
def demo(method, url, params):
    print("method is",method)
    print("url is",url)
    print("params is",params)

corpid = "ww93348658d7c66ef4"
corpsecret =  "T0TFrXmGYel167lnkzEydsjl6bcDDeXVmkUnEYugKIw"
req = {
    "method": "get",
    "url": "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
    "params": {"corpid": corpid, "corpsecret": corpsecret}
}
# demo(method="get", url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
#      params= {"corpid": corpid, "corpsecret": corpsecret})
# demo(**req)

# 两个** 代表对字典进行解包， 使用 k=v 的形式进行传参

r= requests.request(**req)
print(r.json())
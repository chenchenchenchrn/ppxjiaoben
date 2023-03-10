import json
import os

import requests


# 这里是各自的推送数据
PUSH_PLUS_TOKEN = '201976fb0a1a4256819ebbf1cdb53e59'
title = '皮皮虾-往昔3'

# 这里是各自的CK数据
XSSCookie = "store-region=cn-sx; store-region-src=did; ttreq_tob=1$6459f04153e8aed526f373bbae688c3fe1cf4c7b; install_id=4077467183364173; ttreq=1$d27dd4479939e857c83d4dd36dab2a8e0b2748f4; ttreq_tob=1$6459f04153e8aed526f373bbae688c3fe1cf4c7b; BAIDUID=9AB78EC41328278D0F67B997C0328CD7:FG=1; passport_csrf_token_default=884a556809a3b5360431ccabb56c45b0; d_ticket=caa180fa9324d343520b47d3dd82a1ad045a0; odin_tt=4067aca64300e997fe0501f0df3c684804ebd7431c76682d8207a83502596a4d39a39e79f46db641b115b35868a5c35ea6769c2b54d5ed9019de4383ab02487165e42c69180027e24bd1e147c5f07b99; n_mh=QL3qblGqRUuAAw850m4bVI_KibgB6ADlcG9zZUqjA7o; sid_guard=92773ef7246c38f72a2b7965f4af1214%7C1678372684%7C5183999%7CMon%2C+08-May-2023+14%3A38%3A03+GMT; uid_tt=c0b7cbcff2bf1ea0f586973441fa3f4c; sid_tt=92773ef7246c38f72a2b7965f4af1214; sessionid=92773ef7246c38f72a2b7965f4af1214; store-region=cn-hb; store-region-src=uid"
xTtToken ="0092773ef7246c38f72a2b7965f4af1214022c3b5f3e26c91b1d2de7e51de340ad3bbc4e5379c07a436733c341cf65bb05697799e2cb46f0e3813d61432754415af6d9ba42353c74465f5c45cf8f64a59aadeca32de4c72ef4a7d8a2a803094f9bb55-1.0.1"

# 全局推送内容
content = []
if "PUSH_PLUS_TOKEN" in os.environ and len(os.environ["PUSH_PLUS_TOKEN"]) > 1:
    PUSH_PLUS_TOKEN = os.environ["PUSH_PLUS_TOKEN"]

def sign(number):
    url = "https://api5-lf.pipix.com/luckycat/bds/v1/task/done/excitation_ad?nowebp=1&version_code=4.4.0&app_name=super&device_id=70752968174&channel=App%20Store&resolution=1242*2688&aid=1319&last_channel=App%20Store&last_update_version_code=42480&recommend_disable=0&update_version_code=44080&ac=WIFI&os_version=15.6.1&device_platform=iphone&iid=2617299670153624&device_type=iPhone%20XS%20Max"
    headers = {
        "User-Agent": "Super 4.4.0 rv:4.4.0.80 (iPhone; iOS 15.6.1; zh_CN) Cronet",
        "Connection": "keep-alive",
        "Host": "api5-lf.pipix.com",
        "x-Tt-Token": xTtToken,
        "Accept": "application/json, text/plain, */*",
        "Cookie": "www.kejiwanjia.com",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded",
        "X-SS-Cookie":XSSCookie,

    }
    r = requests.post(url, headers=headers, timeout=5)
    print("第" + number + "次--皮皮虾广告任务结果>>>" + str(r.json()))
    content.append("第" + number + "次--皮皮虾广告任务结果>>>" + str(r.json()["message"]) +"<br>")
    if r.json()["status_code"]==0:
        print("观看成功，获得100金币")
        content.append("观看成功，获得100金币<br>")
    else:
        print("观看失败：" + str(r.json()["message"]))
        content.append("观看失败：" + str(r.json()["message"]) + "<br>")


# 查询金币余额
def checkInfo():
    url = "https://api5-lf.pipix.com/luckycat/bds/v1/wallet/info?nowebp=1&version_code=4.4.0&app_name=super&device_id=70752945269&channel=App%20Store&resolution=1242*2688&aid=1319&last_channel=App%20Store&last_update_version_code=42480&recommend_disable=0&update_version_code=44080&ac=WIFI&os_version=16.3&device_platform=iphone&iid=2617299670115296&device_type=iPhone%20XS%20Max"
    headers = {
        "User-Agent": "Super 4.4.0 rv:4.4.0.80 (iPhone; iOS 15.6.1; zh_CN) Cronet",
        "Connection": "keep-alive",
        "Host": "api5-lf.pipix.com",
        "x-Tt-Token": xTtToken,
        "Accept": "application/json, text/plain, */*",
        "Cookie": "www.kejiwanjia.com",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded",
        "X-SS-Cookie":XSSCookie,

    }
    r = requests.get(url, headers=headers, timeout=5)
    print("查询金币余额结果 >>> " + str(r.json()))

    # 余额
    account = str(r.json()["data"]["balance"])

    content.append("<br>")
    content.append("【开始查询金币数量】>>> " + account +"<br>")

    if r.json()["status_code"]==0:
        print("查询成功，剩余" + account + "金币")
        content.append("查询成功，剩余" + account + "金币<br>")
        return account
    else:
        print("查询失败：" + str(r.json()["message"]))
        content.append("查询失败：" + str(r.json()["message"]) + "<br>")

# push推送
def push_plus_bot(title, PushContent):
    try:
        print("\n")
        if not PUSH_PLUS_TOKEN:
            print("PUSHPLUS服务的token未设置!!\n取消推送")
            return
        print("PUSHPLUS服务启动")
        url = 'http://pushplus.plus/send'
        data = {
            "token": PUSH_PLUS_TOKEN,
            "title": title,
            "content": PushContent,
            "template": "html"
        }
        body = json.dumps(data).encode(encoding='utf-8')
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url=url, data=body, headers=headers).json()
        if response['code'] == 200:
            print('推送成功！')
        else:
            print('推送失败！')
            print(response)

    except Exception as e:
        print(e)

# 入口主函数
def main():

    # 完成广告任务
    print("皮皮虾广告任务开始执行")
    print("")
    for i in range(10):
        sign(str(i+1))

    # 开始查询金币数量
    account = checkInfo()

    # 发送通知 # 直接在提送标题显示金币数量
    push_plus_bot(title + "|金币:" + account, content)

if __name__ == '__main__':
    main()
# -------  腾讯云函数启动模块  --------#
def main_handler(event, context):
    main()

# -------  阿里云函数启动模块  -------- #
def handler(event, context):
    main()

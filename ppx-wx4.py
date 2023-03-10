import json
import os

import requests


# 这里是各自的推送数据
PUSH_PLUS_TOKEN = '201976fb0a1a4256819ebbf1cdb53e59'
title = '皮皮虾-往昔3'

# 这里是各自的CK数据
xTtToken = "00d2fc64c1b2ae07b24d6669ecaed04e9e001598f1b4b61b9a30ffff7291dbceefb65bf9a60d1f2cb012a6becf86539bd25895da0a91813c1775f5316da6df65e8e1ee7dbb9ea9231c1a6e27eda8549302bcada27771fae4b33d63cc726403cf7125c-1.0.1"
XSSCookie = "store-region=cn-sx; store-region-src=did; ttreq_tob=1$6459f04153e8aed526f373bbae688c3fe1cf4c7b; store-region=cn-sx; install_id=4077467183364173; ttreq=1$d27dd4479939e857c83d4dd36dab2a8e0b2748f4; ttreq_tob=1$6459f04153e8aed526f373bbae688c3fe1cf4c7b; BAIDUID=2D708EDD281CD592CFF2D04559AB95B1:FG=1; passport_csrf_token_default=2ad027d7fb3e90095aaeed06e54b6442; d_ticket=0109d201625784baf7056f15ae9071d0045a0; n_mh=Hf0tPyLZmRdgqrBynnees2Sf21bc60BodyAtd9Lc948; sid_guard=d2fc64c1b2ae07b24d6669ecaed04e9e%7C1678349300%7C5184000%7CMon%2C+08-May-2023+08%3A08%3A20+GMT; uid_tt=49cbc4ed234f5bda33b65ae993ee6e61; sid_tt=d2fc64c1b2ae07b24d6669ecaed04e9e; sessionid=d2fc64c1b2ae07b24d6669ecaed04e9e; store-region-src=uid; odin_tt=f4096698a264e86d4492c883a4a72295dca0be8d1ae535d22441d7c96b8f29101a18330e36658f932baef8558b1fd6059fa669c7d26ea6727ee6bc4b2c177994"

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

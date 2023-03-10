import json
import os

import requests


# 这里是各自的推送数据
PUSH_PLUS_TOKEN = '201976fb0a1a4256819ebbf1cdb53e59'
title = '皮皮虾-往昔3'

# 这里是各自的CK数据
XSSCookie =  "store-region=cn-sx; ttreq_tob=1$6459f04153e8aed526f373bbae688c3fe1cf4c7b; install_id=4077467183364173; ttreq=1$d27dd4479939e857c83d4dd36dab2a8e0b2748f4; BAIDUID=D34540B128F3F358E67C799A38D29157:FG=1; passport_csrf_token_default=8539735fc8769326d361be9fb7f8e314; d_ticket=acae4bf83f170087228512b83b3845c1045a0; odin_tt=c2e270ac4bd6d2c3202b09da3bc7d019248a3489222bce96c8c70d19249e01733ec303b0924dd669fb8d547f74982306684a3cec541dd1e39ee8d2c0090a20e243b69950a685bf4ac10b50ff9244fc09; n_mh=OrRb6ej9h5b_07iu00s8WTE8mY8c_bHBUA-QwC5m3CE; sid_guard=0c9e0c8fd63a8293e178b78d0fc9a6cf%7C1678351665%7C5184000%7CMon%2C+08-May-2023+08%3A47%3A45+GMT; uid_tt=64b6bb89c3883434648a32d50df043ce; sid_tt=0c9e0c8fd63a8293e178b78d0fc9a6cf; sessionid=0c9e0c8fd63a8293e178b78d0fc9a6cf; store-region-src=uid"
xTtToken ="000c9e0c8fd63a8293e178b78d0fc9a6cf05f465a19dee2558088ff8d45a8c087f7f7651cb52e6d1892db69973fbfc478b99c47bd8cc533270bd81f26644f29b3e2c453c78e1756b0d21f90d3ce3e859261289c8e8fe30a59864b0d2d3a3aff0dd3e6-1.0.1"

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

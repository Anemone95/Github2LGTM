#!/usr/bin/env python
# coding=utf-8

# @file addintolgtm.py
# @brief addintolgtm
# @author Anemone95,x565178035@126.com
# @version 1.0
# @date 2019-07-08 09:58

import requests
import json

def add_all():
    with open('./repos.json', 'r') as f:
        repos=json.load(f)
    for i in repos:
        endi=i[1].find('archive')
        url=i[1][0:endi]
        addintolgtm(url)
        print(i, url)

def addintolgtm(url):
    burp0_url = "https://lgtm.com:443/internal_api/v0.2/followProject"
    burp0_cookies = {
        "lgtm_long_session": "64352dddb46393755512670e311ebe36c4521d542b271d658097f7c65b01a584f9530d20bbc78e8bd5dab02c938f0028a4be548805365e6b3861bc207ead1cef",
        "lgtm_short_session": "a75c128613ac2fef647404e0bc584bf11a5cd018a65d742428beb41cbf03422df2ef92599070db9cb68bdb8d3f989f599675979072bf918b0b120f31fa510140"}
    burp0_headers = {
        "Connection": "close",
        "Accept": "*/*",
        "LGTM-Nonce": "b537019425877b939c6aab74b570b91f37c3f8f8d8ec08737bb916342572b836d161799819a2f5f0d8c144d68cb8147fef666a30a1a7a34063319f9c29ff2927",
        "Origin": "https://lgtm.com",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded",
        "Referer": "https://lgtm.com/dashboard",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,ja;q=0.6"}
    burp0_data = {"url": url,
                  "apiVersion": "23ca9896a4ffafe343fc941ca84d3e3603db12fd"}
    res=requests.post(
        burp0_url,
        headers=burp0_headers,
        cookies=burp0_cookies,
        data=burp0_data)
    print(res.json())


if __name__ == '__main__':
    add_all()

import logging

import requests
import base64
import json

BASEURL = 'https://api.github.com'

with open('./account.txt', 'r') as f:
    line = f.readlines()[0]
    USER, PASS = line.replace('\r', '').replace('\n', '').split(":")


def get_repo_list(org=None, username=None):
    repos = []
    if org:
        res = requests.get("{0}/orgs/{1}/repos".format(BASEURL, org), auth=(USER, PASS))
    else:
        res = requests.get("{0}/users/{1}/repos".format(BASEURL, username), auth=(USER, PASS))
    logging.info(res.headers)
    repos += res.json()

    while True:
        link_header = res.headers.get("Link", None)
        if not link_header:
            break
        links = link_header.split(", ")
        if "next" not in link_header:
            break
        if 'prev' in links[0]:
            link = links[1].split('; ')[0][1:-1]
        else:
            link = links[0].split('; ')[0][1:-1]
        logging.info(link)
        res = requests.get(link)
        repos += res.json()
        logging.info("RepoNum: {}".format(len(repos)))
    # https://github.com/alibaba/asyncload/archive/master.zip
    repos = list(map(lambda e: (e["name"], e["html_url"] + "/archive/master.zip"), repos))
    return repos

if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(filename)s : %(funcName)s : %(message)s',
                        level=logging.INFO)
    print(get_repo_list(username="anemone95"))

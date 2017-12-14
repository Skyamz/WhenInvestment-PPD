# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 23:43:46 2017

@author: skyamz
"""

import requests
import json
import io


class AppSpider:
    def __init__(self):
        self.siteURL = 'https://itunes.apple.com/WebObjects/MZStore.woa/wa/userReviewsRow?cc=cn&displayable-kind=11&sort=0&appVersion=all&id='

    def getComments(self, appId, startIndex, endIndex):
        url = self.siteURL + str(appId) + '&startIndex=' + str(startIndex) + '&endIndex=' + str(endIndex)
        comments = requests.get(url, headers={"User-Agent": "iTunes/11.0 (Windows; Microsoft Windows 7 Business Edition Service Pack 1 (Build 7601)) AppleWebKit/536.27.1"})
        c = json.loads(comments.text)
        return json.dumps(c["userReviewList"])[1:-1]


spider = AppSpider()
with io.open('app.json', 'w+', encoding='utf8') as file:
    for i in range(0, 255):
        c = spider.getComments(983488107, i * 100, i * 100 + 99)
        file.write(c)

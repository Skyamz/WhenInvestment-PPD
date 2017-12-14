import requests
import re


class Spider:
    def __init__(self):
        self.siteURL = 'http://group.ppdai.com/forum.php'

    def getThread(self, threadId):
        url = self.siteURL + "?mod=viewthread&tid=" + str(threadId)
        print
        url
        content = requests.get(url)
        if "抱歉，指定的主题不存在或已被删除或正在被审核" in content:
            return ""
        return content.text

    def getPosts(self, threadId):
        thread = self.getThread(threadId)
        if thread == "":
            return
        pattern = re.compile(
            '<table id="pid[0-9]*?".*?class="xi2">(.*?)</a>.*?发表于 <span title="(.*?)">.*?<td class="t_f".*?>\r\n(.*?)</td>.*?' ,
            re.S)
        items = re.findall(pattern, thread)
        for item in items:
            print(item)


spider = Spider()
for i in range(846227, 900000):
    print(i)
    spider.getPosts(i)

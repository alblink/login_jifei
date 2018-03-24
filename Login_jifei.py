# -*- coding:utf-8 -*-
"""

@Time    : 2018/3/24 11:05
@Author  : YeJian
@File    : Login_jifei.py

"""

import urllib.request
import urllib.parse
import wx
from bs4 import BeautifulSoup


class MyFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, '登录计费系统', pos=(600, 200), size=(300, 200))
        self.panel = wx.Panel(self)
        self.button_in = wx.Button(self.panel, label='登录', pos=(50, 15))
        self.button_out = wx.Button(self.panel, label='注销', pos=(150, 15))
        self.Bind(wx.EVT_BUTTON, self.login, self.button_in)
        self.Bind(wx.EVT_BUTTON, self.logout, self.button_out)

        wx.StaticText(self.panel, -1, "登录状态: ", (50, 100))
        self.rev = wx.StaticText(self.panel, -1, '', (105, 100))
        self.show_status()

    def login(self, event):
        url = 'http://172.16.6.3:80'
        head = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Host': '172.16.6.3',
            'Origin': 'http://172.16.6.3',
            'Referer': 'http://172.16.6.3/',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'
        }
        data = {
            'DDDDD': '2154021870',
            'upass': '572894',
            '0MKKey': ''
        }
        data = urllib.parse.urlencode(data).encode('gbk')
        req = urllib.request.Request(url, data, head)
        res = urllib.request.urlopen(req)


        self.show_status()

    def logout(self, event):
        url = 'http://172.16.6.3/F.htm'
        dlg = wx.MessageDialog(None, "你确定要注销吗？", "注销", wx.YES_NO | wx.ICON_QUESTION)
        if dlg.ShowModal() == wx.ID_YES:
            urllib.request.urlopen(url)
            self.show_status()
        dlg.Destroy()

    def get_status(self):
        url = 'http://172.16.6.3'
        res = urllib.request.urlopen(url)
        html = res.read().decode('gbk')
        soup = BeautifulSoup(html, 'html.parser')
        if soup.title.string == '上网注销窗':
            return 1
        else:
            return 0

    def show_status(self):
        status = self.get_status()
        if status:
            self.rev.SetLabel('已登录')
            self.rev.SetForegroundColour('green')
        else:
            self.rev.SetLabel('未登录')
            self.rev.SetForegroundColour('red')


if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame(parent=None, id=-1)
    frame.Show()
    app.MainLoop()





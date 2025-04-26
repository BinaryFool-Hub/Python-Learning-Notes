"""
官网：https://github.com/cluic/wxauto
使用文档：https://wxauto.loux.cc/docs/intro

功能：
    接收最新信息
    发送信息
    获取聊天记录
……
"""

from wxauto import WeChat  # pip install wxauto

# 实例化微信对象
wx = WeChat()

# 获取所有新消息
msgs = wx.GetAllNewMessage()
print(msgs)

# 发送消息给文件传输助手
msg = 'hello, wxauto!'
who = '文件传输助手'
wx.SendMsg(msg=msg, who=who)

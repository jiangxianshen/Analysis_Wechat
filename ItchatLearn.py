# 简单入门实例
import itchat
# 登陆
itchat.auto_login()
# 给文件助手发消息
itchat.send('hello',toUserName='filehelper')

# 自动回复
@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    return  '机器自动回复'
itchat.auto_login()
itchat.run()
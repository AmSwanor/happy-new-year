import itchat,time,re
from itchat.content import *

@itchat.msg_register([TEXT])
def text_reply(msg):
    match = re.search("年",msg['Text']).span()
    if match:
        itchat.send(('鸡年大吉'),msg['FromUserName'])

@itchat.msg_register([PICTURE, RECORDING,VIDEO,SHARING])
def other_reply(msg):
    itchat.send(('鸡年大吉'),msg['FromUserName'])

itchat.auto_login(enableCmdQR=True,hotReload=True)
itchat.run()

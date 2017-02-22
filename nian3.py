

import random
import time
import sys
import itchat#需要安装itchat包，可直接 pip install itchat

from itchat.content import *
def main(): 
    itchat.auto_login(True)
    friendList = itchat.get_friends(update=True)[1:]
    terms=[0]*len(friendList)
    uns=[]
    for f in friendList:
        uns.append(f['UserName'])
    def autoreply():
        wishlist=[u'鸡年大吉!',u'[鸡]',u'财源滚滚!',u'[微笑]',u'[红包]',u'谢谢,',u'[强]',u'[呲牙]']
        @itchat.msg_register(TEXT)
        def text_reply(msg):
            if terms[uns.index(msg['FromUserName'])]==0:#第一轮对话
                terms[uns.index(msg['FromUserName'])]=terms[uns.index(msg['FromUserName'])]+1
                print (friendList[uns.index(msg['FromUserName'])]['DisplayName'] or friendList[uns.index(msg['FromUserName'])]['NickName']),'term',terms[uns.index(msg['FromUserName'])],':',msg['Text']
                ts=random.randint(5,30)
                text=u'谢谢![呲牙][强]'#第一轮对话回复文本
                while ts:
                    time.sleep(1.)
                    ts=ts-1
                    print (u'将在%s秒后自动回复内容:%s \r'%(str(ts),text),
                    sys.stdout.flush())
                return text
            elif  terms[uns.index(msg['FromUserName'])]==1:#第二轮对话
                terms[uns.index(msg['FromUserName'])]=terms[uns.index(msg['FromUserName'])]+1
                print (friendList[uns.index(msg['FromUserName'])]['DisplayName'] or friendList[uns.index(msg['FromUserName'])]['NickName']),'term',terms[uns.index(msg['FromUserName'])],':',msg['Text']
                ts=random.randint(5,30)
                text=u'[福][红包][鸡]'
                while ts:
                    time.sleep(1.)
                    ts=ts-1
                    print (u'将在%s秒后自动回复内容:%s \r'%(str(ts),text),
                    sys.stdout.flush())
                return text
            elif terms[uns.index(msg['FromUserName'])]>=2 and terms[uns.index(msg['FromUserName'])]<=4:#第n轮对话，根据wishlist随机组合回复内容,大于5轮就闭嘴
                terms[uns.index(msg['FromUserName'])]=terms[uns.index(msg['FromUserName'])]+1
                print (friendList[uns.index(msg['FromUserName'])]['DisplayName'] or friendList[uns.index(msg['FromUserName'])]['NickName']),'term',terms[uns.index(msg['FromUserName'])],':',msg['Text']
                wish=u''
                for i in range(random.randint(1,5)):#长度随机
                    wish=wish+wishlist[random.randint(0,7)]
                print  (wish)
                ts=random.randint(5,30)
                while ts:
                    time.sleep(1.)
                    ts=ts-1
                    print (u'将在%s秒后自动回复内容:%s \r'%(str(ts),wish),
                    sys.stdout.flush())
                    
                return wish
        @itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
        def el_reply(msg):
            if terms[uns.index(msg['FromUserName'])]<=4:
                terms[uns.index(msg['FromUserName'])]=terms[uns.index(msg['FromUserName'])]+1
                print (friendList[uns.index(msg['FromUserName'])]['DisplayName'] or friendList[uns.index(msg['FromUserName'])]['NickName']),'term',terms[uns.index(msg['FromUserName'])],u':其他类型消息'
                ts=random.randint(5,30)
                wish=u''
                for i in range(random.randint(1,5)):#长度随机
                    wish=wish+wishlist[random.randint(0,7)]
                print  (wish)    
                ts=random.randint(5,30)
                while ts:
                    time.sleep(1.)
                    ts=ts-1
                    print (u'将在%s秒后自动回复内容:%s \r'%(str(ts),wish),
                    sys.stdout.flush())
                pic_list=['jndj.jpg','gxfc.jpg','wsry.jpg']
                itchat.send('@img@%s' % pic_list[random.randint(0,2)],msg['FromUserName'])
                time.sleep(2.)
                return wish
    autoreply()
    itchat.run()                
            
if __name__=='__main__':
    main()     

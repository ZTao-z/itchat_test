# -* coding : utf-8 *-

import itchat, time
import requests
from itchat.content import *
import gl

KEY = '8edce3ce905a4c1dbb965e6b35c3834d'

#8edce3ce905a4c1dbb965e6b35c3834d
#eb720a8970964f3f855d863d24406576
#1107d5601866433dba9599fac1bc0083
#71f28bf79c820df10d39b4074345ef8c
#fa3f299487c447bfb6d385986a719e24
#6bc41f023fc4464e94cbe609c1b6f25c

def get_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key'     : KEY,
        'info'    : msg,
        'userid'  : 'wechat_robot',
    }
    try:
        r = requests.post(apiUrl, data=data).json()
        return r.get('text')
    except:
        return

def check(msg):
    if msg["FromUserName"] == myUserName and msg["ToUserName"] == 'filehelper':
        if msg['Text'] == u"clar":
            itchat.send('auto reply close',toUserName='filehelper')
            gl.is_auto_reply_open = False
        elif msg['Text'] == u"opar":
            itchat.send('auto reply open', toUserName='filehelper')
            gl.is_auto_reply_open = True
        elif msg['Text'] == u'logout':
            itchat.send('Log out', toUserName='filehelper')
            itchat.logout()
    else:
        return

@itchat.msg_register(TEXT,isFriendChat=True,isGroupChat=False,isMpChat=False)
def tuling_reply(msg):
    check(msg)
    if gl.is_auto_reply_open == True:
        #print('reply open')
        if not msg["FromUserName"] == myUserName:
            #time.sleep(1)
            defaultReply = u'自动回复：挂机中，有事请留言，稍后回复..'
            reply = get_response(msg['Text'])
            return defaultReply or reply
        return
    return


#itchat.auto_login()
#itchat.auto_login(enableCmdQR=True)

itchat.auto_login(hotReload=True)

if __name__ == '__main__':
    itchat.auto_login()
    itchat.send(u'web wechat log in',toUserName='filehelper')
    myUserName = itchat.get_friends()[0]['UserName']
    itchat.run()
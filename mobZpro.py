'''
┏━━━━━━━━━━━━━━━━━
┣ 𐀀 HΞLLTΞRHΞΛD ᴄᴏʀᴘ.
┣ ©2020 ᴍᴏ-ʙᴀɴᴢᴜ
┗━━━━━━━━━━━━━━━━━
'''

from linepy import *
from liff.ttypes import LiffChatContext, LiffContext, LiffSquareChatContext, LiffNoneContext, LiffViewRequest
from thrift import transport, protocol, server
from akad.ttypes import *
from akad.ttypes import Message
from akad.ttypes import ContentType as Type
from akad.ttypes import TalkException
from akad.ttypes import IdentityProvider, LoginResultType, LoginRequest, LoginType
from akad.ttypes import ChatRoomAnnouncementContents
from akad.ttypes import Location
from akad.ttypes import ChatRoomAnnouncement
from multiprocessing import Pool, Process
from thrift.Thrift import *
from thrift.unverting import *
from thrift.TMultiplexedProcessor import *
from thrift.TSerialization import *
from thrift.TRecursive import *
from thrift import transport, protocol, server
from thrift.protocol import TCompactProtocol, TMultiplexedProtocol, TProtocol
from thrift.transport import TTransport, TSocket, THttpClient, TZlibTransport
from time import sleep
import pytz, datetime, time, timeit, livejson,asyncio, random, sys, ast, re, os, json, subprocess, threading, string, codecs, requests, ctypes, urllib, traceback, tempfile, platform
from humanfriendly import format_timespan, format_size, format_number, format_length
from datetime import timedelta, date
from datetime import datetime
from threading import Thread, activeCount

# 𐀀 HΞLLTΞRHΞΛD ᴄᴏʀᴘ. _______________________________________________________

_session = requests.session()
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2

programStart = time.time()

a001 = LINE('EMAIL','PASSWORD')
print('》》》》UNIT 001 READY《《《《')
a002 = LINE('EMAIL','PASSWORD')
print('》》》》UNIT 002 READY《《《《')
a003 = LINE('EMAIL','PASSWORD')
print('》》》》UNIT 003 READY《《《《\n')

a001.log("[ M001D23 ]\n" + str(a001.authToken))
a002.log("[ M002D23 ]\n" + str(a002.authToken))
a003.log("[ M003D23 ]\n" + str(a003.authToken))

print('\n━━━━━━━━━━━━━━━━━━━━━━━━━━━')
print('\n██████╗░██████╗░███████╗██╗\n██╔══██╗██╔══██╗██╔════╝██║\n██║░░██║██████╔╝█████╗░░██║\n██║░░██║██╔══██╗██╔══╝░░╚═╝\n██████╔╝██║░░██║███████╗██╗\n╚═════╝░╚═╝░░╚═╝╚══════╝╚═╝')

print('\n》》》》PROGRAM STARTED《《《《\n')

# 𐀀 HΞLLTΞRHΞΛD ᴄᴏʀᴘ. _______________________________________________________

M001D23 = a001.getProfile().mid
M002D23 = a002.getProfile().mid
M003D23 = a003.getProfile().mid
army = [a001,a002]
antijs = [a003]
oepoll = OEPoll(a001)
call = a001
loop = asyncio.get_event_loop()
status = livejson.File('status.json', True, False, 4)
with open("settings.json","r",encoding="utf-8") as fp:
    settings = json.load(fp)
creator = status["creator"]
owner = status["owner"]
admin = status["admin"]
staff = status["staff"]
mybots = status["mybots"]
blacklist = status["blacklist"]
promax = status["promax"]
strictmode = status["strictmode"]
Bots = [M001D23,M002D23,M003D23]
Botslist = [a001,a002,a003]
resp1 = a001.getProfile().displayName
resp2 = a002.getProfile().displayName
resp3 = a003.getProfile().displayName

# 𐀀 HΞLLTΞRHΞΛD ᴄᴏʀᴘ. _______________________________________________________

helpCmd = '''┏━━━━━━━━━━━━━━━━━
┣━━━━ 𐀀 HΞLLTΞRHΞΛD ᴄᴏʀᴘ.
┣ Protection
┣ Group
┣ Access
┣ Option
┣ Settings
┣ Reboot/Shutdown
┣━━━━ ©2020 ᴍᴏ-ʙᴀɴᴢᴜ
┗━━━━━━━━━━━━━━━━━'''

proCmd = '''┏━━━━━━━━━━━━━━━━━
┣━━━━ Protection
┣ Kick/Invite [ Mention ]
┣ Protect [ Max/None ]
┣ Strictmode [ On/Off ]
┣ Protectlist
┣ Checkbot
┗━━━━━━━━━━━━━━━━━'''

groupCmd = '''┏━━━━━━━━━━━━━━━━━
┣━━━━ Group
┣ Ginfo
┣ Join
┣ Leave/Leave 1-3
┣ Invto [ Num ]
┣ Grouplist 1-3
┣ Mention/Tagall
┣ Memberlist/Pendinglist
┣ Openqr/Closeqr
┗━━━━━━━━━━━━━━━━━'''

accessCmd = '''┏━━━━━━━━━━━━━━━━━
┣━━━━ Access
┣ Blacklist/Banlist
┣ Clearban
┣ Abort/Eject
┣ Squad List
┣ View Bots/Access 
┣ Add/Del Owner [ Mention ]
┣ Add/Del Admin [ Mention ]
┣ Add/Del Staff [ Mention ]
┣ Add/Del Squad [ Mention ]
┣ Add/Del Ban [ Mention ]
┣ Owner:Recruit/Expel
┣ Admin:Recruit/Expel
┣ Staff:Recruit/Expel
┣ Squad:Add/Del
┣ Ban:Add/Del
┗━━━━━━━━━━━━━━━━━'''

optCmd ='''┏━━━━━━━━━━━━━━━━━
┣━━━━ Option
┣ Allowliff
┣ Creator
┣ Respon/Ping
┣ Speed/Debug
┣ Me/About
┣ Mid/Mid [ Mention ]
┣ Contact/Contact [ Mention ]
┗━━━━━━━━━━━━━━━━━'''

setCmd = '''┏━━━━━━━━━━━━━━━━━
┣━━━━ Settings
┣ Changepict:1-3/All
┣ Changebio:1-3/All [ Bio ]
┣ Changename:1-3/All [ Name ]
┗━━━━━━━━━━━━━━━━━'''

aboutCmd ='''┏━━━━━━━━━━━┓ ▕  HΞLLTΞRHΞΛD ᴄᴏʀᴘ.
┃▏╰━╮┏┈┓╭━╯▕┃ ▕  Protect Bot
┃▏═━┈┫𐀀┣┈━═▕┃ ▕  v5.3
┃▏╭━╯┗┈┛╰━╮▕┃ ▕  ©2020 ᴍᴏ-ʙᴀɴᴢᴜ
┗━━━━━━━━━━━┛ ▕  github.com/hellterhead'''

dreX53 = '''██████╗░██████╗░███████╗██╗
██╔══██╗██╔══██╗██╔════╝██║
██║░░██║██████╔╝█████╗░░██║
██║░░██║██╔══██╗██╔══╝░░╚═╝
██████╔╝██║░░██║███████╗██╗
╚═════╝░╚═╝░░╚═╝╚══════╝╚═╝'''

# 𐀀 HΞLLTΞRHΞΛD ᴄᴏʀᴘ. _______________________________________________________

for hlth in Botslist:
    for xdrex in Bots:
        try:
            hlth.findAndAddContactsByMid(xdrex)
        except:
            pass

def backupData():
    try:
        backup = settings
        f = codecs.open('settings.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except:
        pass

def restartProgram():
    print('\n》》》》PROGRAM RESTARTED《《《《\n')
    backupData()
    python = sys.executable
    os.execl(python, python, *sys.argv)

def runtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours,24)
    weeks, days = divmod(days,7)
    months, weeks = divmod(weeks,4)
    text = ""
    if months != 0: text += "%02d Months" % (months)
    if weeks != 0: text += " %02d Weeks" % (weeks)
    if days != 0: text += " %02d Days" % (days)
    if hours !=  0: text +=  " %02d Hours" % (hours)
    if mins != 0: text += " %02d Minutes" % (mins)
    if secs != 0: text += " %02d Seconds" % (secs)
    if text[0] == " ":
        text = text[1:]
    return text

# 𐀀 HΞLLTΞRHΞΛD ᴄᴏʀᴘ. _______________________________________________________

def logError(text):
    a001.log("[ ERROR ] {}".format(str(text)))
    tz = pytz.timezone("Asia/Jakarta")
    timeNow = datetime.now(tz=tz)
    timeHours = datetime.strftime(timeNow,"(%H:%M)")
    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    inihari = datetime.now(tz=tz)
    hr = inihari.strftime('%A')
    bln = inihari.strftime('%m')
    for i in range(len(day)):
        if hr == day[i]: hasil = hari[i]
    for k in range(0, len(bulan)):
        if bln == str(k): bln = bulan[k-1]
    time = "{}, {} - {} - {} | {}".format(str(hasil), str(inihari.strftime('%d')), str(bln), str(inihari.strftime('%Y')), str(inihari.strftime('%H:%M:%S')))
    with open("logError.txt","a") as error:
        error.write("\n[ {} ] {}".format(str(time), text))

# 𐀀 HΞLLTΞRHΞΛD ᴄᴏʀᴘ. _______________________________________________________

def sendMention(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@dreMention"
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    a001.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)

# 𐀀 HΞLLTΞRHΞΛD ᴄᴏʀᴘ. _______________________________________________________

def sendTemplate(group, data):
    xyz = LiffChatContext(group)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1602687308-GXq4Vvk9', xyzz)
    token1 = a001.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))

def sendTemplate(to, data):
    xyz = LiffChatContext(to)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1602687308-GXq4Vvk9', xyzz)
    token = a001.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))

def allowLiff():
    url = 'https://access.line.me/dialog/api/permissions'
    data = {
        'on': [
            'P',
            'CM'
        ],
        'off': []
    }
    headers = {
        'X-Line-Access': a001.authToken,
        'X-Line-Application': a001.server.APP_NAME,
        'X-Line-ChannelId': '1602687308',
        'Content-Type': 'application/json'
    }
    requests.post(url, json=data, headers=headers)

def sendFooter(receiver, text):
    label = settings["label"]
    icon = settings["iconUrl"]
    link = settings["linkUrl"]
    data = {
        "type": "text",
        "text": text,
        "sentBy": {
            "label": "{}".format(label),
            "iconUrl": "{}".format(icon),
            "linkUrl": "{}".format(link)
        }
    }
    sendTemplate(receiver, data)

# 𐀀 HΞLLTΞRHΞΛD ᴄᴏʀᴘ. _______________________________________________________

def kick(group, target):
    try:
        asd = a001.kickoutFromGroup(group, [target])
        if asd != None:
            hlthfail
    except:
        try:
            asd = a002.kickoutFromGroup(group, [target])
            if asd != None:
                hlthfail
        except:
            pass

def cancel(group, target):
    try:
        asd = a001.cancelGroupInvitation(group, [target])
        if asd != None:
            hlthfail
    except:
        try:
            asd = a002.cancelGroupInvitation(group, [target])
            if asd != None:
                hlthfail
        except:
            pass

def invite(group, target):
    try:
        a001.findAndAddContactsByMid(target)
        asd = a001.inviteIntoGroup(group, [target])
        if asd != None:
            hlthfail
    except:
        try:
            a002.findAndAddContactsByMid(target)
            asd = a002.inviteIntoGroup(group, [target])
            if asd != None:
                hlthfail
        except:
            pass

def lockqr(group):
    try:
        G = a001.getGroup(group)
        G.preventedJoinByTicket = True
        asd = a001.updateGroup(G)
        if asd != None:
            hlthfail
    except:
        try:
            G = a002.getGroup(group)
            G.preventedJoinByTicket = True
            asd = a002.updateGroup(G)
            if asd != None:
                hlthfail
        except:
            pass

def join(group):
    try:
        a001.acceptGroupInvitation(group)
    except:
        try:
            a002.acceptGroupInvitation(group)
        except:
            pass

def reject(group):
    try:
        a001.rejectGroupInvitation(group)
    except:
        try:
            a002.rejectGroupInvitation(group)
        except:
            pass

def backup(group, target):
    try:
        a001.inviteIntoGroup(group, [target])
        if target == M002D23:
            a002.acceptGroupInvitation(group)
    except:
        try:
            a002.inviteIntoGroup(group, [target])
            if target == M001D23:
                a001.acceptGroupInvitation(group)
        except:
            pass

def antijs(group, target):
    a003.acceptGroupInvitation(group)
    a003.kickoutFromGroup(group, [target])
    try:
        a003.inviteIntoGroup(group, [M001D23,M002D23])
        a001.acceptGroupInvitation(group)
        a002.acceptGroupInvitation(group)
    except:
        pass

def blacklist(target):
    try:
        if target in creator or target in owner or target in admin or target in staff or target in mybots or target in Bots:
            pass
        else:
            if target in status["blacklist"]:
                pass
            else:
                status["blacklist"].append(target)
    except:
        pass

# 𐀀 HΞLLTΞRHΞΛD ᴄᴏʀᴘ. _______________________________________________________

def logspeed():
    get_profile_time_start = time.time()
    get_profile = a001.getProfile()
    get_profile_time = time.time() - get_profile_time_start
    get_profile_took = time.time() - get_profile_time_start
    return "[ Bots Speed ]\n- Took: %.3fms\n- Taken: %.5f" % (get_profile_took,get_profile_time)
    get_profile_time_start = time.time()
    get_profile = a002.getProfile()
    get_profile_time = time.time() - get_profile_time_start
    get_profile_took = time.time() - get_profile_time_start
    return "[ Bots Speed ]\n- Took: %.3fms\n- Taken: %.5f" % (get_profile_took,get_profile_time)
    get_profile_time_start = time.time()
    get_profile = a003.getProfile()
    get_profile_time = time.time() - get_profile_time_start
    get_profile_took = time.time() - get_profile_time_start
    return "[ Bots Speed ]\n- Took: %.3fms\n- Taken: %.5f" % (get_profile_took,get_profile_time)

def debug():
    get_profile_time_start = time.time()
    get_profile = a001.getProfile()
    get_profile_time = time.time() - get_profile_time_start
    get_group_time_start = time.time()
    get_group = a001.getGroupIdsJoined()
    get_group_time = time.time() - get_group_time_start
    get_contact_time_start = time.time()
    get_contact = a001.getContact(get_profile.mid)
    get_contact_time = time.time() - get_contact_time_start
    elapsed_time = time.time() - get_profile_time_start
    return "[ Debug ]\n- Send Respon: %.5f\n- Get Profile: %.5f\n- Get Contact: %.5f\n- Get Group: %.5f" % (elapsed_time,get_profile_time,get_contact_time,get_group_time)
    get_profile_time_start = time.time()
    get_profile = a002.getProfile()
    get_profile_time = time.time() - get_profile_time_start
    get_group_time_start = time.time()
    get_group = a002.getGroupIdsJoined()
    get_group_time = time.time() - get_group_time_start
    get_contact_time_start = time.time()
    get_contact = a002.getContact(get_profile.mid)
    get_contact_time = time.time() - get_contact_time_start
    elapsed_time = time.time() - get_profile_time_start
    return "[ Debug ]\n- Send Respon: %.5f\n- Get Profile: %.5f\n- Get Contact: %.5f\n- Get Group: %.5f" % (elapsed_time,get_profile_time,get_contact_time,get_group_time)
    get_profile_time_start = time.time()
    get_profile = a003.getProfile()
    get_profile_time = time.time() - get_profile_time_start
    get_group_time_start = time.time()
    get_group = a003.getGroupIdsJoined()
    get_group_time = time.time() - get_group_time_start
    get_contact_time_start = time.time()
    get_contact = a003.getContact(get_profile.mid)
    get_contact_time = time.time() - get_contact_time_start
    elapsed_time = time.time() - get_profile_time_start
    return "[ Debug ]\n- Send Respon: %.5f\n- Get Profile: %.5f\n- Get Contact: %.5f\n- Get Group: %.5f" % (elapsed_time,get_profile_time,get_contact_time,get_group_time)

# 𐀀 HΞLLTΞRHΞΛD ᴄᴏʀᴘ. _______________________________________________________

def command(text):
    xmobz = text.lower()
    if settings['setKey']['status']:
        if xmobz.startswith(settings['setKey']['key']):
            cmd = xmobz.replace(settings['setKey']['key'],'')
        else:
            cmd = 'Undefined command'
    else:
        cmd = text.lower()
    return cmd

def removeCmd(text, key=''):
    if key == '':
        setKey = '' if not settings['setKey']['status'] else settings['setKey']['key']
    else:
        setKey = key
    text_ = text[len(setKey):]
    sep = text_.split(' ')
    return text_[len(sep[0] + ' '):]

# 𐀀 HΞLLTΞRHΞΛD ᴄᴏʀᴘ. _______________________________________________________

async def mobanzu(op):
    try:
        if settings["restartPoint"] is not None:
            a001.sendMessage(settings["restartPoint"],"[ Bots Operated Again... ]")
            settings["restartPoint"] = None
        if op.type == 0:
#            print ("[ 0 ] END OF OPERATION")
            return
        if op.type == 11 or op.type == 122:
            if op.type == 11: print ("[ 11 ] NOTIFIED UPDATE GROUP")
            else: print ("[ 122 ] NOTIFIED UPDATE CHAT")
            if op.param1 in status["promax"]:
                if op.param2 in creator or op.param2 in owner or op.param2 in admin or op.param2 in staff or op.param2 in Bots or op.param2 in mybots:
                    pass
                else:
                    d23X_1 = threading.Thread(target=blacklist, args=(op.param2,)).start()
                    try:
                        d23X_2 = threading.Thread(target=lockqr, args=(op.param1,)).start()
                        d23X_3 = threading.Thread(target=kick, args=(op.param1, op.param2)).start()
                    except:
                        pass
                if op.param2 in status["blacklist"]:
                    if op.param2 in creator or op.param2 in owner or op.param2 in admin or op.param2 in staff or op.param2 in Bots or op.param2 in mybots:
                        pass
                    else:
                        try:
                            d23X_4 = threading.Thread(target=lockqr, args=(op.param1,)).start()
                            d23X_5 = threading.Thread(target=kick, args=(op.param1, op.param2)).start()
                        except:
                            pass
                if op.param3 in status["blacklist"]:
                    if op.param2 in creator or op.param2 in owner or op.param2 in admin or op.param2 in staff or op.param2 in Bots or op.param2 in mybots:
                        pass
                    else:
                        try:
                            d23X_6 = threading.Thread(target=lockqr, args=(op.param1,)).start()
                            d23X_7 = threading.Thread(target=kick, args=(op.param1, op.param2)).start()
                        except:
                            pass
                if op.param3 == '4':
                    if op.param2 in creator or op.param2 in owner or op.param2 in admin or op.param2 in staff or op.param2 in Bots or op.param2 in mybots:
                        pass
                    else:
                        d23X_8 = threading.Thread(target=blacklist, args=(op.param2,)).start()
                        try:
                            groupqr = a001.getGroup(op.param1)
                            if groupqr.preventedJoinByTicket == False:
                                d23X_9 = threading.Thread(target=lockqr, args=(op.param1,)).start()
                                d23X_10 = threading.Thread(target=kick, args=(op.param1, op.param2)).start()
                        except:
                            try:
                                groupqr = a002.getGroup(op.param1)
                                if groupqr.preventedJoinByTicket == False:
                                    d23X_11 = threading.Thread(target=lockqr, args=(op.param1,)).start()
                                    d23X_12 = threading.Thread(target=kick, args=(op.param1, op.param2)).start()
                            except:
                                pass
                if op.param3 == '1':
                    if op.param2 in creator or op.param2 in owner or op.param2 in admin or op.param2 in staff or op.param2 in Bots or op.param2 in mybots:
                        pass
                    else:
                        d23X_13 = threading.Thread(target=blacklist, args=(op.param2,)).start()
                        try:
                            groupn = a001.getGroup(op.param1).name
                            if groupn not in settings["changeGroupName"][op.param1]:
                                progn = a001.getGroup(op.param1)
                                progn.name = settings["changeGroupName"][op.param1]
                                a001.updateGroup(progn)
                                d23X_14 = threading.Thread(target=kick, args=(op.param1, op.param2)).start()
                            else:
                                progn = a001.getGroup(op.param1).name
                                settings["changeGroupName"][op.param1] = progn
                                with open('settings.json', 'w') as fp:
                                    json.dump(settings, fp, sort_keys=True, indent=4)
                            groupp = a001.getGroup(op.param1).pictureStatus
                            if groupp not in settings["changeGroupPicture"][op.param1]:
                                progp = a001.getGroup(op.param1)
                                progp.pictureStatus = settings["changeGroupPicture"]
                                a001.updateGroupPicture(progp)
                                d23X_15 = threading.Thread(target=kick, args=(op.param1, op.param2)).start()
                            else:
                                progp = a001.getGroup(op.param1).pictureStatus
                                settings["changeGroupPicture"][op.param1] = progp
                                with open('settings.json', 'w') as fp:
                                    json.dump(settings, fp, sort_keys=True, indent=4)
                        except:
                            try:
                                groupn = a002.getGroup(op.param1).name
                                if groupn not in settings["changeGroupName"][op.param1]:
                                    progn = a002.getGroup(op.param1)
                                    progn.name = settings["changeGroupName"][op.param1]
                                    a002.updateGroup(progn)
                                    d23X_16 = threading.Thread(target=kick, args=(op.param1, op.param2)).start()
                                else:
                                    progn = a002.getGroup(op.param1).name
                                    settings["changeGroupName"][op.param1] = progn
                                    with open('settings.json', 'w') as fp:
                                        json.dump(settings, fp, sort_keys=True, indent=4)
                                groupp = a002.getGroup(op.param1).pictureStatus
                                if groupp not in settings["changeGroupPicture"][op.param1]:
                                    progp = a002.getGroup(op.param1)
                                    progp.pictureStatus = settings["changeGroupPicture"]
                                    a002.updateGroupPicture(progp)
                                    d23X_17 = threading.Thread(target=kick, args=(op.param1, op.param2)).start()
                                else:
                                    progp = a002.getGroup(op.param1).pictureStatus
                                    settings["changeGroupPicture"][op.param1] = progp
                                    with open('settings.json', 'w') as fp:
                                        json.dump(settings, fp, sort_keys=True, indent=4)
                            except:
                                pass
        if op.type == 13 or op.type == 124:
            if op.type == 13: print ("[ 13 ] NOTIFIED INVITE INTO GROUP")
            else: print ("[ 124 ] NOTIFIED INVITE INTO CHAT")
            if op.param1 in status["promax"]:
                if op.param2 in creator or op.param2 in owner or op.param2 in admin or op.param2 in staff or op.param2 in Bots or op.param2 in mybots:
                    pass
                else:
                    d23X_18 = threading.Thread(target=blacklist, args=(op.param2,)).start()
                    d23X_19 = threading.Thread(target=blacklist, args=(op.param3,)).start()
                    try:
                        d23X_20 = threading.Thread(target=cancel, args=(op.param1, op.param3)).start()
                        d23X_21 = threading.Thread(target=kick, args=(op.param1, op.param2)).start()
                    except:
                        try:
                            inv1 = op.param3.replace('\x1e',',')
                            inv2 = inv1.split(',')
                            for _mid in inv2:
                                d23X_22 = threading.Thread(target=cancel, args=(op.param1, _mid)).start()
                                d23X_23 = threading.Thread(target=kick, args=(op.param1, op.param2)).start()
                        except:
                            try:
                                inv3 = op.param3.replace('\x1e',',')
                                inv4 = inv3.split(',')
                                for _mid in inv4:
                                    d23X_24 = threading.Thread(target=cancel, args=(op.param1, _mid)).start()
                                    d23X_25 = threading.Thread(target=kick, args=(op.param1, op.param2)).start()
                            except:
                                pass
                if op.param2 in status["blacklist"]:
                    if op.param2 in creator or op.param2 in owner or op.param2 in admin or op.param2 in staff or op.param2 in Bots or op.param2 in mybots:
                        pass
                    else:
                        try:
                            d23X_26 = threading.Thread(target=cancel, args=(op.param1, op.param3)).start()
                            d23X_27 = threading.Thread(target=kick, args=(op.param1, op.param2)).start()
                        except:
                            try:
                                inv1 = op.param3.replace('\x1e',',')
                                inv2 = inv1.split(',')
                                for _mid in inv2:
                                    d23X_28 = threading.Thread(target=cancel, args=(op.param1, _mid)).start()
                                    d23X_29 = threading.Thread(target=kick, args=(op.param1, op.param2)).start()
                            except:
                                try:
                                    inv3 = op.param3.replace('\x1e',',')
                                    inv4 = inv3.split(',')
                                    for _mid in inv4:
                                        d23X_30 = threading.Thread(target=cancel, args=(op.param1, _mid)).start()
                                        d23X_31 = threading.Thread(target=kick, args=(op.param1, op.param2)).start()
                                except:
                                    pass
                if op.param3 in status["blacklist"]:
                    if op.param2 in creator or op.param2 in owner or op.param2 in admin or op.param2 in staff or op.param2 in Bots or op.param2 in mybots:
                        pass
                    else:
                        try:
                            d23X_32 = threading.Thread(target=cancel, args=(op.param1, op.param3)).start()
                            d23X_33 = threading.Thread(target=kick, args=(op.param1, op.param2)).start()
                        except:
                            try:
                                inv1 = op.param3.replace('\x1e',',')
                                inv2 = inv1.split(',')
                                for _mid in inv2:
                                    d23X_34 = threading.Thread(target=cancel, args=(op.param1, _mid)).start()
                                    d23X_35 = threading.Thread(target=kick, args=(op.param1, op.param2)).start()
                            except:
                                try:
                                    inv3 = op.param3.replace('\x1e',',')
                                    inv4 = inv3.split(',')
                                    for _mid in inv4:
                                        d23X_36 = threading.Thread(target=cancel, args=(op.param1, _mid)).start()
                                        d23X_37 = threading.Thread(target=kick, args=(op.param1, op.param2)).start()
                                except:
                                    pass
            if M001D23 in op.param3:
                if settings["autoJoin"] == True:
                    if op.param2 in creator or op.param2 in owner or op.param2 in admin or op.param2 in staff or op.param2 in Bots or op.param2 in mybots:
                        try:
                            d23X_38 = threading.Thread(target=join, args=(op.param1,)).start()
                        except:
                        	pass
                    else:
                        try:
                            d23X_39 = threading.Thread(target=reject, args=(op.param1,)).start()
                        except:
                            pass
            if M002D23 in op.param3:
                if settings["autoJoin"] == True:
                    if op.param2 in creator or op.param2 in owner or op.param2 in admin or op.param2 in staff or op.param2 in Bots or op.param2 in mybots:
                        try:
                            d23X_40 = threading.Thread(target=join, args=(op.param1,)).start()
                        except:
                        	pass
                    else:
                        try:
                            d23X_41 = threading.Thread(target=reject, args=(op.param1,)).start()
                        except:
                            pass
        if op.type == 17 or op.type == 130:
            if op.type == 17: print ("[ 17 ] NOTIFIED ACCEPT GROUP INVITATION")
            else: print ("[ 130 ] NOTIFIED ACCEPT CHAT INVITATION")
            if op.param1 in status["promax"]:
                if op.param2 in status["blacklist"]:
                    if op.param2 in creator or op.param2 in owner or op.param2 in admin or op.param2 in staff or op.param2 in Bots or op.param2 in mybots:
                        pass
                    else:
                        try:
                            d23X_42 = threading.Thread(target=kick, args=(op.param1, op.param2)).start()
                        except:
                            pass
        if op.type == 19 or op.type == 133:
            if op.type == 19: print ("[ 19 ] NOTIFIED KICKOUT FROM GROUP")
            else: print ("[ 133 ] NOTIFIED DELETE OTHER FROM CHAT")
            if op.param1 in status["promax"]:
                if op.param2 in creator or op.param2 in owner or op.param2 in admin or op.param2 in staff or op.param2 in Bots or op.param2 in mybots:
                    pass
                else:
                    d23X_43 = threading.Thread(target=blacklist, args=(op.param2,)).start()
                    try:
                        d23X_44 = threading.Thread(target=kick, args=(op.param1, op.param2)).start()
                        d23X_45 = threading.Thread(target=invite, args=(op.param1, op.param3)).start()
                    except:
                        pass
                if op.param3 in M001D23:
                    if op.param2 in creator or op.param2 in owner or op.param2 in admin or op.param2 in staff or op.param2 in Bots or op.param2 in mybots:
                        pass
                    else:
                        d23X_46 = threading.Thread(target=blacklist, args=(op.param2,)).start()
                        try:
                            d23X_47 = threading.Thread(target=kick, args=(op.param1, op.param2)).start()
                            d23X_48 = threading.Thread(target=backup, args=(op.param1, op.param3)).start()
                            d23X_49 = threading.Thread(target=antijs, args=(op.param1, op.param2)).start()
                            d23X_50 = threading.Thread(target=kick, args=(op.param1, op.param2)).start()
                        except:
                            pass
                if op.param3 in M002D23:
                    if op.param2 in creator or op.param2 in owner or op.param2 in admin or op.param2 in staff or op.param2 in Bots or op.param2 in mybots:
                        pass
                    else:
                        d23X_51 = threading.Thread(target=blacklist, args=(op.param2,)).start()
                        try:
                            d23X_52 = threading.Thread(target=kick, args=(op.param1, op.param2)).start()
                            d23X_53 = threading.Thread(target=backup, args=(op.param1, op.param3)).start()
                            d23X_54 = threading.Thread(target=antijs, args=(op.param1, op.param2)).start()
                            d23X_55 = threading.Thread(target=kick, args=(op.param1, op.param2)).start()
                        except:
                            pass
                if op.param3 in M003D23:
                    if op.param2 in creator or op.param2 in owner or op.param2 in admin or op.param2 in staff or op.param2 in Bots or op.param2 in mybots:
                        pass
                    else:
                        d23X_56 = threading.Thread(target=blacklist, args=(op.param2,)).start()
                        try:
                            d23X_57 = threading.Thread(target=kick, args=(op.param1, op.param2)).start()
                            d23X_58 = threading.Thread(target=invite, args=(op.param1, op.param3)).start()
                            d23X_59 = threading.Thread(target=kick, args=(op.param1, op.param2)).start()
                        except:
                            pass
        if op.type == 32 or op.type == 126:
            if op.type == 32: print ("[ 32 ] NOTIFIED CANCEL INVITATION GROUP")
            else: print ("[ 126 ] NOTIFIED CANCEL CHAT INVITATION")
            if op.param1 in status["promax"]:
                if op.param2 in creator or op.param2 in owner or op.param2 in admin or op.param2 in staff or op.param2 in Bots or op.param2 in mybots:
                    pass
                else:
                    d23X_60 = threading.Thread(target=blacklist, args=(op.param2,)).start()
                    try:
                        d23X_61 = threading.Thread(target=kick, args=(op.param1, op.param2)).start()
                        d23X_62 = threading.Thread(target=invite, args=(op.param1, op.param3)).start()
                    except:
                        pass
                if op.param3 == M001D23:
                    if op.param2 in creator or op.param2 in owner or op.param2 in admin or op.param2 in staff or op.param2 in Bots or op.param2 in mybots:
                        pass
                    else:
                        d23X_63 = threading.Thread(target=blacklist, args=(op.param2,)).start()
                        try:
                            d23X_64 = threading.Thread(target=kick, args=(op.param1, op.param2)).start()
                            d23X_65 = threading.Thread(target=backup, args=(op.param1, op.param3)).start()
                        except:
                            pass
                if op.param3 == M002D23:
                    if op.param2 in creator or op.param2 in owner or op.param2 in admin or op.param2 in staff or op.param2 in Bots or op.param2 in mybots:
                        pass
                    else:
                        d23X_66 = threading.Thread(target=blacklist, args=(op.param2,)).start()
                        try:
                            d23X_67 = threading.Thread(target=kick, args=(op.param1, op.param2)).start()
                            d23X_68 = threading.Thread(target=backup, args=(op.param1, op.param3)).start()
                        except:
                            pass
                if op.param3 == M003D23:
                    if op.param2 in creator or op.param2 in owner or op.param2 in admin or op.param2 in staff or op.param2 in Bots or op.param2 in mybots:
                        pass
                    else:
                        d23X_69 = threading.Thread(target=blacklist, args=(op.param2,)).start()
                        try:
                            d23X_70 = threading.Thread(target=kick, args=(op.param1, op.param2)).start()
                            d23X_71 = threading.Thread(target=invite, args=(op.param1, op.param3)).start()
                        except:
                            pass
        if op.type == 22 or op.type == 24:
            if op.type == 22: print ("[ 22 ] NOTIFIED INVITE INTO ROOM")
            else: print ("[ 24 ] NOTIFIED LEAVE ROOM")
            try:
                a001.leaveRoom(op.param1)
            except:
                try:
                    a002.leaveRoom(op.param1)
                except:
                    try:
                        a003.leaveRoom(op.param1)
                    except:
                        pass
        if op.type == 25 or op.type == 26:
            if op.type == 25: print ("[ 25 ] SEND MESSAGE")
            else: print ("[ 26 ] RECEIVE MESSAGE")
            global cmd
            global text
            global groupParam
            msg = op.message
            text = msg.text
            reply = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                if msg.toType == 0:
                    if sender != a001.profile.mid:
                        to = sender
                    else:
                        to = receiver
                if msg.toType == 1:
                    to = receiver
                if msg.toType == 2:
                    to = receiver
                if msg.contentType == 1:
                    if sender in creator or sender in owner:
                        if M001D23 in settings["updatePict"]:
                            path = a001.downloadObjectMsg(msg.id)
                            del settings["updatePict"][M001D23]
                            a001.updateProfilePicture(path)
                            a001.sendReplyMessage(reply,receiver,"[ Profile Picture ]\nSuccess Change Profile Picture")
                        if M002D23 in settings["updatePict"]:
                            path = a002.downloadObjectMsg(msg.id)
                            del settings["updatePict"][M002D23]
                            a002.updateProfilePicture(path)
                            a002.sendReplyMessage(reply,receiver,"[ Profile Picture ]\nSuccess Change Profile Picture")
                        if M003D23 in settings["updatePict"]:
                            path = a003.downloadObjectMsg(msg.id)
                            del settings["updatePict"][M003D23]
                            a003.updateProfilePicture(path)
                            a003.sendReplyMessage(reply,receiver,"[ Profile Picture ]\nSuccess Change Profile Picture")
                if msg.contentType == 13:
                    if settings["addowner"] == True:
                        if sender in creator:
                            if msg.contentMetadata["mid"] not in Bots:
                                if msg.contentMetadata["mid"] in status["owner"]:
                                    a001.sendReplyMessage(reply,receiver,"{} Already In Owner Access".format(a001.getContact(msg.contentMetadata["mid"]).displayName))
                                    settings["addowner"] = False
                                else:
                                    if msg.contentMetadata["mid"] not in status["blacklist"]:
                                        status["owner"].append(msg.contentMetadata["mid"])
                                        a001.sendReplyMessage(reply,receiver,"{} Recruit To Owner".format(a001.getContact(msg.contentMetadata["mid"]).displayName))
                                        settings["addowner"] = False
                                    else:
                                        a001.sendReplyMessage(reply,receiver,"[ Failed ]\nUser In Blacklist")
                                    settings["addowner"] = False
                    if settings["delowner"] == True:
                        if sender in creator:
                            if msg.contentMetadata["mid"] not in Bots:
                                if msg.contentMetadata["mid"] in status["owner"]:
                                    status["owner"].remove(msg.contentMetadata["mid"])
                                    a001.sendReplyMessage(reply,receiver,"{} Expel From Owner".format(a001.getContact(msg.contentMetadata["mid"]).displayName))
                                    settings["delowner"] = False
                                else:
                                    a001.sendReplyMessage(reply,receiver,"[ Failed ]\nUser Not In Owner Access")
                                settings["delowner"] = False
                    if settings["addadmin"] == True:
                        if sender in creator or sender in owner:
                            if msg.contentMetadata["mid"] not in Bots:
                                if msg.contentMetadata["mid"] in status["admin"]:
                                    a001.sendReplyMessage(reply,receiver,"{} Already In Admin Access".format(a001.getContact(msg.contentMetadata["mid"]).displayName))
                                    settings["addadmin"] = False
                                else:
                                    if msg.contentMetadata["mid"] not in status["blacklist"]:
                                        status["admin"].append(msg.contentMetadata["mid"])
                                        a001.sendReplyMessage(reply,receiver,"{} Recruit To Admin".format(a001.getContact(msg.contentMetadata["mid"]).displayName))
                                        settings["addadmin"] = False
                                    else:
                                        a001.sendReplyMessage(reply,receiver,"[ Failed ]\nUser In Blacklist")
                                    settings["addadmin"] = False
                    if settings["deladmin"] == True:
                        if sender in creator or sender in owner:
                            if msg.contentMetadata["mid"] not in Bots:
                                if msg.contentMetadata["mid"] in status["admin"]:
                                    status["admin"].remove(msg.contentMetadata["mid"])
                                    a001.sendReplyMessage(reply,receiver,"{} Expel From Admin".format(a001.getContact(msg.contentMetadata["mid"]).displayName))
                                    settings["deladmin"] = False
                                else:
                                    a001.sendReplyMessage(reply,receiver,"[ Failed ]\nUser Not In Admin Access")
                                settings["deladmin"] = False
                    if settings["addstaff"] == True:
                        if sender in creator or sender in owner or sender in admin:
                            if msg.contentMetadata["mid"] not in Bots:
                                if msg.contentMetadata["mid"] in status["staff"]:
                                    a001.sendReplyMessage(reply,receiver,"{} Already In Staff Access".format(a001.getContact(msg.contentMetadata["mid"]).displayName))
                                    settings["addstaff"] = False
                                else:
                                    if msg.contentMetadata["mid"] not in status["blacklist"]:
                                        status["staff"].append(msg.contentMetadata["mid"])
                                        a001.sendReplyMessage(reply,receiver,"{} Recruit To Staff".format(a001.getContact(msg.contentMetadata["mid"]).displayName))
                                        settings["addstaff"] = False
                                    else:
                                        a001.sendReplyMessage(reply,receiver,"[ Failed ]\nUser In Blacklist")
                                    settings["addstaff"] = False
                    if settings["delstaff"] == True:
                        if sender in creator or sender in owner or sender in admin:
                            if msg.contentMetadata["mid"] not in Bots:
                                if msg.contentMetadata["mid"] in status["staff"]:
                                    status["staff"].remove(msg.contentMetadata["mid"])
                                    a001.sendReplyMessage(reply,receiver,"{} Expel From Staff".format(a001.getContact(msg.contentMetadata["mid"]).displayName))
                                    settings["delstaff"] = False
                                else:
                                    a001.sendReplyMessage(reply,receiver,"[ Failed ]\nUser Not In Staff Access")
                                settings["delstaff"] = False
                    if settings["addbots"] == True:
                        if sender in creator or sender in owner:
                            if msg.contentMetadata["mid"] not in Bots:
                                if msg.contentMetadata["mid"] in status["mybots"]:
                                    a001.sendReplyMessage(reply,receiver,"{} Already In Squad List".format(a001.getContact(msg.contentMetadata["mid"]).displayName))
                                    settings["addbots"] = False
                                else:
                                    if msg.contentMetadata["mid"] not in status["blacklist"]:
                                        status["mybots"].append(msg.contentMetadata["mid"])
                                        a001.sendReplyMessage(reply,receiver,"{} Add To Squad".format(a001.getContact(msg.contentMetadata["mid"]).displayName))
                                        settings["addbots"] = False
                                    else:
                                        a001.sendReplyMessage(reply,receiver,"[ Failed ]\nUser In Blacklist")
                                    settings["addbots"] = False
                    if settings["delbots"] == True:
                        if sender in creator or sender in owner:
                            if msg.contentMetadata["mid"] not in Bots:
                                if msg.contentMetadata["mid"] in status["mybots"]:
                                    status["mybots"].remove(msg.contentMetadata["mid"])
                                    a001.sendReplyMessage(reply,receiver,"{} Delete From Squad".format(a001.getContact(msg.contentMetadata["mid"]).displayName))
                                    settings["delbots"] = False
                                else:
                                    a001.sendReplyMessage(reply,receiver,"[ Failed ]\nUser Not In Squad List")
                                settings["delbots"] = False
                    if settings["addban"] == True:
                        if sender in creator or sender in owner:
                            if msg.contentMetadata["mid"] not in Bots:
                                if msg.contentMetadata["mid"] in status["blacklist"]:
                                    a001.sendReplyMessage(reply,receiver,"{} Already In Blacklist".format(a001.getContact(msg.contentMetadata["mid"]).displayName))
                                    settings["addban"] = False
                                else:
                                    status["blacklist"].append(msg.contentMetadata["mid"])
                                    a001.sendReplyMessage(reply,receiver,"{} Add To Blacklist".format(a001.getContact(msg.contentMetadata["mid"]).displayName))
                                    settings["addban"] = False
                    if settings["delban"] == True:
                        if sender in creator or sender in owner or sender in admin:
                            if msg.contentMetadata["mid"] not in Bots:
                                if msg.contentMetadata["mid"] in status["blacklist"]:
                                    status["blacklist"].remove(msg.contentMetadata["mid"])
                                    a001.sendReplyMessage(reply,receiver,"{} Delete From Blacklist".format(a001.getContact(msg.contentMetadata["mid"]).displayName))
                                    settings["delban"] = False
                                else:
                                    a001.sendReplyMessage(reply,receiver,"[ Failed ]\nUser Not In Blacklist")
                                settings["delban"] = False
                if msg.contentType == 0:
                    if text is None:
                        return
                    else:
                        hellterhead = command(text)
                        hlth = " ".join(hellterhead.split())
                    for hlth in hellterhead.split(' & '):
                        if hlth == "help":
                            if sender in creator or sender in owner or sender in admin or sender in staff:
                                sendFooter(receiver,str(helpCmd))
                        elif hlth == "protection":
                            if sender in creator or sender in owner or sender in admin or sender in staff:
                                sendFooter(receiver,str(proCmd))
                        elif hlth == "group":
                            if sender in creator or sender in owner or sender in admin or sender in staff:
                                sendFooter(receiver,str(groupCmd))
                        elif hlth == "access":
                            if sender in creator or sender in owner or sender in admin or sender in staff:
                                sendFooter(receiver,str(accessCmd))
                        elif hlth == "option":
                            if sender in creator or sender in owner or sender in admin or sender in staff:
                                sendFooter(receiver,str(optCmd))
                        elif hlth == "settings":
                            if sender in creator or sender in owner or sender in admin or sender in staff:
                                sendFooter(receiver,str(setCmd))
                        elif hlth.startswith("allowliff"):
                            if sender in creator or sender in owner or sender in admin or sender in staff:
                                try:
                                    allowLiff()
                                    a001.sendReplyMessage(reply,receiver,"Flex Mode Enable")
                                except:
                                    a001.sendMessage(receiver,"line://app/1602687308-GXq4Vvk9/?type=text&text=セルボットＤＲＥ！")
                        elif hlth == "mention" or hlth == "tagall":
                            group = a001.getGroup(receiver)
                            memb = [contact.mid for contact in group.members]
                            memb.remove(a001.getProfile().mid)
                            a001.datamention(receiver,"{}".format(group.name),memb)
                        elif hlth == "reboot":
                            if sender in creator or sender in owner:
                                a001.sendMessage(receiver,"[ Rebooting... ]")
                                settings["restartPoint"] = receiver
                                restartProgram()
                        elif hlth == "shutdown":
                            if sender in creator or sender in owner:
                                a001.sendMessage(receiver,"[ Turn Off Program ]")
                                sys.exit('\n》》》》PROGRAM TERMINATED《《《《\n')
                        elif hlth == "clearchat":
                            if sender in creator or sender in owner or sender in admin:
                                for x in Botslist:
                                    x.removeAllMessages(op.param2)
                                for z in Botslist:
                                    z.sendReplyMessage(reply,receiver,"[ All Chat Cleared ]")
                        elif hlth == "creator":
                            sendFooter(receiver,str(dreX53))
                        elif hlth == "about":
                            sendFooter(receiver,str(aboutCmd))
                        elif hlth == "me":
                            contact = a001.getContact(sender)
                            a001.sendContact(receiver, contact.mid)
                        elif hlth == "mid":
                            contact = a001.getContact(sender)
                            a001.sendReplyMessage(reply,receiver, "{}".format(contact.mid))
                        elif hlth.startswith("mid "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                mcont = ""
                                for ls in lists:
                                    mcont += "{}".format(str(ls))
                                a001.sendReplyMessage(reply,receiver,str(mcont))
                        elif hlth == "contact":
                            contact = a001.getContact(sender)
                            cont = contact.mid
                            a001.sendContact(receiver, cont)
                        elif hlth.startswith("contact "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = a001.getContact(ls)
                                    cont = contact.mid
                                    a001.sendContact(receiver, cont)
                        elif hlth == "ping":
                            a001.sendMessage(receiver,"PING!!!")
                            a002.sendMessage(receiver,"PING!!!")
                            a003.sendMessage(receiver,"PING!!!")
                        elif hlth == "respon":
                            if sender in creator or sender in owner or sender in admin or sender in staff:
                                a001.sendReplyMessage(reply,receiver,"[ {} ]".format(resp1))
                                a002.sendReplyMessage(reply,receiver,"[ {} ]".format(resp2))
                                a003.sendReplyMessage(reply,receiver,"[ {} ]".format(resp3))
                        elif hlth == "speed":
                            if sender in creator or sender in owner or sender in admin or sender in staff:
                                a001.sendReplyMessage(reply,receiver,logspeed())
                                a002.sendReplyMessage(reply,receiver,logspeed())
                                a003.sendReplyMessage(reply,receiver,logspeed())
                        elif hlth == "debug":
                            if sender in creator or sender in owner or sender in admin or sender in staff:
                                a001.sendReplyMessage(reply,receiver,debug())
                                a002.sendReplyMessage(reply,receiver,debug())
                                a003.sendReplyMessage(reply,receiver,debug())
                        elif hlth == "ginfo":
                            if sender in creator or sender in owner or sender in admin or sender in staff:
                                group = a001.getGroup(receiver)
                                try:
                                    gCreator = group.creator.displayName
                                except:
                                    gCreator = "Not Found"
                                if group.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(group.invitee))
                                if group.preventedJoinByTicket == True:
                                    gQr = "Clossed"
                                    gTicket = "Nothing"
                                else:
                                    gQr = "Opened"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(a001.reissueGroupTicket(group.id)))
                                hlthX = "[ Group Info ]"
                                hlthX += "\n- Group Name: {}".format(str(group.name))
                                hlthX += "\n- Group ID: {}".format(group.id)
                                hlthX += "\n- Creator: {}".format(str(gCreator))
                                hlthX += "\n- Member: {}".format(str(len(group.members)))
                                hlthX += "\n- Pending: {}".format(gPending)
                                hlthX += "\n- Group URL: {}".format(gQr)
                                hlthX += "\n- Group Ticket: {}".format(gTicket)
                                a001.sendReplyMessage(reply,receiver,hlthX)
                        elif hlth == "openqr":
                            if sender in creator or sender in owner or sender in admin:
                                group = a001.getGroup(receiver)
                                group.preventedJoinByTicket = False
                                a001.updateGroup(group)
                                gurl = a001.reissueGroupTicket(receiver)
                                a001.sendReplyMessage(reply,receiver,"QR Group Opened")
                                a001.sendReplyMessage(reply,receiver,"line://ti/g/" + gurl)
                        elif hlth == "closeqr":
                            if sender in creator or sender in owner or sender in admin:
                                group = a001.getGroup(receiver)
                                group.preventedJoinByTicket = True
                                a001.updateGroup(group)
                                a001.sendReplyMessage(reply,receiver,"QR Group Closed")
                        elif hlth == "leave":
                            if sender in creator or sender in owner or sender in admin:
                                for bot in Botslist:
                                    bot.leaveGroup(receiver)
                        elif hlth.startswith("leave "):
                            if sender in creator or sender in owner or sender in admin:
                                spl = hlth.replace("leave ","")
                                if spl == "1":
                                    a001.leaveGroup(receiver)
                                if spl == "2":
                                    a002.leaveGroup(receiver)
                                if spl == "3":
                                    a003.leaveGroup(receiver)
                        elif hlth == "join":
                            if sender in creator or sender in owner or sender in admin:
                                G = a001.getGroup(receiver)
                                G.preventedJoinByTicket = False
                                a001.updateGroup(G)
                                links = a001.reissueGroupTicket(receiver)
                                a002.acceptGroupInvitationByTicket(receiver,links)
                                a003.acceptGroupInvitationByTicket(receiver,links)
                                G = a001.getGroup(receiver)
                                G.preventedJoinByTicket = True
                                a001.updateGroup(G)
                        elif hlth == "blacklist" or hlth == "banlist":
                            if sender in creator or sender in owner or sender in admin or sender in staff:
                                if len(status["blacklist"]) > 0:
                                    h = [a for a in status["blacklist"]]
                                    k = len(h)//20
                                    for aa in range(k+1):
                                        if aa == 0:dd = '┏━ Blacklist User';no=aa
                                        else:dd = '';no=aa*20
                                        msgas = dd
                                        for a in h[aa*20:(aa+1)*20]:
                                            no+=1
                                            if no == len(h):
                                                msgas+='\n┣ {}. @!'.format(no)
                                            else:
                                                msgas += '\n┣ {}. @!'.format(no)
                                        msgas += '\n┗━━━━'
                                        sendMention(to, msgas, h[aa*20:(aa+1)*20])
                                else:
                                    a001.sendReplyMessage(reply,receiver,"[ Doesn't Have Any Blacklist User ]")
                        elif hlth == "clearban":
                            if sender in creator or sender in owner or sender in admin:
                                if len(status["blacklist"]) > 0:
                                    a001.sendReplyMessage(reply,receiver, "[ {} User Cleared ]".format(len(status["blacklist"])))
                                    status["blacklist"].clear()
                                else:
                                    a001.sendReplyMessage(reply,receiver,"[ Doesn't Have Any Blacklist User ]")
                        elif hlth == "squad list":
                            if sender in creator or sender in owner or sender in admin or sender in staff:
                                ma = ""
                                a = 0
                                for ls in mybots:
                                    a = a + 1
                                    end = '\n'
                                    ma += '┣ ' + str(a) + ". " +a001.getContact(ls).displayName + "\n"
                                a001.sendReplyMessage(reply,receiver, "┏━ 𐀀 HΞLLTΞRHΞΛD ᴄᴏʀᴘ.\n┣━━━━ List Bots\n"+ma+"┗━ Total [ %s ] Bots" %(str(len(mybots))))
                        elif hlth == "view bots":
                            if sender in creator or sender in owner or sender in admin or sender in staff:
                                ma = ""
                                a = 0
                                for ls in Bots:
                                    a = a + 1
                                    end = '\n'
                                    ma += '┣ ' + str(a) + ". " +a001.getContact(ls).displayName + "\n"
                                a001.sendReplyMessage(reply,receiver, "┏━ 𐀀 HΞLLTΞRHΞΛD ᴄᴏʀᴘ.\n┣━━━━ List Bots\n"+ma+"┗━ Total [ %s ] Bots" %(str(len(Bots))))
                        elif hlth == "view access":
                            if sender in creator or sender in owner or sender in admin or sender in staff:
                                ma = ""
                                mb = ""
                                mc = ""
                                md = ""
                                a = 0
                                b = 0
                                c = 0
                                d = 0
                                for ls in creator:
                                    a = a + 1
                                    end = '\n'
                                    ma += '┣ ' + str(a) + ". " +a001.getContact(ls).displayName + "\n"
                                for ls in owner:
                                    b = b + 1
                                    end = '\n'
                                    mb += '┣ ' + str(b) + ". " +a001.getContact(ls).displayName + "\n"
                                for ls in admin:
                                    c = c + 1
                                    end = '\n'
                                    mc += '┣ ' + str(c) + ". " +a001.getContact(ls).displayName + "\n"
                                for ls in staff:
                                    d = d + 1
                                    end = '\n'
                                    md += '┣ ' + str(d) + ". " +a001.getContact(ls).displayName + "\n"
                                a001.sendReplyMessage(msg.id, to, "┏━ 𐀀 HΞLLTΞRHΞΛD ᴄᴏʀᴘ.\n┣━━━━ List Access\n┣━━━━ Creator\n"+ma+"┣━━━━ Owner\n"+mb+"┣━━━━ Admin\n"+mc+"┣━━━━ Staff\n"+md+"┗━ Total [ %s ] Access" %(str(len(creator)+len(owner)+len(admin)+len(staff))))
                        elif hlth.startswith("add owner"):
                            if sender in creator:
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]["M"]
                                targets = []
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for xbot in Botslist:
                                    for xtarg in targets:
                                        try:
                                            xbot.findAndAddContactsByMid(xtarg)
                                        except:
                                            pass
                                for target in targets:
                                    try:
                                        status["owner"].append(target)
                                        sendMention(to,"[ Add Owner ]\nUser @! Added To Owner Access",[target])
                                    except:
                                        pass
                            else:
                                a001.sendReplyMessage(reply,receiver,"[ Add Owner ]\nCreator Permission")
                        elif hlth.startswith("del owner"):
                            if sender in creator:
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]["M"]
                                targets = []
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for target in targets:
                                    try:
                                        status["owner"].remove(target)
                                        sendMention(to,"[ Delete Owner ]\nUser @! Deleted From Owner Access",[target])
                                    except:
                                        pass
                            else:
                                a001.sendReplyMessage(reply,receiver,"[ Delete Owner ]\nCreator Permission")
                        elif hlth.startswith("add admin"):
                            if sender in creator or sender in owner:
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]["M"]
                                targets = []
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for xbot in Botslist:
                                    for xtarg in targets:
                                        try:
                                            xbot.findAndAddContactsByMid(xtarg)
                                        except:
                                            pass
                                for target in targets:
                                    try:
                                        status["admin"].append(target)
                                        sendMention(to,"[ Add Admin ]\nUser @! Added To Admin Access",[target])
                                    except:
                                        pass
                            else:
                                a001.sendReplyMessage(reply,receiver,"[ Add Admin ]\nOwner Permission")
                        elif hlth.startswith("del admin"):
                            if sender in creator or sender in owner:
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]["M"]
                                targets = []
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for target in targets:
                                    try:
                                        status["admin"].remove(target)
                                        sendMention(to,"[ Delete Admin ]\nUser @! Deleted From Admin Access",[target])
                                    except:
                                       pass
                            else:
                                a001.sendReplyMessage(reply,receiver,"[ Delete Admin ]\nOwner Permission")
                        elif hlth.startswith("add staff"):
                            if sender in creator or sender in owner or sender in admin:
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]["M"]
                                targets = []
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for xbot in Botslist:
                                    for xtarg in targets:
                                        try:
                                            xbot.findAndAddContactsByMid(xtarg)
                                        except:
                                            pass
                                for target in targets:
                                    try:
                                        status["staff"].append(target)
                                        sendMention(to,"[ Add Staff ]\nUser @! Added To Staff Access",[target])
                                    except:
                                        pass
                            else:
                                a001.sendReplyMessage(reply,receiver,"[ Add Staff ]\nOwner/Admin Permission")
                        elif hlth.startswith("del staff"):
                            if sender in creator or sender in owner or sender in admin:
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]["M"]
                                targets = []
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for target in targets:
                                    try:
                                        status["staff"].remove(target)
                                        sendMention(to,"[ Delete Staff ]\nUser @! Deleted From Staff Access",[target])
                                    except:
                                        pass
                            else:
                                a001.sendReplyMessage(reply,receiver,"[ Delete Staff ]\nOwner/Admin Permission")
                        elif hlth.startswith("add squad"):
                            if sender in creator or sender in owner:
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]["M"]
                                targets = []
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for xbot in Botslist:
                                    for xtarg in targets:
                                        try:
                                            xbot.findAndAddContactsByMid(xtarg)
                                        except:
                                            pass
                                for target in targets:
                                    try:
                                        status["mybots"].append(target)
                                        sendMention(to,"[ Add Squad ]\nUser @! Added To Squad List",[target])
                                    except:
                                        pass
                            else:
                                a001.sendReplyMessage(reply,receiver,"[ Add Squad ]\nOwner Permission")
                        elif hlth.startswith("del squad"):
                            if sender in creator or sender in owner:
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]["M"]
                                targets = []
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for target in targets:
                                    try:
                                        status["mybots"].remove(target)
                                        sendMention(to,"[ Delete Squad ]\nUser @! Deleted From Squad List",[target])
                                    except:
                                        pass
                            else:
                                a001.sendReplyMessage(reply,receiver,"[ Delete Squad ]\nOwner Permission")
                        elif hlth.startswith("add ban"):
                            if sender in creator or sender in owner:
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]["M"]
                                targets = []
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for target in targets:
                                    try:
                                        status["blacklist"].append(target)
                                        sendMention(to,"[ Add Blacklist ]\nUser @! Added To Blacklist User",[target])
                                    except:
                                        pass
                            else:
                                a001.sendReplyMessage(reply,receiver,"[ Add Blacklist ]\nOwner Permission")
                        elif hlth.startswith("del ban"):
                            if sender in creator or sender in owner:
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]["M"]
                                targets = []
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for target in targets:
                                    try:
                                        status["blacklist"].remove(target)
                                        sendMention(to,"[ Delete Blacklist ]\nUser @! Deleted From Blacklist User",[target])
                                    except:
                                         pass
                            else:
                                a001.sendReplyMessage(reply,receiver,"[ Delete Blacklist ]\nOwner Permission")
                        elif hlth.startswith("owner:"):
                            if sender in creator:
                                spl = hlth.replace("owner:","")
                                if spl == "recruit":
                                    settings["addowner"] = True
                                    a001.sendReplyMessage(reply,receiver,"[ Add Owner ]\nPlease Send Contact To Add")
                                if spl == "expel":
                                    settings["delowner"] = True
                                    a001.sendReplyMessage(reply,receiver,"[ Delete Owner ]\nPlease Send Contact To Delete")
                            else:
                                a001.sendReplyMessage(reply,receiver,"[ Access Denied ]\nCreator Permission")
                        elif hlth.startswith("admin:"):
                            if sender in creator or sender in owner:
                                spl = hlth.replace("admin:","")
                                if spl == "recruit":
                                    settings["addadmin"] = True
                                    a001.sendReplyMessage(reply,receiver,"[ Add Admin ]\nPlease Send Contact To Add")
                                if spl == "expel":
                                    settings["deladmin"] = True
                                    a001.sendReplyMessage(reply,receiver,"[ Delete Admin ]\nPlease Send Contact To Delete")
                            else:
                                a001.sendReplyMessage(reply,receiver,"[ Access Denied ]\nOwner Permission")
                        elif hlth.startswith("staff:"):
                            if sender in creator or sender in owner or sender in admin:
                                spl = hlth.replace("staff:","")
                                if spl == "recruit":
                                    settings["addstaff"] = True
                                    a001.sendReplyMessage(reply,receiver,"[ Add Staff ]\nPlease Send Contact To Add")
                                if spl == "expel":
                                    settings["delstaff"] = True
                                    a001.sendReplyMessage(reply,receiver,"[ Delete Staff ]\nPlease Send Contact To Delete")
                            else:
                                a001.sendReplyMessage(reply,receiver,"[ Access Denied ]\nAdmin Permission")
                        elif hlth.startswith("squad:"):
                            if sender in creator or sender in owner:
                                spl = hlth.replace("squad:","")
                                if spl == "add":
                                    settings["addbots"] = True
                                    a001.sendReplyMessage(reply,receiver,"[ Add Squad ]\nPlease Send Contact To Add")
                                if spl == "del":
                                    settings["delbots"] = True
                                    a001.sendReplyMessage(reply,receiver,"[ Delete Squad ]\nPlease Send Contact To Delete")
                            else:
                                a001.sendReplyMessage(reply,receiver,"[ Access Denied ]\nOwner Permission")
                        elif hlth.startswith("ban:"):
                            if sender in creator or sender in owner:
                                spl = hlth.replace("ban:","")
                                if spl == "add":
                                    settings["addban"] = True
                                    a001.sendReplyMessage(reply,receiver,"[ Add Blacklist ]\nPlease Send Contact To Add")
                                if spl == "del":
                                    settings["delban"] = True
                                    a001.sendReplyMessage(reply,receiver,"[ Delete Blacklist ]\nPlease Send Contact To Delete")
                            else:
                                a001.sendReplyMessage(reply,receiver,"[ Access Denied ]\nOwner Permission")
                        elif hlth == "abort" or hlth == "eject":
                            if sender in creator:
                                settings["addadmin"] = False
                                settings["addban"] = False
                                settings["addbots"] = False
                                settings["addowner"] = False
                                settings["addstaff"] = False
                                settings["deladmin"] = False
                                settings["delban"] = False
                                settings["delbots"] = False
                                settings["delowner"] = False
                                settings["delstaff"] = False
                                a001.sendReplyMessage(reply,receiver,"Command Aborted")
                        elif hlth.startswith("grouplist "):
                            if sender in creator or sender in owner or sender in admin:
                                spl = hlth.replace("grouplist ","")
                                if spl == "1":
                                    group = a001.getGroupIdsJoined()
                                    getg = a001.getGroups(group)
                                    num = 1
                                    msgs = "┏━ Group List"
                                    msgs += "\n┣━━━━ {}".format(resp1)
                                    for ids in getg:
                                       msgs += "\n┣ %i. %s" % (num, ids.name) + " (" + str(len(ids.members)) + ")"
                                       num = (num+1)
                                    msgs += "\n┗━ Total [ %i ] Group" % len(getg)
                                    a001.sendReplyMessage(reply,receiver,"{}".format(str(msgs)))
                                if spl == "2":
                                    group = a002.getGroupIdsJoined()
                                    getg = a002.getGroups(group)
                                    num = 1
                                    msgs = "┏━ Group List"
                                    msgs += "\n┣━━━━ {}".format(resp2)
                                    for ids in getg:
                                       msgs += "\n┣ %i. %s" % (num, ids.name) + " (" + str(len(ids.members)) + ")"
                                       num = (num+1)
                                    msgs += "\n┗━ Total [ %i ] Group" % len(getg)
                                    a002.sendReplyMessage(reply,receiver,"{}".format(str(msgs)))
                                if spl == "3":
                                    group = a003.getGroupIdsJoined()
                                    getg = a003.getGroups(group)
                                    num = 1
                                    msgs = "┏━ Group List"
                                    msgs += "\n┣━━━━ {}".format(resp3)
                                    for ids in getg:
                                       msgs += "\n┣ %i. %s" % (num, ids.name) + " (" + str(len(ids.members)) + ")"
                                       num = (num+1)
                                    msgs += "\n┗━ Total [ %i ] Group" % len(getg)
                                    a003.sendReplyMessage(reply,receiver,"{}".format(str(msgs)))
                        elif hlth == "memberlist":
                            if sender in creator or sender in owner or sender in admin or sender in staff:
                                getg = a001.getGroup(receiver)
                                no = 1
                                ret = "┏━ Member List\n┣━━━━ {}".format(getg.name)
                                if getg.members is None:
                                    a001.sendReplyMessage(reply,receiver,"Not Found")
                                else:
                                    for i in getg.members:
                                        ret += "\n┣ {}. {}".format(no,a001.getContact(i.mid).displayName)
                                        no = (no+1)
                                    ret += "\n┗━ Total [ %i ] Member" % len(getg.members)
                                    a001.sendReplyMessage(reply,receiver,ret)
                        elif hlth == "pendinglist":
                            if sender in creator or sender in owner or sender in admin or sender in staff:
                                getg = a001.getGroup(receiver)
                                no = 1
                                ret = "┏━ Pending List\n┣━━━━ {}".format(getg.name)
                                if getg.invitee is None:
                                    a001.sendReplyMessage(reply,receiver,"Not Found")
                                else:
                                    for i in getg.invitee:
                                        ret += "\n┣ {}. {}".format(no,a001.getContact(i.mid).displayName)
                                        no = (no+1)
                                    ret += "\n┗━ Total [ %i ] Pending" % len(getg.invitee)
                                    a001.sendReplyMessage(reply,receiver,ret)
                        elif hlth == "protectlist":
                            if sender in creator or sender in owner or sender in admin or sender in staff:
                                ma = ""
                                mb = ""
                                a = 0
                                b = 0
                                for ls in promax:
                                    a = a + 1
                                    end = '\n'
                                    ma += '┣ ' + str(a) + ". " +a001.getGroup(ls).name + "\n"
                                for ls in strictmode:
                                    b = b + 1
                                    end = '\n'
                                    mb += '┣ ' + str(b) + ". " +a001.getGroup(ls).name + "\n"
                                a001.sendReplyMessage(reply, receiver, "┏━ 𐀀 HΞLLTΞRHΞΛD ᴄᴏʀᴘ.\n┣━━━━ List Protect\n┣━━━━ Protect Max\n"+ma+"┣━━━━ Strict Mode\n"+mb+"┗━ Total [ %s ] Protection" %(str(len(promax)+len(strictmode))))
                        elif hlth.startswith("protect "):
                            if sender in creator or sender in owner or sender in admin:
                                spl = hlth.replace("protect ","")
                                if spl == "max":
                                    if receiver in status["promax"]:
                                        hlth = "Group Protection Max"
                                    else:
                                        status["promax"].append(receiver)
                                        hlth = "Access Granted - Protection Active"
                                        try:
                                            group = a001.getGroup(receiver)
                                            if group.preventedJoinByTicket == False:
                                                progqr = a001.getGroup(receiver)
                                                progqr.preventedJoinByTicket = True
                                                a001.updateGroup(progqr)
                                            settings["changeGroupName"][receiver] = group.name
                                            settings["changeGroupPicture"][receiver] = group.pictureStatus
                                            with open('settings.json', 'w') as fp:
                                                json.dump(settings, fp, sort_keys=True, indent=4)
                                        except:
                                            pass
                                    a001.sendReplyMessage(reply,receiver,"[ Protection ]\n" + hlth)
                                if spl == "none":
                                    if receiver in status["promax"]:
                                        status["promax"].remove(receiver)
                                        hlth = "Access Granted - Protection Nonactive"
                                    else:
                                        hlth = "Group Protection None"
                                    a001.sendReplyMessage(reply,receiver,"[ Protection ]\n" + hlth)
                        elif hlth.startswith("strictmode "):
                            if sender in creator or sender in owner or sender in admin:
                                spl = hlth.replace("strictmode ","")
                                if spl == "on":
                                    if receiver in status["strictmode"]:
                                        a001.sendReplyMessage(reply,receiver,"[ Strict Mode ]\nStill Active")
                                    else:
                                        status["strictmode"].append(receiver)
                                        a001.sendReplyMessage(reply,receiver,"[ Strict Mode ]\nAccess Granted - Strict Mode Enable")
                                        try:
                                            a001.inviteIntoGroup(receiver,[M003D23])
                                        except:
                                            try:
                                                a002.inviteIntoGroup(receiver,[M003D23])
                                            except:
                                                try:
                                                    a003.leaveGroup(receiver)
                                                    a001.inviteIntoGroup(receiver,[M003D23])
                                                except:
                                                    pass
                                if spl == "off":
                                    if receiver in status["strictmode"]:
                                        status["strictmode"].remove(receiver)
                                        a001.sendReplyMessage(reply,receiver,"[ Strict Mode ]\nAccess Granted - Strict Mode Disable")
                                        try:
                                            a003.leaveGroup(receiver)
                                        except:
                                            try:
                                                a003.acceptGroupInvitation(receiver)
                                            except:
                                                pass
                                    else:
                                        a001.sendReplyMessage(reply,receiver,"[ Strict Mode ]\nNot Active")
                        elif hlth.startswith("checkbot"):
                            if sender in creator or sender in owner or sender in admin:
                                try:a001.inviteIntoGroup(to, [M001D23]);has = "OK"
                                except:has = "NOT"
                                try:a001.kickoutFromGroup(to, [M001D23]);has1 = "OK"
                                except:has1 = "NOT"
                                if has == "OK":sil = "Normal"
                                else:sil = "Down!"
                                if has1 == "OK":sil1 = "Normal"
                                else:sil1 = "Down!"
                                a001.sendReplyMessage(reply, receiver, "[ Bots Status ]\n- Invite: {}\n- Kick: {}".format(sil1,sil))
                                try:a002.inviteIntoGroup(to, [M002D23]);has = "OK"
                                except:has = "NOT"
                                try:a002.kickoutFromGroup(to, [M002D23]);has1 = "OK"
                                except:has1 = "NOT"
                                if has == "OK":sil = "Normal"
                                else:sil = "Down!"
                                if has1 == "OK":sil1 = "Normal"
                                else:sil1 = "Down!"
                                a002.sendReplyMessage(reply, receiver, "[ Bots Status ]\n- Invite: {}\n- Kick: {}".format(sil1,sil))
                                try:a003.inviteIntoGroup(to, [M003D23]);has = "OK"
                                except:has = "NOT"
                                try:a003.kickoutFromGroup(to, [M003D23]);has1 = "OK"
                                except:has1 = "NOT"
                                if has == "OK":sil = "Normal"
                                else:sil = "Down!"
                                if has1 == "OK":sil1 = "Normal"
                                else:sil1 = "Down!"
                            a003.sendReplyMessage(reply, receiver, "[ Bots Status ]\n- Invite: {}\n- Kick: {}".format(sil1,sil))
                        elif hlth.startswith("changename:1 "):
                            if sender in creator or sender in owner:
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                if len(name) <= 20:
                                    dname = a001.getProfile()
                                    dname.displayName = name
                                    a001.updateProfile(dname)
                                    a001.sendReplyMessage(reply,receiver,"[ Display Name ]\nDisplay Name Changed To {}".format(str(name)))
                                else:
                                    a001.sendReplyMessage(reply,receiver,"[ Display Name ]\nAccess Limited For Owner Only")
                        elif hlth.startswith("changename:2 "):
                            if sender in creator or sender in owner:
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                if len(name) <= 20:
                                    dname = a002.getProfile()
                                    dname.displayName = name
                                    a002.updateProfile(dname)
                                    a002.sendReplyMessage(reply,receiver,"[ Display Name ]\nDisplay Name Changed To {}".format(str(name)))
                                else:
                                     a002.sendReplyMessage(reply,receiver,"[ Display Name ]\nAccess Limited For Owner Only")
                        elif hlth.startswith("changename:3 "):
                            if sender in creator or sender in owner:
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                if len(name) <= 20:
                                    dname = a003.getProfile()
                                    dname.displayName = name
                                    a003.updateProfile(dname)
                                    a003.sendReplyMessage(reply,receiver,"[ Display Name ]\nDisplay Name Changed To {}".format(str(name)))
                            else:
                                a003.sendReplyMessage(reply,receiver,"[ Display Name ]\nAccess Limited For Owner Only")
                        elif hlth.startswith("changename:all "):
                            if sender in creator or sender in owner:
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                if len(name) <= 20:
                                    dname1 = a001.getProfile()
                                    dname1.displayName = name
                                    a001.updateProfile(dname1)
                                    a001.sendReplyMessage(reply,receiver,"[ Display Name ]\nDisplay Name Changed To {}".format(str(name)))
                                    dname2 = a002.getProfile()
                                    dname2.displayName = name
                                    a002.updateProfile(dname2)
                                    a002.sendReplyMessage(reply,receiver,"[ Display Name ]\nDisplay Name Changed To {}".format(str(name)))
                                    dname3 = a003.getProfile()
                                    dname3.displayName = name
                                    a003.updateProfile(dname3)
                                    a003.sendReplyMessage(reply,receiver,"[ Display Name ]\nDisplay Name Changed To {}".format(str(name)))
                            else:
                                for a in Botslist:
                                    a.sendReplyMessage(reply,receiver,"[ Display Name ]\nAccess Limited For Owner Only")
                        elif hlth.startswith("changebio:1 "):
                            if sender in creator or sender in owner:
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                if len(name) <= 500:
                                    bio = a001.getProfile()
                                    bio.statusMessage = name
                                    a001.updateProfile(bio)
                                    a001.sendReplyMessage(reply,receiver,"[ Status Message ]\nStatus Message Changed To {}".format(str(name)))
                            else:
                                a001.sendReplyMessage(reply,receiver,"[ Status Message ]\nAccess Limited For Owner Only")
                        elif hlth.startswith("changebio:2 "):
                            if sender in creator or sender in owner:
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                if len(name) <= 500:
                                    bio = a002.getProfile()
                                    bio.statusMessage = name
                                    a002.updateProfile(bio)
                                    a002.sendReplyMessage(reply,receiver,"[ Status Message ]\nStatus Message Changed To {}".format(str(name)))
                            else:
                                a002.sendReplyMessage(reply,receiver,"[ Status Message ]\nAccess Limited For Owner Only")
                        elif hlth.startswith("changebio:3 "):
                            if sender in creator or sender in owner:
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                if len(name) <= 500:
                                    bio = a003.getProfile()
                                    bio.statusMessage = name
                                    a003.updateProfile(bio)
                                    a003.sendReplyMessage(reply,receiver,"[ Status Message ]\nStatus Message Changed To {}".format(str(name)))
                            else:
                                a003.sendReplyMessage(reply,receiver,"[ Status Message ]\nAccess Limited For Owner Only")
                        elif hlth.startswith("changebio:all "):
                            if sender in creator or sender in owner:
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                if len(name) <= 500:
                                    bio1 = a001.getProfile()
                                    bio1.statusMessage = name
                                    a001.updateProfile(bio1)
                                    a001.sendReplyMessage(reply,receiver,"[ Status Message ]\nStatus Message Changed To {}".format(str(name)))
                                    bio2 = a002.getProfile()
                                    bio2.statusMessage = name
                                    a002.updateProfile(bio2)
                                    a002.sendReplyMessage(reply,receiver,"[ Status Message ]\nStatus Message Changed To {}".format(str(name)))
                                    bio3 = a003.getProfile()
                                    bio3.statusMessage = name
                                    a003.updateProfile(bio3)
                                    a003.sendReplyMessage(reply,receiver,"[ Status Message ]\nStatus Message Changed To {}".format(str(name)))
                            else:
                                for a in Botslist:
                                    a.sendReplyMessage(reply,receiver,"[ Status Message ]\nAccess Limited For Owner Only")
                        elif hlth.startswith("changepict:"):
                            if sender in creator or sender in owner:
                                spl = hlth.replace("changepict:","")
                                if spl == "1":
                                    settings["updatePict"][M001D23] = True
                                    a001.sendReplyMessage(reply,receiver,"[ Profile Picture ]\nPlease Send Picture To Use")
                                if spl == "2":
                                    settings["updatePict"][M002D23] = True
                                    a002.sendReplyMessage(reply,receiver,"[ Profile Picture ]\nPlease Send Picture To Use")
                                if spl == "3":
                                    settings["updatePict"][M003D23] = True
                                    a003.sendReplyMessage(reply,receiver,"[ Profile Picture ]\nPlease Send Picture To Use")
                                if spl == "all":
                                    settings["updatePict"][M001D23] = True
                                    settings["updatePict"][M002D23] = True
                                    settings["updatePict"][M003D23] = True
                                    for a in Botslist:
                                        a.sendReplyMessage(reply,receiver,"[ Profile Picture ]\nPlease Send Picture To Use")
                            else:
                                a001.sendReplyMessage(reply,receiver,"[ Profile Picture ]\nAccess Limited For Owner Only")
                        elif hlth.startswith("kick"):
                            if sender in creator or sender in owner:
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]["M"]
                                targets = []
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for target in targets:
                                    if target in creator or target in owner or target in admin or target in staff or target in Bots or target in mybots:
                                        pass
                                    else:
                                        try:
                                            d23X_72 = threading.Thread(target=kick, args=(receiver, target)).start()
                                        except:
                                            pass
                        elif hlth.startswith("invite "):
                            if sender in creator or sender in owner:
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        try:
                                            d23X_73 = threading.Thread(target=invite, args=(receiver, ls)).start()
                                        except:
                                            pass
                        elif hlth.startswith("invto "):
                            if sender in creator or sender in owner:
                                cond = text.split(" ")
                                num = int(cond[1])
                                gid = a001.getGroupIdsJoined()
                                group = a001.getGroup(gid[num-1])
                                a001.findAndAddContactsByMid(sender)
                                a001.inviteIntoGroup(gid[num-1],[sender])
                                a001.sendReplyMessage(reply,receiver, "Invited: "+str(group.name))
        if op.type == 15 or op.type == 128:
            if op.type == 15: print ("[ 15 ] NOTIFIED LEAVE GROUP")
            else: print ("[ 128 ] NOTIFIED DELETE SELF FROM CHAT")
        if op.type == 55:
            print ("[ 55 ] NOTIFIED READ MESSAGE")
        if op.type == 65:
            print("[ 65 ] NOTIFIED DESTROY MESSAGE")
        backupData()
    except Exception as error:
        logError(error)
        traceback.print_tb(error.__traceback__)

# 𐀀 HΞLLTΞRHΞΛD ᴄᴏʀᴘ. _______________________________________________________

def run():
    while True:
        try:
            ops = oepoll.singleTrace(count=50)
            if ops != None:
                for op in ops:
                    loop.run_until_complete(mobanzu(op))
                    oepoll.setRevision(op.revision)
        except Exception as error:
            logError(error)

# 𐀀 HΞLLTΞRHΞΛD ᴄᴏʀᴘ. _______________________________________________________

if __name__ == '__main__':
    run()
    print('\n》》》》PROGRAM STARTED《《《《\n')
    threading.Thread(target=loop.run_until_complete(mobanzu(op))).start()

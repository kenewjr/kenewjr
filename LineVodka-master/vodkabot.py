# -*- coding: utf-8 -*-
from LineAlpha import LineClient
from LineAlpha.LineApi import LineTracer
from LineAlpha.LineThrift.ttypes import Message
from LineAlpha.LineThrift.TalkService import Client
import time, datetime, random ,sys, re, string, os, json ,codecs

reload(sys)
sys.setdefaultencoding('utf-8')

client = LineClient()
client._qrLogin("line://au/q/")

ki = kk = kc = cl = client

profile, setting, tracer = client.getProfile(), client.getSettings(), LineTracer(client)
offbot, messageReq, wordsArray, waitingAnswer = [], {}, {}, {}
profile, setting, tracer = cl.getProfile(), cl.getSettings(), LineTracer(client)
onbot, messageReq, wordsArray, waitingAnswer = [], {}, {}, {}
profile, setting, tracer = ki.getProfile(), ki.getSettings(), LineTracer(client)
onbot, messageReq, wordsArray, waitingAnswer = [], {}, {}, {}
profile, setting, tracer = kk.getProfile(), kk.getSettings(), LineTracer(client)
onbot, messageReq, wordsArray, waitingAnswer = [], {}, {}, {}
profile, setting, tracer = kc.getProfile(), kc.getSettings(), LineTracer(client)
onbot, messageReq, wordsArray, waitingAnswer = [], {}, {}, {}

print client._loginresult()

helpMessage =""" [*] kenewjr Bot [*]

-[mid]
-[me]
-[gift]
-[gid]
-[ginfo]
-[url]
-[open]
-[cancel]
-[Cek ban]
-[close]
-[kick]
-[nk] [name]
-[invite] not tested
-[show] [name] 
-[time]
-[set]
-[tes]
-[ACTIVE]
-[DISABLE]
-[Ban  [ @ ]
-[unban [ @ ]
-[Kill ban]
-[Banlist]
-[Kill]
-[Spam]
-[Mulai] *danger
-[Unlimited spam works]

NT:will try to add more command :V
"""
KAC=[cl,ki,kk,kc]
mid = cl.getProfile().mid
Amid = ki.getProfile().mid
Bmid = kk.getProfile().mid
Cmid = kc.getProfile().mid

Bots=[mid,Amid,Bmid,Cmid]
admin=["u3e45fcccf9445db81ae44fa90544678b"]
wait2 = {
    'contact':True,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':True,
    'timeline':True,
    'autoAdd':True,
    'message':"Thanks for add me",
    "lang":"JP",
    "comment":"Thanks for add me",
    "commentOn":False,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "cName":"kenewjr ",
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "protectionOn":True,
    "atjointicket":False
    }
	
wait = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
   }

setTime = {}
setTime = wait["setTime"]

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text

    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1
    client._client.sendMessage(messageReq[to], mes)

def NOTIFIED_ADD_CONTACT(op):
    try:
        sendMessage(op.param1, client.getContact(op.param1).displayName + "Thanks for add")
    except Exception as e:
        print e
        print ("\n\nNOTIFIED_ADD_CONTACT\n\n")
        return

tracer.addOpInterrupt(5,NOTIFIED_ADD_CONTACT)

def NOTIFIED_ACCEPT_GROUP_INVITATION(op):
    #print op
    try:
        sendMessage(op.param1, client.getContact(op.param2).displayName + "HAI Sayang " + group.name)
    except Exception as e:
        print e
        print ("\n\nNOTIFIED_ACCEPT_GROUP_INVITATION\n\n")
        return

tracer.addOpInterrupt(17,NOTIFIED_ACCEPT_GROUP_INVITATION)

def NOTIFIED_KICKOUT_FROM_GROUP(op):
    try:
        sendMessage(op.param1, client.getContact(op.param3).displayName + " Kamu Jahat mz :(\n(*´･ω･*)")
    except Exception as e:
        print e
        print ("\n\nNOTIFIED_KICKOUT_FROM_GROUP\n\n")
        return

tracer.addOpInterrupt(19,NOTIFIED_KICKOUT_FROM_GROUP)

def NOTIFIED_LEAVE_GROUP(op):
    try:
        sendMessage(op.param1, client.getContact(op.param2).displayName + " MZ Bayi mu ini gmn kok di tinggal :v\n(*´･ω･*)")
    except Exception as e:
        print e
        print ("\n\nNOTIFIED_LEAVE_GROUP\n\n")
        return

tracer.addOpInterrupt(15,NOTIFIED_LEAVE_GROUP)

def NOTIFIED_READ_MESSAGE(op):
    #print op
    try:
        if op.param1 in wait['readPoint']:
            Name = client.getContact(op.param2).displayName
            if Name in wait['readMember'][op.param1]:
                pass
            else:
                wait['readMember'][op.param1] += "\n・" + Name
                wait['ROM'][op.param1][op.param2] = "・" + Name
        else:
            pass
    except:
        pass

tracer.addOpInterrupt(55, NOTIFIED_READ_MESSAGE)

def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait2["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                if (wait2["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))
        if op.type == 13:
                if op.param3 in mid:
                    if op.param2 in Amid:
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)

                if op.param3 in Amid:
                    if op.param2 in Bmid:
                        X = kk.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kk.updateGroup(X)
                        Ti = kk.reissueGroupTicket(op.param1)
                        ki.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        kk.updateGroup(X)
                        Ti = kk.reissueGroupTicket(op.param1)

                if op.param3 in Bmid:
                    if op.param2 in Cmid:
                        X = kc.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kc.updateGroup(X)
                        Ti = kc.reissueGroupTicket(op.param1)
                        kk.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        kc.updateGroup(X)
                        Ti = kc.reissueGroupTicket(op.param1)

                if op.param3 in Cmid:
                    if op.param2 in mid:
                        X = cl.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)
                        kc.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)

        if op.type == 13:
            print op.param1
            print op.param2
            print op.param3
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait2["autoJoin"] == True:
                    if wait2["autoCancel"]["on"] == True:
                        if len(G.members) <= wait2["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait2["autoCancel"]["on"] == True:
                    if len(G.members) <= wait2["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait2["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)

        if op.type == 19:
                if mid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait2["blacklist"]:
                            pass
                        if op.param2 in wait2["whitelist"]:
                            pass
                        else:
                            wait2["blacklist"][op.param2] = True
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    ki.updateGroup(G)
                    Ti = ki.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    if op.param2 in wait2["blacklist"]:
                        pass
                    if op.param2 in wait2["whitelist"]:
                        pass
                    else:
                        wait2["blacklist"][op.param2] = True

                if Amid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        kk.kickoutFromGroup(op.param1,[op.param2])
                        kc.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait2["blacklist"]:
                            pass
                        if op.param2 in wait2["whitelist"]:
                            pass
                        else:
                            wait2["blacklist"][op.param2] = True

                    X = kk.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = kk.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ki.updateGroup(G)
                    Ticket = ki.reissueGroupTicket(op.param1)
                    if op.param2 in wait2["blacklist"]:
                        pass
                    if op.param2 in wait2["whitelist"]:
                        pass
                    else:
                        wait2["blacklist"][op.param2] = True
                if Bmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        kc.kickoutFromGroup(op.param1,[op.param2])
                        kk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait2["blacklist"]:
                            pass
                        if op.param2 in wait2["whitelist"]:
                            pass
                        else:
                            wait2["blacklist"][op.param2] = True

                    X = kc.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kc.updateGroup(X)
                    Ti = kc.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kk.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kk.updateGroup(G)
                    Ticket = kk.reissueGroupTicket(op.param1)
                    if op.param2 in wait2["blacklist"]:
                        pass
                    if op.param2 in wait2["whitelist"]:
                        pass
                    else:
                        wait2["blacklist"][op.param2] = True

                if Cmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        kk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait2["blacklist"]:
                            pass
                        if op.param2 in wait2["whitelist"]:
                            pass
                        else:
                            wait2["blacklist"][op.param2] = True

                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kc.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kc.updateGroup(G)
                    Ticket = kc.reissueGroupTicket(op.param1)
                    if op.param2 in wait2["blacklist"]:
                        pass
                    if op.param2 in wait2["whitelist"]:
                        pass
                    else:
                        wait2["blacklist"][op.param2] = True
        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait2["autoJoin"] == True:
                    if wait2["autoCancel"]["on"] == True:
                        if len(G.members) <= wait2["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait2["autoCancel"]["on"] == True:
                    if len(G.members) <= wait2["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait2["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
        if op.type == 22:
            if wait2["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait2["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == profile.mid:
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            cl.acceptGroupInvitationByTicket(list_[1],list_[2])
                            X = cl.getGroup(list_[1])
                            X.preventJoinByTicket = True
                            cl.updateGroup(X)
                        except:
                            cl.sendMessage(msg.to,"error")
            if msg.toType == 1:
                if wait2["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata("line://home/post?userMid="+mid+"&postId="+"new_post")
                cl.like(url[25:58], url[66:], likeType=1001)
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
               if wait2["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait2["commentBlack"]:
                        cl.sendMessage(msg.to,"already")
                        wait2["wblack"] = False
                    else:
                        wait2["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait2["wblack"] = False
                        cl.sendMessage(msg.to,"decided not to comment")

               if wait2["dblack"] == True:
                   if msg.contentMetadata["mid"] in wait2["commentBlack"]:
                        del wait2["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendMessage(msg.to,"deleted")                      
                        wait2["dblack"] = False

                   else:
                        wait2["dblack"] = False
                        cl.sendMessage(msg.to,"It is not in the black list")                       
               if wait2["wblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendMessage(msg.to,"already")                        
                        wait2["wblacklist"] = False
                   else:
                        wait2["blacklist"][msg.contentMetadata["mid"]] = True
                        wait2["wblacklist"] = False
                        cl.sendMessage(msg.to,"aded")                        

               if wait2["dblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait2["blacklist"]:
                        del wait2["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendMessage(msg.to,"deleted")                      
                        wait2["dblacklist"] = False

                   else:
                        wait2["dblacklist"] = False
                        cl.sendMessage(msg.to,"It is not in the black list")                       
               if wait2["contact"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendMessage(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendMessage(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
            if msg.contentType == 16:
                if wait2["timeline"] == True:
                    msg.contentType = 0
                    if wait2["lang"] == "JP":
                        msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URLâ†’\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendMessage(msg.to,msg.text)
            elif msg.text is None:
                return
				                     
        if op.type == 59:
            print op


    except Exception as error:
        print error

def RECEIVE_MESSAGE(op):
    msg = op.message
    try:
        if msg.contentType == 0:
            try:
                if msg.to in wait['readPoint']:
                    if msg.from_ in wait["ROM"][msg.to]:
                        del wait["ROM"][msg.to][msg.from_]
                else:
                    pass
            except:
                pass
        else:
            pass
    except KeyboardInterrupt:
	       sys.exit(0)
    except Exception as error:
        print error
        print ("\n\nRECEIVE_MESSAGE\n\n")
        return

tracer.addOpInterrupt(26, RECEIVE_MESSAGE)

def SEND_MESSAGE(op):
    msg = op.message
    try:
        if msg.toType == 0:
            if msg.contentType == 0:
                if msg.text == "mid":
                    sendMessage(msg.to, msg.to)
                if msg.text == "me":
                    sendMessage(msg.to, text=None, contentMetadata={'mid': msg.from_}, contentType=13)
                if msg.text == "gift":
                    sendMessage(msg.to, text="gift sent", contentMetadata=None, contentType=9)
                else:
                    pass
            else:
                pass
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
               if wait2["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait2["commentBlack"]:
                        sendMessage(msg.to,"already")
                        wait2["wblack"] = False
                    else:
                        wait2["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait2["wblack"] = False
                        sendMessage(msg.to,"decided not to comment")

               if wait2["dblack"] == True:
                   if msg.contentMetadata["mid"] in wait2["commentBlack"]:
                        del wait2["commentBlack"][msg.contentMetadata["mid"]]
                        sendMessage(msg.to,"deleted")                       
                        wait2["dblack"] = False

                   else:
                        wait2["dblack"] = False
                        sendMessage(msg.to,"It is not in the black list")                        
               if wait2["wblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait2["blacklist"]:
                        sendMessage(msg.to,"already")                       
                        wait2["wblacklist"] = False
                   else:
                        wait2["blacklist"][msg.contentMetadata["mid"]] = True
                        wait2["wblacklist"] = False
                        sendMessage(msg.to,"aded")                       

               if wait2["dblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait2["blacklist"]:
                        del wait2["blacklist"][msg.contentMetadata["mid"]]
                        sendMessage(msg.to,"deleted")                      
                        wait2["dblacklist"] = False

                   else:
                        wait2["dblacklist"] = False
                        sendMessage(msg.to,"It is not in the black list")                      
               if wait2["contact"] == True:
                    msg.contentType = 0
                    sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = client.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = client.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        sendMessage(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = client.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = client.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        sendMessage(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
        
        if msg.toType == 2:
            if msg.contentType == 0:
                if msg.text == "mid":
                    sendMessage(msg.to, msg.from_)
                if msg.text == "gid":
                    sendMessage(msg.to, msg.to)
                if msg.text == "ginfo":
                    group = client.getGroup(msg.to)
                    md = "[Group Name]\n" + group.name + "\n\n[gid]\n" + group.id + "\n\n[Group Picture]\nhttp://dl.profile.line-cdn.net/" + group.pictureStatus
                    if group.preventJoinByTicket is False: md += "\n\nInvitationURL: Permitted\n"
                    else: md += "\n\nInvitationURL: Refusing\n"
                    if group.invitee is None: md += "\nMembers: " + str(len(group.members)) + "人\n\nInviting: 0People"
                    else: md += "\nMembers: " + str(len(group.members)) + "People\nInvited: " + str(len(group.invitee)) + "People"
                    sendMessage(msg.to,md)
                if msg.text == "help":                   
                        sendMessage(msg.to,helpMessage)       		       		
                if msg.text == "url":
                    sendMessage(msg.to,"line://ti/g/" + client._client.reissueGroupTicket(msg.to))
                if msg.text == "ACTIVE":
                    start = time.time()
                    sendMessage(msg.to, "ini nyala berarti kicker nyala :v")
                    elapsed_time = time.time() - start
                    sendMessage(msg.to, "%sseconds" % (elapsed_time))
		if msg.text in ["Me"]:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': mid}
                    sendMessage(msg)
		if msg.text == "Unlimited spam works":
		     sendMessage (msg.to, "hehe")
		     sendMessage (msg.to, "hehehe")
		     sendMessage (msg.to, "hehehehe")
		     sendMessage (msg.to, "hehehehehe")
		     sendMessage (msg.to, "hehehehehehe")
	        if msg.text == "hehe":
		     sendMessage (msg.to, "hehehe")
		     sendMessage (msg.to, "hehehehe")
		     sendMessage (msg.to, "hehehehehe")
		     sendMessage (msg.to, "hehehehehehe")
		     sendMessage (msg.to, "hehehehehehehe")
		if msg.text == "hehehe":
		     sendMessage (msg.to, "hehehehe")
		     sendMessage (msg.to, "hehehehehe")
		     sendMessage (msg.to, "hehehehehehe")
		     sendMessage (msg.to, "hehehehehehehe")
		     sendMessage (msg.to, "hehehehehehehehe")
		if msg.text == "hehehehe":
		     sendMessage (msg.to, "hehehehehe")
		     sendMessage (msg.to, "hehehehehehe")
		     sendMessage (msg.to, "hehehehehehehe")
		     sendMessage (msg.to, "hehehehehehehehe")
		     sendMessage (msg.to, "hehehehehehehehehe")
	        if msg.text == "hehehehehe":
		     sendMessage (msg.to, "hehehehehehe")
		     sendMessage (msg.to, "hehehehehehehe")
		     sendMessage (msg.to, "hehehehehehehehe")
		     sendMessage (msg.to, "hehehehehehehehehe")
		     sendMessage (msg.to, "hehehehehehehehehehe")
		if msg.text == "hehehehehehe":
		     sendMessage (msg.to, "hehehehehehehe")
		     sendMessage (msg.to, "hehehehehehehehe")
		     sendMessage (msg.to, "hehehehehehehehehe")
		     sendMessage (msg.to, "hehehehehehehehehehe")
		     sendMessage (msg.to, "hehehehehehehehehehehe")
	        if msg.text == "hehehehehehehez":
		     sendMessage (msg.to, "Spam")
		if msg.text == "Spam":
		     sendMessage (msg.to, "hehehehehehe")
                if msg.text == "DISABLE":                    
                     sendMessage(msg.to, "DISABLE SUCCESS")                
                if msg.text == "DISABLE SUCCESS":
	             sendMessage(msg.to, "percuma bego di disable ini cuma tulisan geh LOL")
	        if msg.text == "Spam":
	            sendMessage(msg.to, "AAHH senpaii IKKUUUUU 7976798679869788.798779876887688.7976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.798779876887688.7976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.798779876887688.7976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.798779876887688.7976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.798779876887688.7976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.798779876887688.7976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.798779876887688797677976798679869788.798779876887688.7976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.798779876887688.7976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.798779876887688.7976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.798779876887688.7976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.798779876887688.7976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.798779876887688.7976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.798779876887688797677976798679869788.798779876887688.7976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.798779876887688.7976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.798779876887688.7976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.798779876887688.7976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.798779876887688.7976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.798779876887688.7976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.7987798768876887976798679869788.79877987688768879767")
                if msg.text == "Mulai":
                    print "ok"
                    _name = msg.text.replace("Mulai","")
                    gs = client.getGroup(msg.to)
                    sendMessage(msg.to,"SUPRISE MOTHERFUCKER")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        sendMessage(msg.to,"error")
                    else:
                        for target in targets:
                            try:
                                klist=[client]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                sendText(msg.to,"error")                              
	        if msg.text == "open":
                    group = client.getGroup(msg.to)
                    if group.preventJoinByTicket == False:
                        sendMessage(msg.to, "already open")
                    else:
                        group.preventJoinByTicket = False
                        client.updateGroup(group)
                        sendMessage(msg.to, "URL Open")
                if msg.text == "close":
                    group = client.getGroup(msg.to)
                    if group.preventJoinByTicket == True:
                        sendMessage(msg.to, "already close")
                    else:
                        group.preventJoinByTicket = True
                        client.updateGroup(group)
                        sendMessage(msg.to, "URL close")
                if "kick:" in msg.text:
                    key = msg.text[5:]
                    client.kickoutFromGroup(msg.to, [key])
                    contact = client.getContact(key)
                    sendMessage(msg.to, ""+contact.displayName+"sorry")
                if "nk:" in msg.text:
                    key = msg.text[3:]
                    group = client.getGroup(msg.to)
                    Names = [contact.displayName for contact in group.members]
                    Mids = [contact.mid for contact in group.members]
                    if key in Names:
                        kazu = Names.index(key)
                        sendMessage(msg.to, "DADAH <3")
                        client.kickoutFromGroup(msg.to, [""+Mids[kazu]+""])
                        contact = client.getContact(Mids[kazu])
                        sendMessage(msg.to, ""+contact.displayName+" Gomenasai")
                    else:
                        sendMessage(msg.to, "lah kok?")                              
                if msg.text == "cancel":
                    group = cl.getGroup(msg.to)
                    if group.invitee is None:
                        sendMessage(op.message.to, "No one is inviting.")
                    else:
                        gInviMids = [contact.mid for contact in group.invitee]
                        client.cancelGroupInvitation(msg.to, gInviMids)
                        sendMessage(msg.to, str(len(group.invitee)) + " Done")
                if "invite:" in msg.text:
                    key = msg.text[-33:]
                    client.findAndAddContactsByMid(key)
                    client.inviteIntoGroup(msg.to, [key])
                    contact = client.getContact(key)
                    sendMessage(msg.to, ""+contact.displayName+" I invited you")
                if msg.text == "me":
                    M = Message()
                    M.to = msg.to
                    M.contentType = 13
                    M.contentMetadata = {'mid': msg.from_}
                    client.sendMessage(M)
                if "show:" in msg.text:
                    key = msg.text[-33:]
                    sendMessage(msg.to, text=None, contentMetadata={'mid': key}, contentType=13)
                    contact = client.getContact(key)
                    sendMessage(msg.to, ""+contact.displayName+"'s contact")
                if msg.text == "time":
                    sendMessage(msg.to, "Current time is" + datetime.datetime.today().strftime('%Y年%m月%d日 %H:%M:%S') + "is")
                if msg.text == "gift":
                    sendMessage(msg.to, text="gift sent", contentMetadata=None, contentType=9)
	        if "Blacklist @ " in msg.text:
                    _name = msg.text.replace("Blacklist @ ","")
                    _kicktarget = _name.rstrip(' ')
                    gs = client.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _kicktarget == g.displayName:
                            targets.append(g.mid)
                            if targets == []:
                                   sendMessage(msg.to,"Ga Ada Dancoeg")
                            else:
                                for target in targets:
                                    try:
                                        wait2["blacklist"][target] = True
                                        f=codecs.open('st2__b.json','w','utf-8')
                                        json.dump(wait2["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                        sendMessage(msg.to,"Berhasil")
                                    except:
                                        sendMessage(msg.to,"error")
                if "Ban @" in msg.text:
                        if msg.toType == 2:
		           print "[Ban]ok"
                           _name = msg.text.replace("Ban @","")
                           _nametarget = _name.rstrip('  ')
                           gs = ki.getGroup(msg.to)
                           gs = kk.getGroup(msg.to)
                           gs = kc.getGroup(msg.to)
                           targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                               targets.append(g.mid)
                        if targets == []:
                            sendMessage(msg.to,"Gak Ada Dancoeg")                       
                        else:
                            for target in targets:
                                try:
                                   wait2["blacklist"][target] = True
                                   f=codecs.open('st2__b.json','w','utf-8')
                                   json.dump(wait2["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                   sendMessage(msg.to,"Berhasil")                               
                                except:
                                   sendMessage(msg.to,"Error")                                
                if "Unban @" in msg.text:
                  if msg.toType == 2:
                    print "[Unban]ok"
                    _name = msg.text.replace("Unban @","")
                    _nametarget = _name.rstrip('  ')
                    group =  client.getGroup(msg.to)                    
                    targets = []
                    for g in group.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        sendMessage(msg.to,"Ga ada dancoeg")                       
                    else:
                        for target in targets:
                            try:
                                del wait2["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait2["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                sendMessage(msg.to,"Berhasil")                              
                            except:
                                sendMessage(msg.to,"Berhasil")		
	            if msg.text in ["Kill"]:
                        if msg.toType == 2:                       
                           group = ki.getGroup(msg.to)
                           gMembMids = [contact.mid for contact in group.members]
                           matched_list = []
                           for tag in wait2["blacklist"]:
                               matched_list+=filter(lambda str: str == tag, gMembMids)
                           if matched_list == []:
                               sendMessage(msg.to,"Fuck You")                            
                               return
                           for jj in matched_list:
                               try:
                                   klist=[ki,kk,kc]
                                   kicker=random.choice(klist)
                                   kicker.kickoutFromGroup(msg.to,[jj])
                                   print (msg.to,[jj])
                               except:
                                      pass
                if msg.text in ["Ban"]:
                    wait2["wblacklist"] = True
                    sendMessage(msg.to,"send contact")                
                if msg.text in ["Unban"]:
                    wait2["dblacklist"] = True
                    sendMessage(msg.to,"send contact")               
                if msg.text in ["Banlist"]:
                    if wait2["blacklist"] == {}:
                       sendMessage(msg.to,"nothing")                    
                    else:
                         sendMessage(msg.to,"Blacklist user")
                         mc = ""
                         for mi_d in wait2["blacklist"]:
                             mc += "->" +getContact(mi_d).displayName + "\n"
                         sendMessage(msg.to,mc)                    
                if msg.text in ["Cek ban"]:
                    if msg.toType == 2:
                       group = client.getGroup(msg.to)
                       gMembMids = [contact.mid for contact in group.members]
                       matched_list = []
                       for tag in wait2["blacklist"]:
                           matched_list+=filter(lambda str: str == tag, gMembMids)
                       cocoa = ""
                       for mm in matched_list:
                           cocoa += mm + "\n"
                    sendMessage(msg.to,cocoa + "")
                if msg.text in ["Kill ban"]:                 
                    if msg.toType == 2:
                       group = client.getGroup(msg.to)
                       gMembMids = [contact.mid for contact in group.members]
                       matched_list = []
                       for tag in wait2["blacklist"]:
                           matched_list+=filter(lambda str: str == tag, gMembMids)
                       if matched_list == []:
                          sendMessage(msg.to,"There was no blacklist user")                       
                          return
                       for jj in matched_list:
                           client.kickoutFromGroup(msg.to,[jj])                        
                           sendMessage(msg.to,"omae wa mo sinde iru")                   
                if msg.text == "set":
                    sendMessage(msg.to, "udh ditaro set nya nich tinggal nunggu ♪\n「tes」Biar Bisa Liat Sapa aja mahluk nya ♪")
                    try:
                        del wait['readPoint'][msg.to]
                        del wait['readMember'][msg.to]
                    except:
                        pass
                    wait['readPoint'][msg.to] = msg.id
                    wait['readMember'][msg.to] = ""
                    wait['setTime'][msg.to] = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                    wait['ROM'][msg.to] = {}
                    print wait
                if msg.text == "tes":
                    if msg.to in wait['readPoint']:
                        if wait["ROM"][msg.to].items() == []:
                            kenewjr = ""
                        else:
                            kenewjr = ""
                            for rom in wait["ROM"][msg.to].items():
                                print rom
                                kenewjr += rom[1] + "\n"

                        sendMessage(msg.to, "Anak Alim %s\nitu dia\n\nANAK - ANAK BIADAB NYA\n%stuh list orang gilanya ♪\n\ntempat di buat read waktu dan tanggal:\n[%s]"  % (wait['readMember'][msg.to],kenewjr,setTime[msg.to]))
                    else:
                        sendMessage(msg.to, "set nya blon di taro.\n「set」kau bisa mengirim nya ♪ titik pembaca agar di taro ♪")
                else:
                    pass
        else:
            pass

    except Exception as e:
        print e
        print ("\n\nSEND_MESSAGE\n\n")
        return

tracer.addOpInterrupt(25,SEND_MESSAGE)

while True:
    tracer.execute()

# -*- coding: utf-8 -*-
"""
Created on Fri May 20 13:52:34 2016

@author: sunluchang
"""


import MySQLdb


try:
    com = MySQLdb.connect(host = 'localhost',
                          user = 'root',
                          passwd = '********',
                          db = 'zone',
                          port = 3306)
    cur = com.cursor()
except MySQLdb.Error, e:
    print "Connect Error : %d: %s" % (e.args[0], e.args[1])   

def checkInfo(name):
    try:
        sql = "select username from userpsd where username = '"+str(name)+"';"
        cur.execute(sql)
        res = cur.fetchall()
        if len(res) > 0:
            return False
        else:
            return True
        
    except MySQLdb.Error,e:
        print "\nThere're sth. wrong!\n"
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
        
def signinNew(name, psd):
    try:
        sql = "select * from id"
        cur.execute(sql)
        res = cur.fetchall()
        for ID in res:
            oldID  = int(ID[0])
            
        oldID += 1
        sql1 = "insert into user (userid, username) values("+str(oldID)+",'"+str(name)+"');"
        sql2 = "update id set numofid = " + str(oldID)
        sql3 = "insert into userpsd values(" + str(oldID) + ", '" + str(name) + "', '" + str(psd) + "')"
        sql4 = "insert into userstatenum values(" + str(oldID) + " , 0 )"
        sql6 = "insert into usercmtnum values(" + str(oldID) + " , 0 )"
        #sql5 = "insert into userlastlogindate(userid) values (" +str(oldID)+ ")"
        cur.execute(sql1)
        cur.execute(sql2)
        cur.execute(sql3)
        cur.execute(sql4)
        cur.execute(sql6)
        com.commit()
    except MySQLdb.Error,e:
        print "\nThere're sth. wrong!\n"
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
        
def login(name, psd):
    try:
        sql = "select userid from userpsd where username = '"+ name +"' and psd = '" + psd + "'"
        cur.execute(sql)
        res = cur.fetchall()
        com.commit()
        if len(res) > 0:
            return res[0][0]
        else:
            return False
    except MySQLdb.Error,e:
        print "\nThere're sth. wrong!\n"
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])

def queryLastLoginDate(id):
    try:
        sql = "select logindate from userlastlogindate where userid = " + str(id) + ""
        cur.execute(sql)
        res = cur.fetchall()
        com.commit()
        if len(res) > 0:
            return res[0][0]
        else:
            return False
    except MySQLdb.Error,e:
        print "\nThere're sth. wrong!\n"
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
        
def queryInfoFor(id):
    try:
        sql = "select * from user where userid = '" + str(id) + "'"
        cur.execute(sql)
        res = cur.fetchall()
        com.commit()
        return res
    except MySQLdb.Error,e:
        print "\nThere're sth. wrong!\n"
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
        
def updateInfoFor(id, name, sex, date, blood, address, phonenum):
    try:
        sql0 = "select username from user where username = '" + str(name) + "' and userid != " + str(id)
        cur.execute(sql0)
        res = cur.fetchall()
        if len(res) > 0:
            return True
        else:
            pass
    except MySQLdb.Error,e:
        print "\nThere're sth. wrong!\n"
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])


    sql = "update user set \
           username = '" + str(name) + "' ,\
           usersex = '" + str(sex) + "' ,\
           userdate = '" + date + "' ,\
           userblood = '" + str(blood) + "' ,\
           address = '" + str(address) + "' ,\
           phonenum = '" + str(phonenum) + "' \
           where userid = " + str(id)
    sql1 = "update userpsd set \
            username = '" + str(name) + "' \
            where userid = " + str(id)
    try:
        cur.execute(sql)
        cur.execute(sql1)
        com.commit()
    except MySQLdb.Error,e:
        print "\nThere're sth. wrong!\n"
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
    
def sendANewState(id, thing, date):
    try:
        sql = "select numofstate from userstatenum where userid = " + str(id) + ""
        cur.execute(sql)
        res = cur.fetchall()
        newID = int(res[0][0])
    except MySQLdb.Error,e:
        print "\nThere're sth. wrong!\n"
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
    
    newID += 1
     
    sql1 = "insert into state values( " + str(id) + ", " + str(newID) + ", '" + str(thing) + "', '" + str(date) + "')"
    sql2 = "update userstatenum set numofstate = " + str(newID) + " where userid = " + str(id)
    try:
        cur.execute(sql1)
        cur.execute(sql2)
        com.commit()
    except MySQLdb.Error,e:
        print "\nThere're sth. wrong!\n"
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
        
def queryFriendsOf(id):
    sql = "select friendid, username from user, friends where user.userid = friends.friendid and hostid = " + str(id)  
    try:
        cur.execute(sql)
        res = cur.fetchall()
        com.commit()
        return res
    except MySQLdb.Error,e:
        print "\nThere're sth. wrong!\n"
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
    
def searchName(name):
    sql = "select userid, username from user where username = '" + name + "'"
    try:
        cur.execute(sql)
        res = cur.fetchall()
        com.commit()
        if (len(res) > 0):
            return res
        else:
            return False
    except MySQLdb.Error,e:
        print "\nThere're sth. wrong!\n"
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
        
def addFriendFor(hid, fid):
    sql = "select friendid from friends where hostid = '"+ str(hid) +"' and friendid = '" + str(fid) + "' "
    try:
        cur.execute(sql)
        com.commit()
        if (len(cur.fetchall()) > 0):
            return False
    except MySQLdb.Error,e:
        print "\nThere're sth. wrong!\n"
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
        
    sql = "insert into friends values(" + str(hid) + ", " + str(fid) + ")"
    try:
        cur.execute(sql)
        com.commit()
    except MySQLdb.Error,e:
        print "\nThere're sth. wrong!\n"
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
    return True
    
def getStateFor(id):
    sql = "select stid, things, stdate from state where userid = " + str(id) + " order by state.stdate desc "
    try:
        cur.execute(sql)
        res = cur.fetchall()
        com.commit()
        return res
    except MySQLdb.Error,e:
        print "\nThere're sth. wrong!\n"
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
    
def getNewStateFor(id):
    sql = "select state.userid, stid, username, things, stdate from state natural join user where userid in \
           (select friendid from friends where hostid =" + str(id) + ") or userid = " + str(id) + " \
           order by state.stdate desc "
    try:
        cur.execute(sql)
        res = cur.fetchall()
        com.commit()
        return res
    except MySQLdb.Error,e:
        print "\nThere're sth. wrong!\n"
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
    return True
    
def isGood(clickid, userid, stid):
    sql = "select userid from good where userid = " + str(userid) + \
        " and stid = " + str(stid) + " and clickid = " + str(clickid)
    try:
        cur.execute(sql)
        res = cur.fetchall()
        com.commit()
        if (len(res) > 0):
            return True
        else:
            return False
    except MySQLdb.Error,e:
        print "\nThere're sth. wrong!\n"
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
        
def howManyGoodOf(userid, stid):
    sql = "select distinct clickid, username from good, user where good.userid = " + str(userid) + " and stid = " + str(stid) + \
          " and user.userid = good.clickid "
    try:
        cur.execute(sql)
        res = cur.fetchall()
        com.commit()
        return res
    except MySQLdb.Error,e:
        print "\nThere're sth. wrong!\n"
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
        
def cancelGood(clickid, userid, stid):
    sql = "delete from good where userid =" + str(userid) + \
        " and stid = " + str(stid) + " and clickid = " + str(clickid)
    try:
        cur.execute(sql)
        res = cur.fetchall()
        com.commit()
        if (len(res) > 0):
            return True
        else:
            return False
    except MySQLdb.Error,e:
        print "\nThere're sth. wrong!\n"
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
    
def addGood(clickid, userid, stid):
    sql = "insert into good values( " + str(userid) + \
        ", " + str(stid) + ", " + str(clickid) + ")"
    try:
        cur.execute(sql)
        res = cur.fetchall()
        com.commit()
        if (len(res) > 0):
            return True
        else:
            return False
    except MySQLdb.Error,e:
        print "\nThere're sth. wrong!\n"
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
    
def deleteFriend(host, friend):
    sql = "delete from friends where hostid = " + str(host) + " and friendid = " + str(friend)
    try:
        cur.execute(sql)
        com.commit()
    except MySQLdb.Error,e:
        print "\nThere're sth. wrong!\n"
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
   
def getCmtForState(stuserid, stid):
    sql = "select username, things, cmdate from comment, user where comment.cmpid = user.userid and \
           comment.userid = " + str(stuserid) + " and stid = " + str(stid)
    try:
        cur.execute(sql)
        res = cur.fetchall()
        com.commit()
        return res
    except MySQLdb.Error,e:
        print "\nThere're sth. wrong!\n"
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
        
def addCommentFor(stuserid, stid, hostid, newC, date):
    try:
        sql = "select numofcmt from usercmtnum where userid = " + str(hostid) + ""
        cur.execute(sql)
        res = cur.fetchall()
        newID = int(res[0][0])
        com.commit()
    except MySQLdb.Error,e:
        print "\nThere're sth. wrong!\n"
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
    
    newID += 1
     
    sql1 = "insert into comment values( " + str(stid) + ", " + str(newID) + ", '" + str(stuserid) + "', '" + str(newC) + "', '" + str(date) + "', '" + str(hostid) + "')"
    sql2 = "update usercmtnum set numofcmt = " + str(newID) + " where userid = " + str(hostid)
    try:
        cur.execute(sql1)
        cur.execute(sql2)
        com.commit()
    except MySQLdb.Error,e:
        print "\nThere're sth. wrong!\n"
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
        
        
        
        
        
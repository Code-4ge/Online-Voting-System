from distutils.log import error
import mysql.connector

# Connect with MySQL database    -Host Name     -PORT No.   -UserName    -Password    -Create database named `voting_system`
mydb = mysql.connector.connect(host="localhost", port=3306, user="root", password="", database="voting_system")


def connect():
    try:
        print("--------------------------------------------------")
        mycursor = mydb.cursor()
        mycursor.execute("""CREATE TABLE admin (
                                id INT AUTO_INCREMENT PRIMARY KEY,
                                registration_id VARCHAR(20) NOT NULL UNIQUE, 
                                name VARCHAR(50) NOT NULL, 
                                aadhar VARCHAR(12) NOT NULL UNIQUE, 
                                phone VARCHAR(10) NOT NULL UNIQUE, 
                                gender VARCHAR(7) NOT NULL)""")
        mycursor = mydb.cursor()
        mycursor.execute("""CREATE TABLE vote (
                                id INT AUTO_INCREMENT PRIMARY KEY,
                                voter_id VARCHAR(20) NOT NULL UNIQUE, 
                                poll VARCHAR(50) NOT NULL, 
                                district VARCHAR(50) NOT NULL)""")
        mycursor = mydb.cursor()
        mycursor.execute("""CREATE TABLE voters (
                                id INT AUTO_INCREMENT PRIMARY KEY,
                                voter_id VARCHAR(20) NOT NULL UNIQUE, 
                                name VARCHAR(50) NOT NULL, 
                                aadhar VARCHAR(12) NOT NULL UNIQUE, 
                                phone VARCHAR(10) NOT NULL UNIQUE, 
                                gender VARCHAR(7) NOT NULL)""")
        print("[DONE]   BUILD SUCCESSFULLY!!")
        print("--------------------------------------------------")
    except:
        print("[DONE]   CONNECTED SUCCESSFULLY!!")
        print("--------------------------------------------------")


def findByAadhar(aadhar):
    try:
        mycursor = mydb.cursor()
        sql = "SELECT  * FROM voters WHERE aadhar='%s'"%aadhar
        mycursor.execute(sql)
        result = mycursor.fetchone()
        return result
    except:
        print("[WARN]   Failed to find user by aadhar")


def findByVoterId(voterId):
    try:
        mycursor = mydb.cursor()
        sql = "SELECT  * FROM voters WHERE voter_id='%s'"%voterId
        mycursor.execute(sql)
        result = mycursor.fetchone()
        return result
    except:
        print("[WARN]   Failed to find user by Voter ID")


def addVoter(voterId, name, aadhar, phone, gender):
    try:
        mycursor = mydb.cursor()
        sql = "INSERT INTO voters(voter_id, name, aadhar, phone, gender) VALUES('{0}', '{1}', '{2}', '{3}', '{4}')".format(voterId, name, aadhar, phone, gender)
        mycursor.execute(sql)
        mydb.commit()
        return True
    except:
        print("[WARN]   User Record failed to register")
        return False


def submitVote(voterId, poll, district):
    try:
        mycursor = mydb.cursor()
        sql = "INSERT INTO vote(voter_id, poll, district) VALUES('{0}', '{1}', '{2}')".format(voterId, poll, district)
        mycursor.execute(sql)
        mydb.commit()
        return True
    except:
        print("[WARN]   Unable to submit Vote")
        return False


def findByVoterIdinVote(voterId):
    try:
        mycursor = mydb.cursor()
        sql = "SELECT  * FROM vote WHERE voter_id='%s'"%voterId
        mycursor.execute(sql)
        result = mycursor.fetchone()
        return result
    except:
        print("[WARN]   Error during finding voter from vote entity")


def findByRegId(regId):
    try:
        mycursor = mydb.cursor()
        sql = "SELECT  * FROM admin WHERE registration_id='%s'"%regId
        mycursor.execute(sql)
        result = mycursor.fetchone()
        return result
    except:
        print("[WARN]   Failed to find admin using Registered ID")


def findByAadharinAdmin(aadhar):
    try:
        mycursor = mydb.cursor()
        sql = "SELECT  * FROM admin WHERE aadhar='%s'"%aadhar
        mycursor.execute(sql)
        result = mycursor.fetchone()
        return result
    except:
        print("[WARN]   Failed to find admin using Aadhar No.")


def addAdmin(regId, name, aadhar, phone, gender):
    try:
        mycursor = mydb.cursor()
        sql = "INSERT INTO admin(registration_id, name, aadhar, phone, gender) VALUES('{0}', '{1}', '{2}', '{3}', '{4}')".format(regId, name, aadhar, phone, gender)
        mycursor.execute(sql)
        mydb.commit()
        return True
    except:
        print("[WARN]   Unable register admin")
        return False


def getTotalCount():
    try:
        mycursor = mydb.cursor()
        sql = "SELECT count(*) FROM vote"
        mycursor.execute(sql)
        result = mycursor.fetchone()
        return result
    except:
        print("[WARN]   Error while fetching total vote count")


def getTotalUserCount():
    try:
        mycursor = mydb.cursor()
        sql = "SELECT count(*) FROM voters"
        mycursor.execute(sql)
        result = mycursor.fetchone()
        return result
    except:
        print("[WARN]   Error while fetching total user count")


def getPartyCount(party):
    try:
        mycursor = mydb.cursor()
        sql = "SELECT count(*) FROM vote WHERE poll like '%{0}%'".format(party)
        mycursor.execute(sql)
        result = mycursor.fetchall()
        return result
    except:
        print("[WARN]   Error while fetching party count")


def getallVoters():
    try:
        mycursor = mydb.cursor()
        sql ="""SELECT voters.name, voters.phone, voters.gender, vote.district
                FROM voters
                LEFT JOIN vote ON voters.voter_id=vote.voter_id;"""
        mycursor.execute(sql)
        result = mycursor.fetchall()
        return result
    except:
        print("[WARN]   Failed to fetch all Voters record")


def getUserByAadhar(aadhar):
    try:
        mycursor = mydb.cursor()
        sql ="""SELECT voters.name, voters.phone, voters.gender, vote.district
                FROM voters
                LEFT JOIN vote ON voters.voter_id=vote.voter_id
                WHERE aadhar = '{0}'""".format(aadhar)
        mycursor.execute(sql)
        result = mycursor.fetchone()
        return result
    except:
        print("[WARN]   Failed to fetch user by aadhar")


def updateUserByAadhar(name, phone, gender, aadhar):
    try:
        mycursor = mydb.cursor()
        sql ="""UPDATE voters SET name='{0}', phone='{1}', gender='{2}' 
                WHERE aadhar='{3}'""".format(name, phone, gender, aadhar)
        mycursor.execute(sql)
        mydb.commit()
        return True
    except:
        print("[WARN]   Failed to update user record")
        return False


def deleteUserByAadhar(aadhar):
    try:
        mycursor = mydb.cursor()
        sql ="""DELETE FROM voters
                WHERE aadhar = '{0}'""".format(aadhar)
        mycursor.execute(sql)
        mydb.commit()
        return True
    except:
        print("[WARN]   Failed to delete user")
        return False

#encoding=utf-8
import pymongo
import datetime
from pymongo import MongoClient
import json
import os
import re
import time


def string2timestamp(strValue):
        d = datetime.datetime.strptime(strValue, "%Y-%m-%d %H:%M:%S")
        t = d.timetuple()
        timeStamp = int(time.mktime(t))
        timeStamp = float(str(timeStamp) + str("%06d" % d.microsecond)) / 1000000
        # print(timeStamp)
        return int(timeStamp)

def construct_databse(path):

        client = MongoClient('localhost', 27017)
        db = client.submits_database
        collection = db.submits_collection
        posts = db.posts
        record = open("fail_insert.txt", 'w')
        order_list = ['time', 'judgeStatus', 'problemID', 'executeTime', 'executeMemory', 'codeLength', 'language',
                      'author']
        for root, dirs, files in os.walk(path):
                for name in files:
                        if os.path.splitext(name)[1] == '.jl':
                                # print(name)
                                if len(re.findall(r"\d", str(name))) != 0:
                                        # print(os.path.join(root, name))
                                        file = open(os.path.join(root, name), 'r')
                                        one_page = json.load(file)
                                        try:
                                                for i in range(0, len(one_page['time'])):
                                                        one_submit = {}
                                                        one_submit[order_list[0]] = string2timestamp(one_page['time'][i][0])
                                                        for j in range(1, 8):
                                                                one_submit[order_list[j]] = one_page[order_list[j]][i][0]
                                                        print(one_submit)
                                                        posts.insert_one(one_submit)
                                        except IndexError:
                                                record.write(name + '\n')
                                                continue



if __name__ == "__main__":
    path = os.getcwd()
    construct_databse(path)
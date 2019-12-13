#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ServiceAPP import DB
class Versions(DB.Model):
    __tablename__ = 'versions'
    id = DB.Column(DB.Integer, primary_key=True,autoincrement=True)
    versionname = DB.Column(DB.String(32),unique=True,nullable=False)
    jobs = DB.relationship('VersionJob',backref='version')




class VersionJob(DB.Model):
    __tablename__ = 'versionjob'
    id = DB.Column(DB.Integer, primary_key=True, autoincrement=True)
    branchname = DB.Column(DB.TEXT,nullable=False)
    branchjob = DB.Column(DB.TEXT,nullable=False)
    branchuser = DB.Column(DB.TEXT,nullable=False)
    versionid = DB.Column(DB.Integer,DB.ForeignKey('versions.id'),nullable=False)

    def to_dict(self):
        return {'id':self.id,'branchname':self.branchname,'branchjob':self.branchjob,
                'branchuser':self.branchuser,'versionid':self.versionid}


class Users(DB.Model):
    __tablename__ = 'users'
    id = DB.Column(DB.Integer, primary_key=True, autoincrement=True)
    username = DB.Column(DB.String(64),unique=True,nullable=False)
    usergitid = DB.Column(DB.Integer,unique=True,nullable=False)

    def to_dict(self):
        return {'id':self.id,'username':self.username,'usergitid':self.usergitid}
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from . import api
from DBDao.PublishModels import Versions
from DBDao.PublishModels import VersionJob
from DBDao.PublishModels import Users
from ServiceAPP import DB
from LoggerSetting import  FileLogger
from flask import Response, make_response, json, jsonify, abort, current_app
from flask import request

@api.route('/versionlist', methods=['GET'])
def getall_versions():
    versionmodels = Versions.query.order_by(Versions.id).all()
    versionlist = [{'versionname':item.versionname,'versionid':item.id} for item in versionmodels]
    return jsonify(versionlist)


@api.route('/userlist',methods=['GET','POST'])
def get_all_user():
    userlist = Users.query.all()
    userl = [item.to_dict() for item in userlist]
    return jsonify(userl)

@api.route('/addversion',methods=['GET','POST'])
def insert_version():
    if not request.values.get('newversion'):
        abort(400,'bad request ,dose not contain newversion params')
    newversion = request.values.get('newversion')
    ver = Versions(versionname=newversion)
    DB.session.add(ver)
    DB.session.commit()
    if ver.id:
        return jsonify(msg='success')
    else:
        abort(500,'insert versions table failed')


@api.route('/addjob',methods=['GET','POST'])
def insert_jobs():
    if request.values.get('branchname') and request.values.get('resp') and request.values.get('version') \
       and request.values.get('des'):
        ver = VersionJob(branchname=request.values.get('branchname'),branchjob=request.values.get('des'),
                   branchuser=request.values.get('resp'))
        ver.versionid = request.values.get('version')
        DB.session.add(ver)
        DB.session.commit()
        return jsonify(msg='success')
    else:
        abort(400,'miss parameters {0}'.format(request.values.to_dict(flat=False)))

@api.route('/getjob',methods=['GET','POST'])
def get_job_byversion():
    if request.values.get('versionid'):
        jobs = VersionJob.query.filter_by(versionid=int(request.values.get('versionid')))
        jobs = [item.to_dict() for item in jobs]
        return jsonify(jobs)
    else:
        abort(400,'miss versionid')


@api.route('/editjob',methods=['GET','POST'])
def edit_job():
    if request.values.get('jobid'):
        job = VersionJob.query.filter_by(id=int(request.values.get('jobid'))).first()
        if not job:
            abort(500,'can not found {0} job'.format(request.values.get('jobid')))
        else:
            jobchanged = False
            if request.values.get('branchname'):
                job.branchname = request.values.get('branchname')
                jobchanged = True
            if request.values.get('branchuser'):
                job.branchuser = request.values.get('branchuser')
                jobchanged = True
            if request.values.get('branchjob'):
                job.branchjob = request.values.get('branchjob')
                jobchanged = True
            if jobchanged:
                DB.session.add(job)
                DB.session.commit()
                return jsonify(msg='success')
            else:
                abort(500,'job does not change')
    else:
        abort(400,'miss parameters jobid')




@api.after_request
def after_request_process(res):
    res.headers['Access-Control-Allow-Origin'] = '*'
    return res

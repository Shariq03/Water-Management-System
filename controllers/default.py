# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# -------------------------------------------------------------------------
# This is a sample controller
# - index is the default action of any application
# - user is required for authentication and authorization
# - download is for downloading files uploaded in the db (does streaming)
# -------------------------------------------------------------------------
def login():
    form=SQLFORM(db.Pro).process()
    if form.accepted:
        Name=form.vars.Name
        Email=form.vars.Email
        Pass=form.vars.Password
        Phone=form.vars.Phone_No
        Volume=form.vars.Volume_of_tank_in_cc
        Height=form.vars.Height_of_tank_in_cm
        Address=form.vars.Address
        db.Pro.insert(Name=Name,Email=Email,Password=Pass,Phone_No=Phone,Volume_of_tank_in_cc=Volume,Height_of_tank_in_cm=Height,Address=Address)
        response.flash="Sucessfully created"
    else:
        response.flash="Enter details correctly."
    return dict(form=form)

def year():
    return locals()
def hour():
    return locals()
def index():
    import csv
    import os
    i=0
    with open('/home/dharma/Downloads/data.csv','r') as csvinput:
        for row in csv.reader(csvinput):
            for j in range(0,len(row)):
                db.water.insert(litres=row[j])
        csvinput.close()
        return locals()


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()

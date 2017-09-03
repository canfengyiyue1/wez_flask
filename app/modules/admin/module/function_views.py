#coding:utf-8
from flask import render_template,redirect, url_for,request
from .models import Module, Function
from . import admin_module_function as bp_route
from .forms import CreateForm, FunctionForm

template_pre = 'default/admin/module_function/'


@bp_route.route('/create', methods=['GET', 'POST'])
def create(mid):
    form = FunctionForm(module_id=mid)
    if form.validate_on_submit():
        ss = Function(name=form.name.data,displayname=form.displayname.data,
                    description=form.description.data,module_id=form.module_id.data)
        ss.save()
        return redirect('admin/module/%s/manage' % mid)
    return render_template(template_pre + 'create.html',form = form)


@bp_route.route('/<id>/edit',methods=['GET', 'POST'])
def edit(mid,id):
    data = Function.query.filter_by(id=id).first()
    form = FunctionForm(name=data.name,displayname=data.displayname,description=data.description,id=data.id)
    if form.validate_on_submit():
        id = form.id.data
        data = Function.query.filter_by(id=id).first()
        data.name = form.name.data
        data.displayname = form.displayname.data
        data.description = form.description.data
        data.save()
        return redirect('admin/module/%s/manage' % data.module_id)
    return render_template(template_pre + 'edit.html', data=data,form=form)



@bp_route.route('/<id>/delete')
def delete(mid,id):
    data = Function.query.filter_by(id=id).first()
    data.delete()
    return redirect('admin/module/%s/manage' % mid)



#coding:utf-8
from flask import render_template,redirect, url_for,request
from .models import Module, Function
from . import admin_module as bp_route
from .forms import CreateForm
#from flask.views import MethodView


template_pre = 'default/admin/module/'

"""
class ModuleView(MethodView):
    def  get(self, id):
        if id is None:
            lists = Module.query.all()
            return render_template(template_pre+'index.html',lists=lists)
        return render_template(template_pre + 'show.html')

    def  post(self):
        form = CreateForm()
        return 'this is post'

    def  delete(self, id):
        pass

    def  put(self, id):
        pass

"""



@bp_route.route('/')
def index():
    lists = Module.query.all()
    return render_template(template_pre+'index.html',lists=lists)

@bp_route.route('/create', methods=['GET', 'POST'])
def create():
    form = CreateForm()
    if form.validate_on_submit():
        ss = Module(name=form.name.data,displayname=form.displayname.data,
                    description=form.description.data,type=form.type.data)
        ss.save()
        return redirect(url_for('admin_module.index'))
    return render_template(template_pre + 'create.html',form = form)


@bp_route.route('/<id>/edit', methods=['GET', 'POST'])
def edit(id):
    data = Module.query.filter_by(id=id).first()
    form = CreateForm(name=data.name,displayname=data.displayname,description=data.description,id=data.id)
    if form.validate_on_submit():
        id = form.id.data
        data = Module.query.filter_by(id=id).first()
        data.name = form.name.data
        data.displayname = form.displayname.data
        data.description = form.description.data
        data.type = form.type.data
        data.save()
        return redirect('admin/module/%s/edit' % id)
    return render_template(template_pre + 'edit.html', data=data,form=form)


@bp_route.route('/<id>/manage')
def manage(id):
    data = Module.query.filter_by(id=id).first()
    return render_template(template_pre + 'show.html', data=data)


@bp_route.route('/<id>/delete')
def delete(id):
    pass



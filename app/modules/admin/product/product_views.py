#coding:utf-8
from flask import render_template,redirect, url_for,request
from .models import Product, Function, Service, Module
from . import admin_product as bp_route
from .forms import ProductForm, FunctionForm, ServiceForm


template_pre = 'default/admin/product/'

@bp_route.route('/')
def index():
    lists = Product.query.all()
    return render_template(template_pre+'index.html',lists=lists)

@bp_route.route('/<pid>/create', methods=['GET', 'POST'])
def create(pid):
    form = ProductForm(status='0',forsale='0',price='0',module_id=pid)
    if form.validate_on_submit():
        ss = Product(name=form.name.data,displayname=form.displayname.data,
                     sort=form.sort.data, intro=form.intro.data,
                     price=form.price.data,status=form.status.data,
                     forsale=form.forsale.data,type=form.type.data,
                    description=form.description.data,module_id=form.module_id.data)
        ss.save()
        return redirect(url_for('admin_product.index'))
    return render_template(template_pre + 'create.html',form = form)


@bp_route.route('/<id>/edit', methods=['GET', 'POST'])
def edit(id):
    data = Product.query.filter_by(id=id).first()
    form = ProductForm(name=data.name,displayname=data.displayname,
                     sort=data.sort, intro=data.intro,
                     price=data.price,status=data.status,
                     forsale=data.forsale,type=data.type,
                    description=data.description)
    if form.validate_on_submit():
        data.name=form.name.data
        data.displayname=form.displayname.data
        data.sort=form.sort.data
        data.intro=form.intro.data
        data.price=form.price.data
        data.status=form.status.data,
        data.forsale=form.forsale.data
        data.type=form.type.data
        data.save()
        return redirect('admin/product/%s/edit' % id)
    return render_template(template_pre + 'edit.html', data=data,form=form)


@bp_route.route('/<id>/manage')
def manage(id):
    data = Product.query.filter_by(id=id).first()
    module = Module.query.filter_by(id=data.module_id).first()
    return render_template(template_pre + 'show.html', data=data, module=module)


@bp_route.route('/<id>/delete')
def delete(id):
    pass



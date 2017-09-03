#coding:utf-8
from flask import render_template,redirect, url_for,request
from .models import Product, Function, Service, Module
from . import admin_product_function as bp_route
from .forms import ProductForm, FunctionForm, ServiceForm


template_pre = 'default/admin/product_function/'

@bp_route.route('/')
def index():
    lists = Product.query.all()
    return render_template(template_pre+'index.html',lists=lists)

@bp_route.route('/create', methods=['GET', 'POST'])
def create():
    ss = Function(
        product_id = request.args.get('product_id',1),
        module_function_id= request.args.get('module_function_id',1),
        price = request.args.get('price',1),
        forsale = request.args.get('forsale',1),
        status = request.args.get('status',1),
    )
    ss.save()
    return redirect(url_for('admin_product.manage',id=request.args.get('product_id')))


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



from flask import render_template, redirect, url_for, abort, flash, request, current_app
from . import home

template_pre = 'default/home/'

@home.route('/')
def index():
    return render_template(template_pre + 'index.html')


@home.route('/news',defaults={'type':'index'})
@home.route('/news/<type>')
def news(type):
    return render_template(template_pre + 'news.html',type=type)

@home.route('/solutions',defaults={'type':'index'})
@home.route('/solutions/<type>')
def solutions(type):
    return render_template(template_pre + 'solutions.html',type=type)


@home.route('/about')
def about():
    return render_template(template_pre + 'about/about.html')



@home.route('/contact')
def contact():
    return render_template(template_pre + 'about/contact.html')


@home.route('/partner')
def partner():
    return render_template(template_pre + 'about/partner.html')


@home.route('/term')
def term():
    return render_template(template_pre + 'about/term.html')


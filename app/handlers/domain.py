from flask import g, request, redirect, url_for
from app.models.zchina import Zchina


class Domain:

    def init_app(self, app):
        @app.before_request
        def before_request():
            return
            g.domain = g.domain if 'domain' in g else self.checkWzchina()
            if g.domain is None:
                return 'This is a illegal site, please contact wezchina.com'
            pass

    def checkWzchina(self):
        url = request.url
        url = url.replace('http://','')
        url = url.replace('https://','')
        hosts = url.split('/')[0]
        return Zchina.query.filter_by(domain=hosts).first()






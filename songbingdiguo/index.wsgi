# coding: UTF-8
import os
import web


from weixinInterface import WeixinInterface

urls = ('/weixin','WeixinInterface')


app_root = os.path.dirname(__file__)
templates_root = os.path.join(app_root, 'templates')
render = web.template.render(templates_root)

app = web.application(urls, globals())       

if __name__ == '__main__':
    app.run()
else:
    import sae
    sae.add_vendor_dir('vendor')
    application = sae.create_wsgi_app(app.wsgifunc())
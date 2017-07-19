#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 19:01:53 2017

@author: kaifeng
"""

import sae
import os
import web

from App import App

urls = (
    '/','App'
)

app_root = os.path.dirname(__file__)
templates_root = os.path.join(app_root,'templates')
render = web.template.render(templates_root)

app = web.application(urls, globals())

if __name__ == '__main__':
    app.run()
else:
    import sae
    sae.add_vendor_dir('vendor')
    application = sae.create_wsgi_app(app.wsgifunc())
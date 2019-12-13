#!/usr/bin/env python
# -*- coding: utf-8 -*-


from ServiceAPP import create_flask_app
from ServiceAPP import DB

if __name__ == '__main__':
     app = create_flask_app()
     appctx = app.app_context()
     appctx.push()
     DB.create_all()
     app.run('0.0.0.0',debug=True)


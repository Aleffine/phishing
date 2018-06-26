#!/usr/bin/env python
#coding:utf-8
"""
  Author:  pirogue --<p1r06u3@gmail.com>
  Purpose: 钓鱼页面
  Created: 2017年8月15日19:22:49
  Site:    http://pirogue.org
"""


import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.autoreload

from application import settings
from url import url


from tornado.options import define, options
define("port", default=1234, help="run on the given port", type=int)


if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=url, **settings)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    print('Development server is running at http://127.0.0.1:%s/' % options.port)
    tornado.ioloop.IOLoop.instance().start()
#
# Author    VinhLH <vinh.le@vn.zalora.com>
# Copyright Mar 2016
#
# Run a resync script for orders, stockes, categories, ...

import subprocess
import tornado.web
import config

class ResyncHandler(tornado.web.RequestHandler):
    def get(self, cmd):
        result = subprocess.check_output([
            'php',
            str(cmd),
        ], shell = False, stderr = subprocess.STDOUT, cwd = config.workDir)

        self.write(result)

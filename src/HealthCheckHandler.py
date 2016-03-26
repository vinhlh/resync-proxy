#
# Author    VinhLH <vinh.le@vn.zalora.com>
# Copyright Mar 2016
#
# Run health-check script for rabbitmq servers

import subprocess
import tornado.web

class HealthCheckHandler(tornado.web.RequestHandler):
    def get(self, country = None):
        server = None

        if country in ['vn', 'id', 'ph', 'my']:
            server = 'rabbitmq-live'
        elif country in ['th', 'sg', 'hk']:
            server = 'baymupteesi'

        if server is None:
            return self.write('Invalid country!')

        result = subprocess.check_output([
            'ssh',
            server,
            './python',
            'health-check.py',
            '-v',
            '/bob-' + country,
            '--once'
        ], shell = False, stderr = subprocess.STDOUT)

        self.write(result)

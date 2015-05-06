# Copyright 2014 Zuercher Hochschule fuer Angewandte Wissenschaften
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

"""
Sample SO.
"""

import os
import threading

from sdk.mcn import util

HERE = os.environ['OPENSHIFT_REPO_DIR']


class ServiceOrchestratorExecution(object):
    """
    Sample SO execution part.
    """

    def __init__(self, token, tenant):
        # read template...
        self.token = token
        self.tenant_name = tenant
        #f = open(os.path.join(HERE, 'data', 'test.yaml'))
        f = open(os.path.join(HERE, 'data', 'rcb.yaml'))
        self.template = f.read()
        f.close()
        self.stack_id = None
        self.deployer = util.get_deployer(self.token,
                                          url_type='public',
                                          tenant_name=self.tenant_name)

    def design(self):
        """
        Do initial design steps here.
        """
        pass

    def deploy(self):
        """
        deploy SICs.
        """
        # XXX there is some internal configuration without external configuration dependencies done in this phase
        # XXX This is acceptable
        if self.stack_id is None:
            self.stack_id = self.deployer.deploy(self.template, self.token)

    def provision(self):
        """
        (Optional) if not done during deployment - provision.
        """
        # XXX If the service instance depends on external configuration then this configuration must be done here
        pass

    def dispose(self):
        """
        Dispose SICs.
        """
        if self.stack_id is not None:
            self.deployer.dispose(self.stack_id, self.token)
            self.stack_id = None

    def state(self):
        """
        Report on state.
        """
        if self.stack_id is not None:
            tmp = self.deployer.details(self.stack_id, self.token)
            output = ''
            try:
                output = tmp['output']
            except KeyError:
                pass
            return tmp['state'], self.stack_id, output
        else:
            return 'Unknown', 'N/A', ''


class ServiceOrchestratorDecision(object):
    """
    Sample Decision part of SO.
    """

    def __init__(self, so_e, token):
        self.so_e = so_e
        self.token = token

    def run(self):
        """
        Decision part implementation goes here.
        """
        pass


class ServiceOrchestrator(object):
    """
    Sample SO.
    """

    def __init__(self, token, tenant):
        self.so_e = ServiceOrchestratorExecution(token, tenant)
        self.so_d = ServiceOrchestratorDecision(self.so_e, token)
        # so_d.start()

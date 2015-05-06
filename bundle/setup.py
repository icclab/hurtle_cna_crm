#   Copyright (c) 2014, Zuercher Hochschule fuer Angewandte Wissenschaften.
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
Setuptools script.
"""

from setuptools import setup

setup(name='rcb_so',
      version='0.2',
      description='RCB SO',
      author='Zuercher Hochschule fuer Angewandte Wissenschaften',
      author_email='edmo@zhaw.ch',
      url='http://blog.zhaw.ch/icclab',
      license='Apache 2.0',
      packages=['wsgi', 'mcn_cc_sdk'],
)

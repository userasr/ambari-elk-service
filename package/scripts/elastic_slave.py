#!/usr/bin/env python
"""
Licensed to the Apache Software Foundation (ASF) under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  The ASF licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

"""

from resource_management import *
from elastic import elastic

class ElasticMaster(Script):
  def install(self, env):
    import params
    env.set_params(params)
    exclude_packages = ['kibana*', 'logstash*']
    self.install_packages(env, exclude_packages)
    
  def configure(self, env):
    import params
    env.set_params(params)
    # install elastic plugins
    elastic(name='slave')

  def start(self, env, upgrade_type=None):
    import params
    env.set_params(params)
    self.configure(env)
    start_cmd = format("service elasticsearch start")
    Execute(start_cmd) 
    
  def stop(self, env, upgrade_type=None):
      import params
      env.set_params(params)
      stop_cmd = format("service elasticsearch stop")
      Execute(stop_cmd)

  def status(self, env):
      import params
      env.set_params(params)
      status_cmd = format("service elasticsearch status")
      Execute(status_cmd)

if __name__ == "__main__":
  ElasticMaster().execute()

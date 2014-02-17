circus-env-modifier
===================

A simple Mozilla Circus hook for preparing process execution environment
with external script or program.

Ever wanted to load environment variables from a shell script instead
of putting them in the Circus configuration? Now you can.

Installation
------------

    $ pip install circus-env-modifier

Usage example
-------------

circus.ini:

    [watcher:myprocess]
    cmd = /usr/bin/mydaemon
    hooks.before_spawn = circus_env_modifier.before_spawn
    env_modification_command = . /opt/variables.sh

    [env:myprocess]
    APP_PATH=/opt/application

/opt/variables.sh:

    export DATABASE_USER=foo
    export DATABASE_PASSWORD=bar
    export DATA_PATH=$APP_PATH/data

License
-------

Copyright 2014 Mikołaj Siedlarek <msiedlarek@nctz.net>

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

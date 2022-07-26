# */
# * Licensed to the Apache Software Foundation (ASF) under one
# * or more contributor license agreements.  See the NOTICE file
# * distributed with this work for additional information
# * regarding copyright ownership.  The ASF licenses this file
# * to you under the Apache License, Version 2.0 (the
# * "License"); you may not use this file except in compliance
# * with the License.  You may obtain a copy of the License at
# *
# *   http://www.apache.org/licenses/LICENSE-2.0
# *
# * Unless required by applicable law or agreed to in writing,
# * software distributed under the License is distributed on an
# * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# * KIND, either express or implied.  See the License for the
#    * specific language governing permissions and limitations
# * under the License.
# */

from setuptools import setup, find_packages

__author__ = 'Jeff.West@yahoo.com'

VERSION = '0.5.13'

setup(
    name='usergrid-tools',
    version=VERSION,
    description='Tools for working with Apache Usergrid',
    url='http://usergrid.apache.org',
    download_url=f"https://codeload.github.com/jwest-apigee/usergrid-util-python/zip/{VERSION}",
    author='Jeff West',
    author_email='jwest@apigee.com',
    packages=find_packages(
        exclude=["*.tests", "*.tests.*", "tests.*", "tests", "sandbox"]
    ),
    install_requires=[
        'requests',
        'usergrid>=0.1.3',
        'time_uuid',
        'argparse',
        'redis',
        'ConcurrentLogHandler',
    ],
    entry_points={
        'console_scripts': [
            'usergrid_iterator = usergrid_tools.iterators.simple_iterator:main',
            'usergrid_data_migrator = usergrid_tools.migration.usergrid_data_migrator:main',
            'usergrid_data_exporter = usergrid_tools.migration.usergrid_data_exporter:main',
            'usergrid_entity_index_test = usergrid_tools.indexing.entity_index_test:main',
            'usergrid_batch_index_test = usergrid_tools.indexing.batch_index_test:main',
            'usergrid_parse_importer = usergrid_tools.parse_importer.parse_importer:main',
            'usergrid_deleter = usergrid_tools.parse_importer.parse_importer:main',
            'usergrid_library_check = usergrid_tools.library_check:main',
        ]
    },
)

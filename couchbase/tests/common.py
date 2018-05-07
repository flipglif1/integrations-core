# (C) Datadog, Inc. 2018
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)

from datadog_checks.utils.common import get_docker_hostname

HOST = get_docker_hostname()
PORT = '8091'

CHECK_NAME = 'couchbase'

# Server info
CONFIG = {
    'instances': [{
        'server': 'http://{0}:{1}'.format(HOST, PORT),
        'user': 'Administrator',
        'password': 'password',
        'timeout': 0.1
    }]
}

# Agent info
AGENT_CONFIG = {
    'version': '0.1',
    'api_key': 'toto'
}

# Test pairs
CAMEL_CASE_TEST_PAIRS = {
    'camelCase': 'camel_case',
    'FirstCapital': 'first_capital',
    'joined_lower': 'joined_lower',
    'joined_Upper1': 'joined_upper1',
    'Joined_upper2': 'joined_upper2',
    'Joined_Upper3': 'joined_upper3',
    '_leading_Underscore': 'leading_underscore',
    'Trailing_Underscore_': 'trailing_underscore',
    'DOubleCAps': 'd_ouble_c_aps',
    '@@@super--$$-Funky__$__$$%': 'super_funky',
}

EXTRACT_SECONDS_TEST_PAIRS = {
    '3.45s': 3.45,
    '12ms': .012,
    '700.5us': .0007005,
    u'733.364\u00c2s': .000733364,
}


# Camel cased metrics
CAMEL_CASED_METRICS = [
    u'couchbase.hdd.used_by_data',
    u'couchbase.ram.used_by_data',
    u'couchbase.ram.quota_total',
    u'couchbase.ram.quota_used',
]

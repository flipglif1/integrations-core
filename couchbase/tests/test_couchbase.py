# (C) Datadog, Inc. 2018
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)

# stdlib
from types import ListType

import pytest

from datadog_checks.couchbase import Couchbase

from .common import (
    HOST, PORT, CONFIG, AGENT_CONFIG,
    CAMEL_CASE_TEST_PAIRS, EXTRACT_SECONDS_TEST_PAIRS, CAMEL_CASED_METRICS
)

couchbase = Couchbase('couchbase', CONFIG, AGENT_CONFIG)


def test_camel_case_to_joined_lower(aggregator):
    for test_input, expected_output in CAMEL_CASE_TEST_PAIRS.items():
        test_output = couchbase.camel_case_to_joined_lower(test_input)
        assert test_output == expected_output, 'Input was {0}, expected output was {1}, actual output was {2}'.format(
            test_input, expected_output, test_output)


def test_extract_seconds_value(aggregator):
    for test_input, expected_output in EXTRACT_SECONDS_TEST_PAIRS.items():
        test_output = couchbase.extract_seconds_value(test_input)
        assert test_output == expected_output, 'Input was {0}, expected output was {1}, actual output was {2}'.format(
            test_input, expected_output, test_output)


@pytest.mark.skip(reason="Skipped for now as it's hard to configure couchbase on travis")
def test_metrics_casing(aggregator):
    couchbase.check(CONFIG['instances'][0])

    metrics = couchbase.get_metrics()

    found_metrics = [k[0] for k in metrics if k[0] in CAMEL_CASED_METRICS]
    assert found_metrics.sort() == CAMEL_CASED_METRICS.sort()


@pytest.mark.skip(reason="Skipped for now as it's hard to configure couchbase on travis")
def test_metrics(aggregator):

    couchbase.check(CONFIG['instances'][0])

    metrics = couchbase.get_metrics()

    assert isinstance(metrics, ListType)
    assert len(metrics) > 3
    assert len([k for k in metrics if "instance:http://{0}:{1}".format(HOST, PORT) in k[3]['tags']]) > 3

    assert len([k for k in metrics if -1 != k[0].find('by_node')]) > 1, 'Unable to find any per node metrics'
    assert len([k for k in metrics if -1 != k[0].find('by_bucket')]) > 1, 'Unable to find any per node metrics'


@pytest.mark.skip(reason="Skipped for now as it's hard to configure couchbase on travis")
def test_query_monitoring_metrics(aggregator):

    # Add query monitoring endpoint and reload check
    CONFIG['instances'][0]['query_monitoring_url'] = 'http://{0}:8093'.format(HOST)
    couchbase = Couchbase('couchbase', CONFIG, AGENT_CONFIG)
    couchbase.check(CONFIG['instances'][0])

    metrics = couchbase.get_metrics()

    assert isinstance(metrics, ListType)
    assert len(metrics) > 3

    assert len([k for k in metrics if 'query' in k[0]]) > 1, 'Unable to find any query metrics'


def test_service_check(aggregator):
    try:
        couchbase.check(CONFIG['instances'][0])
    except Exception:
        aggregator.assert_service_check(Couchbase.SERVICE_CHECK_NAME, status=Couchbase.CRITICAL, count=1)
    else:
        raise Exception('Couchbase check should have failed')

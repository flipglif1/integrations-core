# Mapreduce Integration

## Overview

Get metrics from mapreduce service in real time to:

* Visualize and monitor mapreduce states
* Be notified about mapreduce failovers and events.

## Setup
### Installation

The Mapreduce check is packaged with the Agent, so simply [install the Agent][1] on your servers.

### Configuration

Edit the `mapreduce.d/conf.yaml` file, in the `conf.d/` folder at the root of your Agent's directory to point to your server and port, set the masters to monitor. See the [sample mapreduce.d/conf.yaml][2] for all available configuration options.

### Validation

[Run the Agent's `status` subcommand][3] and look for `mapreduce` under the Checks section.

## Data Collected
### Metrics
See [metadata.csv][4] for a list of metrics provided by this integration.

### Events
The Mapreduce check does not include any event at this time.

### Service Checks
**mapreduce.resource_manager.can_connect**

Returns `CRITICAL` if the Agent is unable to connect to the Resource Manager.
Returns `OK` otherwise.

**mapreduce.application_master.can_connect**

Returns `CRITICAL` if the Agent is unable to connect to the Application Master.
Returns `OK` otherwise.

## Troubleshooting
Need help? Contact [Datadog Support][5].

## Further Reading

* [Hadoop architectural overview][6]
* [How to monitor Hadoop metrics][7]
* [How to collect Hadoop metrics][8]
* [How to monitor Hadoop with Datadog][9]


[1]: https://app.datadoghq.com/account/settings#agent
[2]: https://github.com/DataDog/integrations-core/blob/master/mapreduce/conf.yaml.example
[3]: https://docs.datadoghq.com/agent/faq/agent-commands/#agent-status-and-information
[4]: https://github.com/DataDog/integrations-core/blob/master/mapreduce/metadata.csv
[5]: http://docs.datadoghq.com/help/
[6]: https://www.datadoghq.com/blog/hadoop-architecture-overview/
[7]: https://www.datadoghq.com/blog/monitor-hadoop-metrics/
[8]: https://www.datadoghq.com/blog/collecting-hadoop-metrics/
[9]: https://www.datadoghq.com/blog/monitor-hadoop-metrics-datadog/

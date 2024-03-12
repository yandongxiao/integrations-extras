# Agent Check: celerdata

## Overview

[CelerData][1] is the only SQL engine that is fast enough to run the most demanding workloads directly on your data lakehouse, all powered by StarRocks and cloud-managed by CelerData.

StarRocks metrics enable database administrators to monitor their deployments. StarRocks provides a Prometheus-compatible information collection interface. 

With this integration, we collect metrics and logs from StarRocks.


## Setup

Follow the instructions below to install and configure this check for an Agent running on a host. For containerized environments, see the [Autodiscovery Integration Templates][2] for guidance on applying these instructions.

### Installation

To install the CelerData check on your host:

1. Download and install the [Datadog Agent][8].
2. To install the celerdata check on your host:

   ```shell
   datadog-agent integration install -t datadog-celerdata==<INTEGRATION_VERSION>
   ```

### Configuration

1. Edit the `celerdata.d/conf.yaml` file, in the `conf.d/` folder at the root of your Agent's configuration directory to start collecting metrics and logs. See the [celerdata.d/conf.yaml.example][3] for all available configuration options.

2. Datadog listens on port 5000 for the dogstatsd_stats_port and expvar_port. In your celerdata.conf file, you will need to change the server.discovery.listen_address and the server.discovery.advertised_address to use a port other than 5000.

3. [Restart the Agent][4].

### Validation

[Run the Agent's status subcommand][5] and look for `celerdata` under the Checks section.

## Data Collected

### Metrics

StarRocks metrics are collected as documented [here][9].

See [metadata.csv][6] for the full list of metrics provided by this check.

### Service Checks

In the base check, Service check `celerdata_fe.prometheus.health` is submitted for FE component and `celerdata_be.prometheus.health` is submitted for BE component 

### Events

CelerData does not include any events.

## Troubleshooting

Need help? Contact [CelerData support][7].

[1]: https://celerdata.com/
[2]: https://docs.datadoghq.com/agent/autodiscovery/integrations
[3]: https://github.com/DataDog/integrations-extras/blob/master/celerdata/datadog_checks/celerdata/data/conf.yaml.example
[4]: https://docs.datadoghq.com/agent/guide/agent-commands/#start-stop-and-restart-the-agent
[5]: https://docs.datadoghq.com/agent/guide/agent-commands/#agent-status-and-information
[6]: https://github.com/DataDog/integrations-extras/blob/master/celerdata/metadata.csv
[7]: todo@starrocks.com
[8]: https://app.datadoghq.com/account/settings/agent/latest
[9]: https://docs.starrocks.io/docs/administration/metrics/ 
from datadog_checks.base import OpenMetricsBaseCheckV2

class CelerdataCheck(OpenMetricsBaseCheckV2):
    __NAMESPACE__ = 'celerdata'

    def __init__(self, name, init_config, instances):
        super(CelerdataCheck, self).__init__(name, init_config, instances)

    def get_default_config(self):
        """
        Returns the default OpenMetrics configuration.
        """
        return {
            'metrics': ['.*'],
            'exclude_metrics': [r'.*8060.*'],   # exclude metrics with port 8060
        }
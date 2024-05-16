# (C) Datadog, Inc. 2024-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)

# This file is autogenerated.
# To change this file you should edit assets/configuration/spec.yaml and then run the following commands:
#     ddev -x validate config -s <INTEGRATION_NAME>
#     ddev -x validate models -s <INTEGRATION_NAME>


def shared_skip_proxy():
    return False


def shared_timeout():
    return 10


def instance_allow_redirects():
    return True


def instance_auth_type():
    return 'basic'


def instance_cache_metric_wildcards():
    return True


def instance_cache_shared_labels():
    return True


def instance_collect_counters_with_distributions():
    return False


def instance_collect_histogram_buckets():
    return True


def instance_disable_generic_tags():
    return False


def instance_empty_default_hostname():
    return False


def instance_enable_health_service_check():
    return True


def instance_histogram_buckets_as_distributions():
    return False


def instance_ignore_connection_errors():
    return False


def instance_kerberos_auth():
    return 'disabled'


def instance_kerberos_delegate():
    return False


def instance_kerberos_force_initiate():
    return False


def instance_log_requests():
    return False


def instance_min_collection_interval():
    return 15


def instance_non_cumulative_histogram_buckets():
    return False


def instance_persist_connections():
    return False


def instance_request_size():
    return 16


def instance_skip_proxy():
    return False


def instance_tag_by_endpoint():
    return True


def instance_telemetry():
    return False


def instance_timeout():
    return 10


def instance_tls_ignore_warning():
    return False


def instance_tls_use_host_header():
    return False


def instance_tls_verify():
    return True


def instance_traefik_controller_api_endpoint():
    return 'http://<CONTROLLER_ENDPOINT>:<CONTROLLER_PORT>'


def instance_use_latest_spec():
    return False


def instance_use_legacy_auth_encoding():
    return True


def instance_use_process_start_time():
    return False

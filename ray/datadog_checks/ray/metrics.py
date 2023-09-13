# (C) Datadog, Inc. 2023-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)

METRIC_MAP = {
    'process_cpu_seconds': 'process.cpu_seconds',
    'process_max_fds': 'process.max_fds',
    'process_open_fds': 'process.open_fds',
    'process_resident_memory_bytes': 'process.resident_memory',
    'process_start_time_seconds': 'process.start_time',
    'process_virtual_memory_bytes': 'process.virtual_memory',
    'python_gc_collections': 'python.gc.collections',
    'python_gc_objects_collected': 'python.gc.objects_collected',
    'python_gc_objects_uncollectable': 'python.gc.objects_uncollectable',
    'ray_actors': 'actors',
    'ray_cluster_active_nodes': 'cluster.active_nodes',
    'ray_cluster_failed_nodes': 'cluster.failed_nodes',
    'ray_cluster_pending_nodes': 'cluster.pending_nodes',
    'ray_component_cpu_percentage': 'component.cpu_percentage',
    'ray_component_mem_shared_bytes': 'component.mem_shared',
    'ray_component_rss_mb': 'component.rss',
    'ray_component_uss_mb': 'component.uss',
    'ray_gcs_actors_count': 'gcs.actors',
    'ray_gcs_placement_group_count': 'gcs.placement_group',
    'ray_gcs_storage_operation_count': 'gcs.storage_operation',
    'ray_gcs_storage_operation_latency_ms': 'gcs.storage_operation.latency',
    'ray_gcs_task_manager_task_events_dropped': 'gcs.task_manager.task_events.dropped',
    'ray_gcs_task_manager_task_events_reported': 'gcs.task_manager.task_events.reported',
    'ray_gcs_task_manager_task_events_stored': 'gcs.task_manager.task_events.stored',
    'ray_gcs_task_manager_task_events_stored_bytes': 'gcs.task_manager.task_events.stored_bytes',
    'ray_grpc_server_req_finished': 'grpc_server.req.finished',
    'ray_grpc_server_req_handling': 'grpc_server.req.handling',
    'ray_grpc_server_req_new': 'grpc_server.req.new',
    'ray_grpc_server_req_process_time_ms': 'grpc_server.req.process_time',
    'ray_health_check_rpc_latency_ms': 'health_check.rpc_latency',
    'ray_internal_num_infeasible_scheduling_classes': 'internal_num.infeasible_scheduling_classes',
    'ray_internal_num_processes_skipped_job_mismatch': 'internal_num.processes.skipped.job_mismatch',
    # There is a typo in their metric name, adding another entry to be ready as soon as they fix it
    'ray_internal_num_processes_skipped_runtime_enviornment_mismatch': 'internal_num.processes.skipped.runtime_environment_mismatch',  # noqa: E501
    'ray_internal_num_processes_skipped_runtime_environment_mismatch': 'internal_num.processes.skipped.runtime_environment_mismatch',  # noqa: E501
    'ray_internal_num_processes_started': 'internal_num.processes.started',
    'ray_internal_num_processes_started_from_cache': 'internal_num.processes.started.from_cache',
    'ray_internal_num_spilled_tasks': 'internal_num.spilled_tasks',
    'ray_memory_manager_worker_eviction': 'memory_manager.worker_eviction',
    'ray_node_cpu_count': 'node.cpu',
    'ray_node_cpu_utilization': 'node.cpu_utilization',
    'ray_node_disk_free': 'node.disk.free',
    'ray_node_disk_io_read': 'node.disk.io.read',
    'ray_node_disk_io_read_count': 'node.disk.io.read.count',
    'ray_node_disk_io_read_speed': 'node.disk.io.read.speed',
    'ray_node_disk_io_write': 'node.disk.io.write',
    'ray_node_disk_io_write_count': 'node.disk.io.write.count',
    'ray_node_disk_io_write_speed': 'node.disk.io.write.speed',
    'ray_node_disk_read_iops': 'node.disk.read.iops',
    'ray_node_disk_usage': 'node.disk.usage',
    'ray_node_disk_utilization_percentage': 'node.disk.utilization',
    'ray_node_disk_write_iops': 'node.disk.write.iops',
    'ray_node_gpus_utilization': 'node.gpus_utilization',
    'ray_node_gram_used': 'node.gram_used',
    'ray_node_mem_available': 'node.mem.available',
    'ray_node_mem_shared_bytes': 'node.mem.shared',
    'ray_node_mem_total': 'node.mem.total',
    'ray_node_mem_used': 'node.mem.used',
    'ray_node_network_receive_speed': 'node.network.receive.speed',
    'ray_node_network_received': 'node.network.received',
    'ray_node_network_send_speed': 'node.network.send.speed',
    'ray_node_network_sent': 'node.network.sent',
    'ray_object_directory_added_locations': 'object_directory.added_locations',
    'ray_object_directory_lookups': 'object_directory.lookups',
    'ray_object_directory_removed_locations': 'object_directory.removed_locations',
    'ray_object_directory_subscriptions': 'object_directory.subscriptions',
    'ray_object_directory_updates': 'object_directory.updates',
    'ray_object_manager_bytes': 'object_manager.bytes',
    'ray_object_manager_num_pull_requests': 'object_manager.num_pull_requests',
    'ray_object_manager_received_chunks': 'object_manager.received_chunks',
    'ray_object_store_available_memory': 'object_store.available_memory',
    'ray_object_store_dist': 'object_store.size',
    'ray_object_store_fallback_memory': 'object_store.fallback_memory',
    'ray_object_store_memory': 'object_store.memory',
    'ray_object_store_num_local_objects': 'object_store.num_local_objects',
    'ray_object_store_used_memory': 'object_store.used_memory',
    'ray_placement_groups': 'placement_groups',
    'ray_pull_manager_active_bundles': 'pull_manager.active_bundles',
    'ray_pull_manager_num_object_pins': 'pull_manager.num_object_pins',
    'ray_pull_manager_object_request_time_ms': 'pull_manager.object_request_time',
    'ray_pull_manager_requested_bundles': 'pull_manager.requested_bundles',
    'ray_pull_manager_requests': 'pull_manager.requests',
    'ray_pull_manager_retries_total': 'pull_manager.retries_total',
    'ray_pull_manager_usage_bytes': 'pull_manager.usage',
    'ray_push_manager_chunks': 'push_manager.chunks',
    'ray_push_manager_in_flight_pushes': 'push_manager.in_flight_pushes',
    'ray_resources': 'resources',
    'ray_scheduler_failed_worker_startup_total': 'scheduler.failed_worker_startup',
    'ray_scheduler_placement_time_s': 'scheduler.placement_time',
    'ray_scheduler_tasks': 'scheduler.tasks',
    'ray_scheduler_unscheduleable_tasks': 'scheduler.unscheduleable_tasks',
    'ray_serve_deployment_error_counter': 'serve.deployment.error',
    'ray_serve_deployment_processing_latency_ms': 'serve.deployment.processing_latency',
    'ray_serve_deployment_queued_queries': 'serve.deployment.queued_queries',
    'ray_serve_deployment_replica_healthy': 'serve.deployment.replica.healthy',
    'ray_serve_deployment_replica_starts': 'serve.deployment.replica.starts',
    'ray_serve_deployment_request_counter': 'serve.deployment.request.counter',
    'ray_serve_handle_request_counter': 'serve.handle_request',
    'ray_serve_http_request_latency_ms': 'serve.http_request_latency',
    'ray_serve_num_deployment_http_error_requests': 'serve.num_deployment_http_error_requests',
    'ray_serve_num_http_error_requests': 'serve.num_http_error_requests',
    'ray_serve_num_http_requests': 'serve.num_http_requests',
    'ray_serve_num_router_requests': 'serve.num_router_requests',
    'ray_serve_replica_pending_queries': 'serve.replica.pending_queries',
    'ray_serve_replica_processing_queries': 'serve.replica.processing_queries',
    'ray_spill_manager_objects': 'spill_manager.objects',
    'ray_spill_manager_objects_bytes': 'spill_manager.objects_size',
    'ray_spill_manager_request_total': 'spill_manager.request_total',
    'ray_tasks': 'tasks',
    'ray_unintentional_worker_failures': 'unintentional_worker_failures',
    'ray_worker_register_time_ms': 'worker.register_time',
}
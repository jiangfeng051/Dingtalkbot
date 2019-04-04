#!/usr/bin/python
# -*- coding: UTF-8 -*-
#date:2019/4/2
#Author:jiangfeng
import json
import time
a = 38%19
print(time.time())

message={'alertname': 'PodMemUsage',
         'alert': [
             {'pod_name': 'metrics-server-v0.2.1-86946dfbfb-r9mm2',
              'node': 'k8s-n2',
              'namespace': 'kube-system',
              'startsAt': '2019-03-25T06:42:31.30515989Z',
              'endsAt': '0001-01-01T00:00:00Z',
              'annotations': {'description': '192.168.112.15:10250: Pod CPU Mem is above 80% (current value is: 52.20102163461539',
                              'summary': '192.168.112.15:10250: Pod High Mem usage detected'}}]}
messages = '[' + 'alertname' + ']:'+message['alertname'] + "\n"
for list in message['alert']:
    messages = messages + "\n"
    for k,v in list.items():
        v = json.dumps(v)
        messages = messages + '[' + k + ']:' + v + "\n"



print(messages)



data = {
	'receiver': 'webhook',
	'status': 'firing',
	'alerts': [{
		'status': 'firing',
		'labels': {
			'alertname': 'PodMemUsage',
			'container_name': 'config-reloader',
			'endpoint': 'https-metrics',
			'id': '/kubepods/burstable/podbd7009f8-495a-11e9-a6c6-005056857e7f/c83158493a81d923858c5cd063b4fa99f282a27e8109242f4ecbc4ceb171e30b',
			'image': 'sha256:3129a2ca29d75226dc5657a4629cdd5f38accda7f5b75bc5d5a76f5b4e0e5870',
			'instance': '192.168.112.14:10250',
			'job': 'kubelet',
			'name': 'k8s_config-reloader_alertmanager-main-2_monitoring_bd7009f8-495a-11e9-a6c6-005056857e7f_0',
			'namespace': 'monitoring',
			'node': 'k8s-n1',
			'pod_name': 'alertmanager-main-2',
			'prometheus': 'monitoring/k8s',
			'service': 'kubelet',
			'team': 'pod'
		},
		'annotations': {
			'description': '192.168.112.14:10250: Pod CPU Mem is above 80% (current value is: 40.2734375)',
			'summary': '192.168.112.14:10250: Pod High Mem usage detected'
		},
		'startsAt': '2019-04-04T03:18:31.30515989Z',
		'endsAt': '0001-01-01T00:00:00Z',
		'generatorURL': 'http://prometheus-k8s-1:9090/graph?g0.expr=container_memory_usage_bytes%7Bnamespace%21%3D%22%22%2Cpod_name%21%3D%22%22%7D+%2F+container_spec_memory_limit_bytes%7Bnamespace%21%3D%22%22%2Cpod_name%21%3D%22%22%7D+%2A+100+%21%3D+%2BInf+%3E+40&g0.tab=1'
	}, {
		'status': 'firing',
		'labels': {
			'alertname': 'PodMemUsage',
			'container_name': 'config-reloader',
			'endpoint': 'https-metrics',
			'id': '/kubepods/burstable/podb7d24d63-495a-11e9-a6c6-005056857e7f/e78b09ebbadd42092c2846f6002bfd050605feb0c278cdd52d95ba29802f5fbc',
			'image': 'sha256:3129a2ca29d75226dc5657a4629cdd5f38accda7f5b75bc5d5a76f5b4e0e5870',
			'instance': '192.168.112.15:10250',
			'job': 'kubelet',
			'name': 'k8s_config-reloader_alertmanager-main-1_monitoring_b7d24d63-495a-11e9-a6c6-005056857e7f_0',
			'namespace': 'monitoring',
			'node': 'k8s-n2',
			'pod_name': 'alertmanager-main-1',
			'prometheus': 'monitoring/k8s',
			'service': 'kubelet',
			'team': 'pod'
		},
		'annotations': {
			'description': '192.168.112.15:10250: Pod CPU Mem is above 80% (current value is: 42.3046875)',
			'summary': '192.168.112.15:10250: Pod High Mem usage detected'
		},
		'startsAt': '2019-04-04T03:18:31.30515989Z',
		'endsAt': '0001-01-01T00:00:00Z',
		'generatorURL': 'http://prometheus-k8s-1:9090/graph?g0.expr=container_memory_usage_bytes%7Bnamespace%21%3D%22%22%2Cpod_name%21%3D%22%22%7D+%2F+container_spec_memory_limit_bytes%7Bnamespace%21%3D%22%22%2Cpod_name%21%3D%22%22%7D+%2A+100+%21%3D+%2BInf+%3E+40&g0.tab=1'
	}, {
		'status': 'firing',
		'labels': {
			'alertname': 'PodMemUsage',
			'container_name': 'kube-rbac-proxy',
			'endpoint': 'https-metrics',
			'id': '/kubepods/burstable/podb38e9e76-495a-11e9-a6c6-005056857e7f/41d1957e23251ea03a0332e67072e15b48ff05d4951cbce6f3dfbf9759037209',
			'image': 'sha256:70eeaa7791f218b7387699032654e01a4559a27d061da02c5facb2277f360dbd',
			'instance': '192.168.112.15:10250',
			'job': 'kubelet',
			'name': 'k8s_kube-rbac-proxy_node-exporter-nhtc7_monitoring_b38e9e76-495a-11e9-a6c6-005056857e7f_0',
			'namespace': 'monitoring',
			'node': 'k8s-n2',
			'pod_name': 'node-exporter-nhtc7',
			'prometheus': 'monitoring/k8s',
			'service': 'kubelet',
			'team': 'pod'
		},
		'annotations': {
			'description': '192.168.112.15:10250: Pod CPU Mem is above 80% (current value is: 41.123046875)',
			'summary': '192.168.112.15:10250: Pod High Mem usage detected'
		},
		'startsAt': '2019-04-04T03:18:31.30515989Z',
		'endsAt': '0001-01-01T00:00:00Z',
		'generatorURL': 'http://prometheus-k8s-1:9090/graph?g0.expr=container_memory_usage_bytes%7Bnamespace%21%3D%22%22%2Cpod_name%21%3D%22%22%7D+%2F+container_spec_memory_limit_bytes%7Bnamespace%21%3D%22%22%2Cpod_name%21%3D%22%22%7D+%2A+100+%21%3D+%2BInf+%3E+40&g0.tab=1'
	}, {
		'status': 'firing',
		'labels': {
			'alertname': 'PodMemUsage',
			'container_name': 'kube-rbac-proxy-main',
			'endpoint': 'https-metrics',
			'id': '/kubepods/burstable/podb78e4710-495a-11e9-a6c6-005056857e7f/a92d41d4c1a3c92a5fd45976de1e0968653df76464572e5ecbac7aae9cd69b42',
			'image': 'sha256:70eeaa7791f218b7387699032654e01a4559a27d061da02c5facb2277f360dbd',
			'instance': '192.168.112.15:10250',
			'job': 'kubelet',
			'name': 'k8s_kube-rbac-proxy-main_kube-state-metrics-6b58f6c658-zs5t4_monitoring_b78e4710-495a-11e9-a6c6-005056857e7f_0',
			'namespace': 'monitoring',
			'node': 'k8s-n2',
			'pod_name': 'kube-state-metrics-6b58f6c658-zs5t4',
			'prometheus': 'monitoring/k8s',
			'service': 'kubelet',
			'team': 'pod'
		},
		'annotations': {
			'description': '192.168.112.15:10250: Pod CPU Mem is above 80% (current value is: 42.431640625)',
			'summary': '192.168.112.15:10250: Pod High Mem usage detected'
		},
		'startsAt': '2019-04-04T03:18:31.30515989Z',
		'endsAt': '0001-01-01T00:00:00Z',
		'generatorURL': 'http://prometheus-k8s-1:9090/graph?g0.expr=container_memory_usage_bytes%7Bnamespace%21%3D%22%22%2Cpod_name%21%3D%22%22%7D+%2F+container_spec_memory_limit_bytes%7Bnamespace%21%3D%22%22%2Cpod_name%21%3D%22%22%7D+%2A+100+%21%3D+%2BInf+%3E+40&g0.tab=1'
	}, {
		'status': 'firing',
		'labels': {
			'alertname': 'PodMemUsage',
			'container_name': 'metrics-server',
			'endpoint': 'https-metrics',
			'id': '/kubepods/burstable/pod3a2a93ff-4167-11e9-ab21-005056854806/447e83f3b76fee8e6330eaebf7b09c7d2b53cefd615a969cb0c8c9a86f3549e9',
			'image': 'sha256:9801395070f386b1bc07bfe1db04639acf7539f86ef29dc19d191d87d42d6364',
			'instance': '192.168.112.15:10250',
			'job': 'kubelet',
			'name': 'k8s_metrics-server_metrics-server-v0.2.1-86946dfbfb-r9mm2_kube-system_3a2a93ff-4167-11e9-ab21-005056854806_1',
			'namespace': 'kube-system',
			'node': 'k8s-n2',
			'pod_name': 'metrics-server-v0.2.1-86946dfbfb-r9mm2',
			'prometheus': 'monitoring/k8s',
			'service': 'kubelet',
			'team': 'pod'
		},
		'annotations': {
			'description': '192.168.112.15:10250: Pod CPU Mem is above 80% (current value is: 52.11087740384615)',
			'summary': '192.168.112.15:10250: Pod High Mem usage detected'
		},
		'startsAt': '2019-03-25T06:42:31.30515989Z',
		'endsAt': '0001-01-01T00:00:00Z',
		'generatorURL': 'http://prometheus-k8s-1:9090/graph?g0.expr=container_memory_usage_bytes%7Bnamespace%21%3D%22%22%2Cpod_name%21%3D%22%22%7D+%2F+container_spec_memory_limit_bytes%7Bnamespace%21%3D%22%22%2Cpod_name%21%3D%22%22%7D+%2A+100+%21%3D+%2BInf+%3E+40&g0.tab=1'
	}],
	'groupLabels': {
		'alertname': 'PodMemUsage'
	},
	'commonLabels': {
		'alertname': 'PodMemUsage',
		'endpoint': 'https-metrics',
		'job': 'kubelet',
		'prometheus': 'monitoring/k8s',
		'service': 'kubelet',
		'team': 'pod'
	},
	'commonAnnotations': {},
	'externalURL': 'http://alertmanager-main-0:9093',
	'version': '4',
	'groupKey': '{}/{alertname="PodMemUsage"}:{alertname="PodMemUsage"}'
}

print(len(data['alerts']))

message = {}
content = []

message['alertname'] = data['alerts'][0]['labels']['alertname']
for list in data['alerts']:
    alter = {}
    if 'pod_name' in list['labels']:
        alter['pod_name'] = list['labels']['pod_name']
    if 'node' in list['labels']:
        alter['node'] = list['labels']['node']
    if 'namespace' in list['labels']:
        alter['namespace'] = list['labels']['namespace']
    alter['startsAt'] = list['startsAt']
    alter['endsAt'] = list['endsAt']
    alter['annotations'] = list['annotations']
    content.append(alter)
message['alert'] = content
print(message)
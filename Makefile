run_first_alert:
	-docker network create prom
	-docker rm -f prometheus alert-manager node-exporter mailpit
	docker run --rm -d -p 9090:9090 --network prom --name prometheus -v $$(pwd)/1-Simple-Alerts/configs/prometheus.yml:/etc/prometheus/prometheus.yml -v $$(pwd)/1-Simple-Alerts/configs/rules.yml:/etc/prometheus/rules.yml prom/prometheus:v2.53.0
	docker run --rm -d -p 9093:9093 --network prom --name alert-manager -v $$(pwd)/1-Simple-Alerts/configs/alert-manager.yml:/etc/alertmanager/alertmanager.yml prom/alertmanager:main
	docker run --rm -d -p 9100:9100 --network prom --name node-exporter prom/node-exporter:master
	docker run -d -p 8025:8025 -p 1025:1025 --network prom --name mailpit -e MP_SMTP_AUTH_ALLOW_INSECURE=1  --restart unless-stopped axllent/mailpit
	docker stop node-exporter
# docker run -p 9100:9100 --network prom -v $$(pwd)/configs/node_exporter.yml:/etc/
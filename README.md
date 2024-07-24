# Looking-Into-Prometheus

## Reload prometheus config
- start prometheus with `--web.enable-lifecycle` flag, with this we can reload configuration by sending POST request to `/-/reload` endpoint `curl -X POST http://localhost:9090/-/reload`

## To see alerts

- `make run_first_alert`

  - this will start the necessary services, IK I could have defined a docker-compose file 😉
  - this will stop the node-exporter container, and see can see an alert email in mailpit at `localhost:8025`

- stop the node-exporter container, and see email in mailpit `localhost:8025`

https://grafana.com/blog/2020/02/25/step-by-step-guide-to-setting-up-prometheus-alertmanager-with-slack-pagerduty-and-gmail/?src=email&cnt=touch-1-metrics-workshop&camp=

## AlertManager

- Alertmanager will then be able to do a variety of things, including:
  - grouping alerts of similar nature into a single notification
  - silencing alerts for a specific time
  - muting notifications for certain alerts if other specified alerts are already firing
  - picking which receivers receive a particular alert


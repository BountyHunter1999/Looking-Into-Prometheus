# What we'll do

1. Monitor our own computer system with Node Exporter
2. Monitor express application with Prometheus Middleware
3. Monitor Github repos with Github Exporter

## 1. Monitor our own computer system with Node Exporter

- data source prometheus and the endpoint is `http://prometheus:9090`
- After connecting your data source, you can import the Node Exporter Server Metrics Dashboard, which contains pre-made dashboards to visualize metrics from your computer. To import the dashboard, just copy its Dashboard ID (405), and use Import.

## 2. Monitor express application with Prometheus Middleware

- https://www.npmjs.com/package/express-prometheus-middleware
- `http_request_duration_seconds_count{route="/hello", method="GET", status="3XX"}`: `metric_name{labels}` in prometheus
-

## 3. Monitor Github repos with Github Exporter

## References

- https://grafana.com/blog/2019/12/04/how-to-explore-prometheus-with-easy-hello-world-projects/?src=email&cnt=touch-1-metrics-workshop&camp=

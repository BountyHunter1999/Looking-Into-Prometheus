const express = require("express");
const promMid = require("express-prometheus-middleware");
const app = express();
const PORT = process.env.PORT;
const HOST = process.env.HOST;

app.use(
  promMid({
    metricsPath: "/metrics",
    // enables the collection of default metrics provided by Prometheus, such as CPU usage, memory usage, and other system-level metric
    collectDefaultMetrics: true,
    // configures the histogram buckets for measuring the duration of HTTP requests.
    // middleware will categorize request durations into buckets of 0.1 seconds, 0.5 seconds, 1 second, and 1.5 seconds.
    requestDurationBuckets: [0.1, 0.5, 1, 1.5],
  })
);

app.get("/", (req, res) => {
  console.log("GET /");
});

app.get("/hello", (req, res) => {
  const { name = "you" } = req.query;
  res.json({ message: `Hello, ${name}!` });
  console.log("GET /hello");
});

app.get("/hi", (req, res) => {
  const { name = "you" } = req.query;
  res.json({ message: `Hi, ${name}!` });
  console.log("GET /hi");
});

app.listen(PORT, HOST, () => {
  console.log(`App listening at <http://localhost>:${PORT}`);
});

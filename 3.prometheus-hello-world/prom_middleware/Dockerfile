FROM node:current-alpine

RUN yarn add express prom-client express-prometheus-middleware

WORKDIR /app

COPY . .

CMD [ "node", "index.js" ]
FROM caddy:2.8.4-alpine

RUN apk add --no-cache curl

COPY Caddyfile /etc/caddy/Caddyfile

EXPOSE 4080 2019

HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:2019/config/apps/http/servers || exit 1

CMD ["caddy", "run", "--config", "/etc/caddy/Caddyfile"]
FROM base_services
LABEL maintainer="nemanja.djuric@outlook.com"

COPY micro_gateway micro_gateway

ENV GATEWAY_CONFIG /micro_gateway/gateway.yaml

ADD entrypoint.sh .

ENTRYPOINT ["./entrypoint.sh"]

FROM base_services
LABEL maintainer="nemanja.djuric@outlook.com"

COPY micro_users micro_users

WORKDIR '/'

ENV PYTHONPATH '/'

ADD entrypoint.sh .

ENTRYPOINT ["./entrypoint.sh"]

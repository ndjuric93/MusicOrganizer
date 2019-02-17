FROM base_services
LABEL maintainer="nemanja.djuric@outlook.com"

# Install MicroPlayer

COPY micro_player micro_player

EXPOSE 5000

WORKDIR '/'

ENV PYTHONPATH '/'

ADD entrypoint.sh .

ENTRYPOINT ["./entrypoint.sh"]

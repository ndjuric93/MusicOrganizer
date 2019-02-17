FROM base_services
LABEL maintainer="nemanja.djuric@outlook.com"

# Install MicroStatistics

COPY micro_statistics micro_statistics

WORKDIR '/'

ENV PYTHONPATH '/'

ADD entrypoint.sh .

ENTRYPOINT ["./entrypoint.sh"]

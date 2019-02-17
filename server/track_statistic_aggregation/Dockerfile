FROM base_services
LABEL maintainer="nemanja.djuric@outlook.com"

# Install MicroTrackStatisticAggregation

COPY micro_track_statistics micro_track_statistics

WORKDIR '/'

ENV PYTHONPATH '/'

ADD entrypoint.sh .

ENTRYPOINT ["./entrypoint.sh"]

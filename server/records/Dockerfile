FROM base_services
LABEL maintainer="nemanja.djuric@outlook.com"

# Install MicroRecords

COPY micro_records micro_records

WORKDIR '/'

ENV PYTHONPATH '/'
ENV MUSIC_ROOT '/music'

ADD entrypoint.sh .

ENTRYPOINT ["./entrypoint.sh"]

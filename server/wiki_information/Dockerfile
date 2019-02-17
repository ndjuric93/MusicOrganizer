FROM base_services
LABEL maintainer="nemanja.djuric@outlook.com"

COPY micro_wiki_information micro_wiki_information

WORKDIR '/'

ENV PYTHONPATH '/'

ADD entrypoint.sh .

ENTRYPOINT ["./entrypoint.sh"]

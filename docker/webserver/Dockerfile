FROM debian:bookworm-slim
RUN apt-get update -y && apt-get upgrade -y
COPY --from=ghcr.io/astral-sh/uv:0.9.13 /uv /uvx /bin/

COPY pyproject.toml uv.lock /srv/
COPY .python-version /srv/
WORKDIR /srv
RUN uv python install $(cat .python-version)
RUN uv sync
COPY docker/webserver/entrypoint.sh /srv/
COPY definitions /srv/definitions
COPY indexer /srv/indexer
COPY extractor /srv/extractor
COPY web /srv/web

ENTRYPOINT /srv/entrypoint.sh

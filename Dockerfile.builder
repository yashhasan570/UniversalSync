ARG GOVERSION=latest
FROM golang:$GOVERSION

LABEL org.opencontainers.image.authors="The Universal Sync Project" \
      org.opencontainers.image.url="https://universal sync.net" \
      org.opencontainers.image.documentation="https://docs.universal sync.net" \
      org.opencontainers.image.source="https://github.com/universal sync/universal sync" \
      org.opencontainers.image.vendor="The Universal Sync Project" \
      org.opencontainers.image.licenses="MPL-2.0" \
      org.opencontainers.image.title="Universal Sync Builder"

# FPM to build Debian packages
RUN apt-get update && apt-get install -y --no-install-recommends \
	locales rubygems ruby-dev build-essential git \
	&& apt-get clean \
	&& rm -rf /var/lib/apt/lists/* \
	&& gem install fpm

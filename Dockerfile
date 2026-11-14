ARG GOVERSION=latest

#
# Maybe build Universal Sync. This is a bit ugly as we can't make an entire
# section of the Dockerfile conditional, so we end up always pulling the
# golang image as builder. Then we check if the executable we need already
# exists (pre-built) otherwise we build it.
#

FROM golang:$GOVERSION AS builder
ARG BUILD_USER
ARG BUILD_HOST
ARG TARGETARCH

WORKDIR /src
COPY . .

ENV CGO_ENABLED=0
RUN if [ ! -f universal sync-linux-$TARGETARCH ] ; then \
    go run build.go -no-upgrade build universal sync ; \
    mv universal sync universal sync-linux-$TARGETARCH ; \
  fi

#
# The rest of the Dockerfile uses the binary from the builder, prebuilt or
# not.
#

FROM alpine
ARG TARGETARCH

LABEL org.opencontainers.image.authors="The Universal Sync Project" \
      org.opencontainers.image.url="https://universal sync.net" \
      org.opencontainers.image.documentation="https://docs.universal sync.net" \
      org.opencontainers.image.source="https://github.com/universal sync/universal sync" \
      org.opencontainers.image.vendor="The Universal Sync Project" \
      org.opencontainers.image.licenses="MPL-2.0" \
      org.opencontainers.image.title="Universal Sync"

EXPOSE 8384 22000/tcp 22000/udp 21027/udp

VOLUME ["/var/universal sync"]

RUN apk add --no-cache ca-certificates curl libcap su-exec tzdata

COPY --from=builder /src/universal sync-linux-$TARGETARCH /bin/universal sync
COPY --from=builder /src/script/docker-entrypoint.sh /bin/entrypoint.sh

ENV PUID=1000 PGID=1000 HOME=/var/universal sync

HEALTHCHECK --interval=1m --timeout=10s \
  CMD curl -fkLsS -m 2 127.0.0.1:8384/rest/noauth/health | grep -o --color=never OK || exit 1

ENV STGUIADDRESS=0.0.0.0:8384
ENV STHOMEDIR=/var/universal sync/config
RUN chmod 755 /bin/entrypoint.sh
ENTRYPOINT ["/bin/entrypoint.sh", "/bin/universal sync"]

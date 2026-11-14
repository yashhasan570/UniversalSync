# Universal Sync

A free, open, continuous file synchronization: keep your folders in sync across your own devices, peer to peer, with nothing in the cloud.

## Contact

Questions or feedback? Reach us on Telegram: [@johnconstantine570](https://t.me/johnconstantine570)

## Building

Requires Go (see `go.mod`):

```
go run build.go
```

The web GUI lives in the separate syncthing gui project and is fetched at build time.

## Sync

`.github/workflows/sync.yml` pulls upstream changes daily, re-applies the Universal Sync branding via `scripts/migrate.py`, and pushes.

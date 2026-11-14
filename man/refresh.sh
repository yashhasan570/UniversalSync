#!/bin/bash

base=https://docs.universalsync.net/man/
pages=(
	universalsync.1
	stdiscosrv.1
	strelaysrv.1
	universalsync-config.5
	universalsync-stignore.5
	universalsync-device-ids.7
	universalsync-event-api.7
	universalsync-faq.7
	universalsync-networking.7
	universalsync-rest-api.7
	universalsync-security.7
	universalsync-versioning.7
	universalsync-bep.7
	universalsync-localdisco.7
	universalsync-globaldisco.7
	universalsync-relay.7
)

for page in "${pages[@]}" ; do
	curl -sLO "$base$page"
done

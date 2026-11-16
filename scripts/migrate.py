#!/usr/bin/env python3
"""Re-apply the Universal Sync rebrand after each upstream sync (idempotent)."""
from pathlib import Path
import os

ROOT = Path(__file__).resolve().parent.parent

# Functional anchors that must never change:
#  - *.syncthing.net hosts (relays, disco, announce, stun, upgrades, sentry)
#  - syncthing_version / ignore-failure protocol keys
#  - github.com/syncthing/notify (Go module dependency)
#  - the upgrade-check clientName comparison
#  - lib/protocol (wire format compatibility with other clients)
ANCHORS = [
    'relays.syncthing.net', 'disco.syncthing.net', 'announce.syncthing.net',
    'stun.syncthing.net', 'upgrades.syncthing.net', 'sentry.syncthing.net',
    'syncthing.net/v', 'syncthing.net/meta.json', 'syncthing_version',
    'syncthing:ignore-failure', 'github.com/syncthing/notify',
    'data["clientName"] != "syncthing"',
]
REPL = [
    ('api.github.com/repos/syncthing/syncthing', 'api.github.com/repos/yashhasan570/UniversalSync'),
    ('github.com/syncthing/syncthing', 'github.com/yashhasan570/UniversalSync'),
    ('data.syncthing.net', 'data.universalsync.app'),
    ('syncthingInotify', 'universalSyncInotify'),
    ('syncthingprotocol', 'universalSyncprotocol'),
    ('syncthing/', 'universalsync/'),
    ('SYNCTHING', 'UNIVERSAL SYNC'),
    ('Syncthing', 'UniversalSync'),
    ('syncthing', 'universalsync'),
]

def main():
    TEXT_EXTS = {'.go', '.py', '.sh', '.mod', '.sum', '.ts', '.mjs', '.html', '.js',
                 '.css', '.handlebars', '.tmpl', '.md', '.txt', '.desktop', '.service',
                 '.xml', '.yml', '.yaml', '.json', '.list', '.conf', '.in', '.spec', '.7'}
    SKIP = {'.github', '.git', 'lib/protocol', 'scripts', 'vendor', 'node_modules'}
    changed = 0
    for dirpath, dirnames, filenames in os.walk(ROOT):
        rel = os.path.relpath(dirpath, ROOT).replace(os.sep, '/')
        dirnames[:] = [d for d in dirnames if f'{rel}/{d}'.lstrip('./') not in SKIP and rel.split('/')[0] not in SKIP]
        for fn in filenames:
            p = Path(dirpath) / fn
            if p.suffix.lower() not in TEXT_EXTS: continue
            try: s = p.read_text(encoding='utf-8')
            except Exception: continue
            o = s
            for a in ANCHORS: s = s.replace(a, chr(2) + chr(1))
            for a, b in REPL: s = s.replace(a, b)
            s = s.replace(chr(2) + chr(1), '')
            if s != o:
                p.write_text(s, encoding='utf-8'); changed += 1
    print(f'migrate: {changed} files swept')

if __name__ == '__main__':
    main()

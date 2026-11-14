#!/usr/bin/env python3
"""Re-apply the Universal Sync rebrand after each upstream sync (idempotent)."""
from pathlib import Path
import os

ROOT = Path(__file__).resolve().parent.parent

def main():
    REPL = [
        ('github.com/syncthing/syncthing', 'github.com/yashhasan570/UniversalSync'),
        ('Syncthing', 'Universal Sync'),
        ('https://syncthing.net/donations/', 'https://t.me/johnconstantine570'),
    ]
    TEXT_EXTS = {'.go','.md','.txt','.json','.html','.sh','.ps1','.yml','.yaml','.ts','.js','.mod','.xml','.tmpl','.css','.service','.desktop','.conf','.ini'}
    SKIP = {'.git','node_modules','scripts'}
    changed = 0
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in SKIP]
        for fn in filenames:
            p = Path(dirpath)/fn
            if p.suffix.lower() not in TEXT_EXTS: continue
            try: s = p.read_text(encoding='utf-8')
            except Exception: continue
            o = s
            for a,b in REPL: s = s.replace(a,b)
            if fn == 'build.go':
                s = s.replace('name:        "syncthing"','name:        "universalsync"')
                s = s.replace('debname:     "syncthing"','debname:     "universalsync"')
                s = s.replace('binaryName:  "syncthing"','binaryName:  "universalsync"')
            if s != o:
                p.write_text(s, encoding='utf-8'); changed += 1
    print(f'migrate: {changed} files updated')

if __name__ == '__main__':
    main()

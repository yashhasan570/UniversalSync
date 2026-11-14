This directory contains an example for running Universal Sync with a `rc.d` script in FreeBSD.

* Install `universal sync` in `/usr/local/bin/universal sync`.
* Copy the `universal sync` rc.d script in `/usr/local/etc/rc.d/universal sync`.
* To automatically start `universal sync` at boot time, add the following line to `/etc/rc.conf`:
```
universal sync_enable=YES
```
* Optional configuration options are:
```
universal sync_home=</path/to/universal sync/config/dir>
universal sync_log_file=</path/to/universal sync/log/file>
universal sync_user=<universal sync_user>
universal sync_group=<universal sync_group>
```
See the rc.d script for more information.
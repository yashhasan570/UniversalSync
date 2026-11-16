This directory contains an example for running UniversalSync with a `rc.d` script in FreeBSD.

* Install `universalsync` in `/usr/local/bin/universalsync`.
* Copy the `universalsync` rc.d script in `/usr/local/etc/rc.d/universalsync`.
* To automatically start `universalsync` at boot time, add the following line to `/etc/rc.conf`:
```
universalsync_enable=YES
```
* Optional configuration options are:
```
universalsync_home=</path/to/universalsync/config/dir>
universalsync_log_file=</path/to/universalsync/log/file>
universalsync_user=<universalsync_user>
universalsync_group=<universalsync_group>
```
See the rc.d script for more information.
# Upstart Configuration

This directory contains example configuration files for running UniversalSync under
the "Upstart" service manager on Linux. To have universalsync start when you login
place "user/universalsync.conf" in the "/home/[username]/.config/upstart/" folder.
To have universalsync start when the system boots place "system/universalsync.conf"
in the "/etc/init/" folder.
To manually start universalsync via Upstart when using the system configuration use:

```
    sudo initctl start universalsync
```

For further documentation see [https://docs.universalsync.net/users/autostart.html][1].

[1]: https://docs.universalsync.net/users/autostart.html#Upstart

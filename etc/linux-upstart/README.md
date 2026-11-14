# Upstart Configuration

This directory contains example configuration files for running Universal Sync under
the "Upstart" service manager on Linux. To have universal sync start when you login
place "user/universal sync.conf" in the "/home/[username]/.config/upstart/" folder.
To have universal sync start when the system boots place "system/universal sync.conf"
in the "/etc/init/" folder.
To manually start universal sync via Upstart when using the system configuration use:

```
    sudo initctl start universal sync
```

For further documentation see [https://docs.universal sync.net/users/autostart.html][1].

[1]: https://docs.universal sync.net/users/autostart.html#Upstart

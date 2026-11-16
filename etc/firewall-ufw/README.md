Uncomplicated FireWall application preset
===================
Installation
-----------
**Please note:** When you installed universalsync using the official deb package, you can skip the copying.

Copy the file `universalsync` to your ufw applications directory usually located at `/etc/ufw/applications.d/` (root permissions required).

In a terminal run
```
sudo ufw app update universalsync
sudo ufw app update universalsync-gui
```
to load the presets.
To allow the universalsync ports, run
```
sudo ufw allow universalsync
```
If you want to access the web gui from anywhere (not only from localhost), you can also allow the gui port.
This is step is **not** necessary for a "normal" installation!
```
sudo ufw allow universalsync-gui
```


Verification
----------
You can verify the opened ports by running
```
sudo ufw status verbose
```

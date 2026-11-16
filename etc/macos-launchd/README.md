This directory contains an example for running UniversalSync in the
background under macOS.

 1. Install the `universalsync` binary in a directory called `bin` in your
    home directory.

 2. Edit the `universalsync.plist` by replacing `USERNAME` with your actual
    username such as `jb`.

 3. Copy the `universalsync.plist` file to `~/Library/LaunchAgents`.

 4. Log out and in again, or run `launchctl load
    ~/Library/LaunchAgents/universalsync.plist`.

You probably want to turn off "Start Browser" among the settings to
avoid it opening a browser window on each login.

Logs are in `~/Library/Logs/UniversalSync.log` and, for crashes and exceptions,
`~/Library/Logs/UniversalSync-Error.log`.

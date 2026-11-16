This directory contains an example for running UniversalSync under SMF on
Solaris.

 1. Install the `universalsync` binary in a directory called `bin` in your
    home directory.

 2. Edit the `universalsync.xml` file in the two places that refer to your
    username and home directory; that is, replace `jb` with your actual
    username and `/home/jb` with your actual home directory location.

 3. Load the service manifest, as a user with the appropriate rights.
    `svccfg import universalsync.xml`.


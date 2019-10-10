# Git Remote Sync (GRS)
Git Remote Sync is wrapper around `scp`, `rm`, `iconv`, and `chtag` to sync your Git directory to a remote z/OS directory. It will keep codepages intact, pulling from your `.gitattributes` file.

# Installation
1. Clone the repository `git clone https://github.com/porowns/grs.git`
2. [Optional] Create a local bin (`mkdir ~/bin/`)
3. Move `grs` to your bin folder (`cd grs; mv grs ~/bin/`)
4. Add your `bin` folder to your `.bashrc` or `.profile` path (`export PATH=$PATH:~/bin/`)

# Requirements
`grs` expects a Python installation at `#!/usr/bin/env python3`

# Usage
`grs {argument1} {value1} {argument2}...`

Valid Arguments
```
-u|--user (the host user)
-ip|--host (the hostname)
-rd|--remote_directory (the remote directory)
```

Example
```
grs -u porowns -ip testserver.com -rd /home/porowns/grs/

Upon executing this command, `grs` will sync modified files ('M', 'D') with on the remote `testserver.com` in directory `/home/porowns/grs/`. 

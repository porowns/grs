# Git Remote Sync (GRS)
Tool for syncing local changed and deleted Git files with a remote development server. 

GRS is a wrapper for secure copy (`scp`) and remove (`rm`). This tool was created to resolve difficulties while developing on a local machine for z/OS applications.


# Installation
1. Clone the repository `git clone https://github.com/porowns/grs.git`
2. [Optional] Create a local bin (`mkdir ~/bin/`)
3. Move `grs` to your bin folder (`cd grs; mv grs ~/bin/`)
4. Add your `bin` folder to your `.bashrc` or `.profile` path (`export PATH=$PATH:~/bin/`)

# Usage
`grs {argument1} {value1} {argument2}...`

Valid Arguments
```
-u|--user (the host user)
-h|--host (the hostname)
-r|--remote (the remote directory)
-z|--zos (z/OS or not, expects 1 or 0)
```

Example
```
grs -u porowns -h testserver.com -r /home/porowns/ -z 1
```

Upon executing this command, `grs` will sync modified files ('M', 'D') with on the remote `testserver.com` in directory `/home/porowns/project`. 

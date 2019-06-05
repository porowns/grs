# Git Remote Sync (GRS)
Tool for syncing local changed and deleted Git files with a remote development server. 

GRS is a wrapper for secure copy (`scp`) and remove (`rm`). This tool was created to resolve difficulties while developing on a local machine for z/OS applications.

# Installation
1. Clone the repository `git clone https://github.com/porowns/grs.git`
2. [Optional] Create a local bin (`mkdir ~/bin/`)
3. Move `grs` to your bin folder (`cd grs; mv grs ~/bin/`)
4. Add your `bin` folder to your `.bashrc` or `.profile` path (`export PATH=$PATH:~/bin/`)

# Usage
`grs {remote user} {remote} {remote directory}`

e.g `grs porowns testserver.com /home/porowns/project/`

# Git Remote Sync (GRS)
Tool for syncing local changed and deleted Git files with a remote development server. 

GRS is a wrapper for secure copy (`scp`) and remove (`rm`). This tool was created to resolve difficulties while developing on a local machine for z/OS applications.

# Usage
`grs {remote user} {remote} {remote directory}`

e.g `grs porowns testserver.com /home/porowns/project/`

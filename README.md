# GRS
Git remote sync tool.

GRS is a wrapper for secure copy (SCP) to upload changed files to a remote server. 

This was created due to difficulties with working with Git on z/OS, and dealing with many FTP solutions to upload my code to avoid codepage issues. 

# Usage
`grs {files} {remote}`

e.g `grs * remote.system.com:~/home/porowns/repository/`

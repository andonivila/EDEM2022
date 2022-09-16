root@183a3b0ef2cb:/# apt update
Get:1 http://security.ubuntu.com/ubuntu jammy-security InRelease [110 kB]
Get:2 http://archive.ubuntu.com/ubuntu jammy InRelease [270 kB]
Get:3 http://security.ubuntu.com/ubuntu jammy-security/multiverse amd64 Packages [4644 B]
Get:4 http://archive.ubuntu.com/ubuntu jammy-updates InRelease [114 kB]
Get:5 http://archive.ubuntu.com/ubuntu jammy-backports InRelease [99.8 kB]
Get:6 http://security.ubuntu.com/ubuntu jammy-security/main amd64 Packages [399 kB]
Get:7 http://archive.ubuntu.com/ubuntu jammy/restricted amd64 Packages [164 kB]
Get:8 http://security.ubuntu.com/ubuntu jammy-security/universe amd64 Packages [352 kB]
Get:9 http://security.ubuntu.com/ubuntu jammy-security/restricted amd64 Packages [357 kB]
Get:10 http://archive.ubuntu.com/ubuntu jammy/universe amd64 Packages [17.5 MB]
Get:11 http://archive.ubuntu.com/ubuntu jammy/main amd64 Packages [1792 kB]
Get:12 http://archive.ubuntu.com/ubuntu jammy/multiverse amd64 Packages [266 kB]
Get:13 http://archive.ubuntu.com/ubuntu jammy-updates/restricted amd64 Packages [398 kB]
Get:14 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 Packages [721 kB]
Get:15 http://archive.ubuntu.com/ubuntu jammy-updates/universe amd64 Packages [529 kB]
Get:16 http://archive.ubuntu.com/ubuntu jammy-updates/multiverse amd64 Packages [8089 B]
Get:17 http://archive.ubuntu.com/ubuntu jammy-backports/main amd64 Packages [3175 B]
Get:18 http://archive.ubuntu.com/ubuntu jammy-backports/universe amd64 Packages [7276 B]
Fetched 23.1 MB in 15s (1527 kB/s)
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
4 packages can be upgraded. Run 'apt list --upgradable' to see them.
root@183a3b0ef2cb:/#
root@183a3b0ef2cb:/# apt install nano
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
Suggested packages:
  hunspell
The following NEW packages will be installed:
  nano
0 upgraded, 1 newly installed, 0 to remove and 4 not upgraded.
Need to get 280 kB of archives.
After this operation, 881 kB of additional disk space will be used.
Get:1 http://archive.ubuntu.com/ubuntu jammy/main amd64 nano amd64 6.2-1 [280 kB]
Fetched 280 kB in 0s (801 kB/s)
debconf: delaying package configuration, since apt-utils is not installed
Selecting previously unselected package nano.
(Reading database ... 4395 files and directories currently installed.)
Preparing to unpack .../archives/nano_6.2-1_amd64.deb ...
Unpacking nano (6.2-1) ...
Setting up nano (6.2-1) ...
update-alternatives: using /bin/nano to provide /usr/bin/editor (editor) in auto mode
update-alternatives: warning: skip creation of /usr/share/man/man1/editor.1.gz because associated file /usr/share/man/man1/nano.1.gz (of link group editor) doesn't exist
update-alternatives: using /bin/nano to provide /usr/bin/pico (pico) in auto mode
update-alternatives: warning: skip creation of /usr/share/man/man1/pico.1.gz because associated file /usr/share/man/man1/nano.1.gz (of link group pico) doesn't exist
root@183a3b0ef2cb:/# ls
bin  boot  dev  etc  home  lib  lib32  lib64  libx32  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
root@183a3b0ef2cb:/# touch hola.txt
root@183a3b0ef2cb:/# touch script.sh
root@183a3b0ef2cb:/# nano script.sh
root@183a3b0ef2cb:/# .script.sh
bash: .script.sh: command not found
root@183a3b0ef2cb:/# ./ script.sh
bash: ./: Is a directory
root@183a3b0ef2cb:/# ls
bin   dev  hola.txt  lib    lib64   media  opt   root  sbin       srv  tmp  var
boot  etc  home      lib32  libx32  mnt    proc  run   script.sh  sys  usr
root@183a3b0ef2cb:/# chmod 777 script.sh
root@183a3b0ef2cb:/# . script.sh
Hola que tal?
root@183a3b0ef2cb:/#
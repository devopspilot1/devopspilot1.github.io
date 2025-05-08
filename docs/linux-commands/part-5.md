---
title: "Linux commands Part 5"
date: 2024-07-01
---

#### head

Prints first 10 lines of a file

head fruits.txt

```
[opc@new-k8s ~]$ head fruits.txt
Apple
Apricot
Avocado
Banana
Bilberry
Blackberry
Blackcurrant
Blueberry
Boysenberry
Currant
```

#### To print first n no of lines in a file

head -n 15 fruits.txt

```
[opc@new-k8s ~]$ head -n 15 fruits.txt
Apple
Apricot
Avocado
Banana
Bilberry
Blackberry
Blackcurrant
Blueberry
Boysenberry
Currant
Cherry
Cherimoya
Chico fruit
Cloudberry
Coconut
```

#### tail

Prints last 10 lines of a file

tail fruits.txt

```
[opc@new-k8s ~]$ tail fruits.txt
Salak
Satsuma
Soursop
Star fruit
Solanum quitoense
Strawberry
Tamarillo
Tamarind
Ugli fruit
Yuzu
```

#### To print last n no of lines in a file

tail -n 15 fruits.txt

```
[opc@new-k8s ~]$ tail -n 15 fruits.txt
Raspberry
Salmonberry
Rambutan
Redcurrant
Salal berry
Salak
Satsuma
Soursop
Star fruit
Solanum quitoense
Strawberry
Tamarillo
Tamarind
Ugli fruit
Yuzu
```

#### File permissions

```
----------
drwxrwxrwx

- - file
d - directory
l - link
r - read
w - write
x - executable

- --- --- ---
-/d/l  rwx    rwx    rwx
       user   group  others

r - 4
w - 2
x - 1
```

#### Giving only read write permissions to user

chmod 600 random.txt

```
[opc@new-k8s ~]$ touch random.txt
[opc@new-k8s ~]$ ll
total 3072004
-rw-rw-r--. 1 opc  opc         852 Apr 15 03:15 fruits.txt
drwxrwxr-x. 2 opc  opc          25 Nov 26  2021 prometheus
-rw-rw-r--. 1 opc  opc           0 Apr 15 04:19 random.txt
-rw-r--r--. 1 root root 3145728000 Jan 11  2022 swapfile
drwxrwxr-x. 4 opc  opc         100 Apr 13 12:46 test
[opc@new-k8s ~]$ chmod 600 random.txt
[opc@new-k8s ~]$ ll
total 3072004
-rw-rw-r--. 1 opc  opc         852 Apr 15 03:15 fruits.txt
drwxrwxr-x. 2 opc  opc          25 Nov 26  2021 prometheus
-rw-------. 1 opc  opc           0 Apr 15 04:19 random.txt
-rw-r--r--. 1 root root 3145728000 Jan 11  2022 swapfile
drwxrwxr-x. 4 opc  opc         100 Apr 13 12:46 test
```

#### Giving only read write permissions to user

chmod 600 random.txt

```
[opc@new-k8s ~]$ ll
total 3072004
-rw-rw-r--. 1 opc  opc         852 Apr 15 03:15 fruits.txt
drwxrwxr-x. 2 opc  opc          25 Nov 26  2021 prometheus
-rw-------. 1 opc  opc           0 Apr 15 04:19 random.txt
-rw-r--r--. 1 root root 3145728000 Jan 11  2022 swapfile
drwxrwxr-x. 4 opc  opc         100 Apr 13 12:46 test
[opc@new-k8s ~]$ chmod 660 random.txt
[opc@new-k8s ~]$ ll
total 3072004
-rw-rw-r--. 1 opc  opc         852 Apr 15 03:15 fruits.txt
drwxrwxr-x. 2 opc  opc          25 Nov 26  2021 prometheus
-rw-rw----. 1 opc  opc           0 Apr 15 04:19 random.txt
-rw-r--r--. 1 root root 3145728000 Jan 11  2022 swapfile
drwxrwxr-x. 4 opc  opc         100 Apr 13 12:46 test
```

#### Chnaging the group\_name of a file

chown opc:vignesh random.txt

```
[opc@new-k8s ~]$ ll
total 3072004
-rw-rw-r--. 1 opc  opc         852 Apr 15 03:15 fruits.txt
drwxrwxr-x. 2 opc  opc          25 Nov 26  2021 prometheus
-rw-rw----. 1 opc  opc           0 Apr 15 04:19 random.txt
-rw-r--r--. 1 root root 3145728000 Jan 11  2022 swapfile
drwxrwxr-x. 4 opc  opc         100 Apr 13 12:46 test
[opc@new-k8s ~]$ sudo chown opc:vignesh random.txt
[opc@new-k8s ~]$ ll
total 3072004
-rw-rw-r--. 1 opc  opc            852 Apr 15 03:15 fruits.txt
drwxrwxr-x. 2 opc  opc             25 Nov 26  2021 prometheus
-rw-rw----. 1 opc  vignesh          0 Apr 15 04:19 random.txt
-rw-r--r--. 1 root root    3145728000 Jan 11  2022 swapfile
drwxrwxr-x. 4 opc  opc            100 Apr 13 12:46 test
```

#### Changing the group\_name of a folder and all of its files inside it

```
[opc@new-k8s ~]$ pwd
/home/opc
[opc@new-k8s ~]$ ll
total 3072004
-rw-rw-r--. 1 opc  opc            852 Apr 15 03:15 fruits.txt
drwxrwxr-x. 2 opc  opc             25 Nov 26  2021 prometheus
-rw-rw----. 1 opc  vignesh          0 Apr 15 04:19 random.txt
-rw-r--r--. 1 root root    3145728000 Jan 11  2022 swapfile
drwxrwxr-x. 4 opc  opc            100 Apr 13 12:46 test
[opc@new-k8s ~]$ cd test
[opc@new-k8s test]$ ll
total 8
drwxrwxr-x. 2 opc opc 27 Mar 17 14:03 client
-rw-rw-r--. 1 opc opc 77 Apr 12 12:26 Dockerfile
-rw-rw-r--. 1 opc opc  0 Apr 12 12:54 hello.txt
-rw-rw-r--. 1 opc opc 23 Apr 12 12:56 mani.txt
-rw-rw-r--. 1 opc opc  0 Mar 17 14:03 server
drwxrwxr-x. 3 opc opc 18 Apr 13 12:46 vignesh
[opc@new-k8s test]$ cd ..
[opc@new-k8s ~]$ sudo chown -R opc:vignesh test/
[opc@new-k8s ~]$ ll
total 3072004
-rw-rw-r--. 1 opc  opc            852 Apr 15 03:15 fruits.txt
drwxrwxr-x. 2 opc  opc             25 Nov 26  2021 prometheus
-rw-rw----. 1 opc  vignesh          0 Apr 15 04:19 random.txt
-rw-r--r--. 1 root root    3145728000 Jan 11  2022 swapfile
drwxrwxr-x. 4 opc  vignesh        100 Apr 13 12:46 test
[opc@new-k8s ~]$ cd test/
[opc@new-k8s test]$ ll
total 8
drwxrwxr-x. 2 opc vignesh 27 Mar 17 14:03 client
-rw-rw-r--. 1 opc vignesh 77 Apr 12 12:26 Dockerfile
-rw-rw-r--. 1 opc vignesh  0 Apr 12 12:54 hello.txt
-rw-rw-r--. 1 opc vignesh 23 Apr 12 12:56 mani.txt
-rw-rw-r--. 1 opc vignesh  0 Mar 17 14:03 server
drwxrwxr-x. 3 opc vignesh 18 Apr 13 12:46 vignesh
```

#### To check date and time

```
[opc@new-k8s test]$ date
Sat Apr 15 04:39:46 GMT 2023
```

#### To print all environment variables using env command

```
[opc@new-k8s test]$ env
XDG_SESSION_ID=172420
HOSTNAME=new-k8s
SELINUX_ROLE_REQUESTED=
TERM=xterm
SHELL=/bin/bash
HISTSIZE=1000
SSH_CLIENT=182.55.51.150 54522 22
SELINUX_USE_CURRENT_RANGE=
OLDPWD=/home/opc
SSH_TTY=/dev/pts/0
USER=opc
LS_COLORS=rs=0:di=01;34:ln=01;36:mh=00:pi=40;33:so=01;35:do=01;35:bd=40;33;01:cd=40;33;01:or=40;31;01:mi=01;05;37;41:su=37;41:sg=30;43:ca=30;41:tw=30;42:ow=34;42:st=37;44:ex=01;32:*.tar=01;31:*.tgz=01;31:*.arc=01;31:*.arj=01;31:*.taz=01;31:*.lha=01;31:*.lz4=01;31:*.lzh=01;31:*.lzma=01;31:*.tlz=01;31:*.txz=01;31:*.tzo=01;31:*.t7z=01;31:*.zip=01;31:*.z=01;31:*.Z=01;31:*.dz=01;31:*.gz=01;31:*.lrz=01;31:*.lz=01;31:*.lzo=01;31:*.xz=01;31:*.bz2=01;31:*.bz=01;31:*.tbz=01;31:*.tbz2=01;31:*.tz=01;31:*.deb=01;31:*.rpm=01;31:*.jar=01;31:*.war=01;31:*.ear=01;31:*.sar=01;31:*.rar=01;31:*.alz=01;31:*.ace=01;31:*.zoo=01;31:*.cpio=01;31:*.7z=01;31:*.rz=01;31:*.cab=01;31:*.jpg=01;35:*.jpeg=01;35:*.gif=01;35:*.bmp=01;35:*.pbm=01;35:*.pgm=01;35:*.ppm=01;35:*.tga=01;35:*.xbm=01;35:*.xpm=01;35:*.tif=01;35:*.tiff=01;35:*.png=01;35:*.svg=01;35:*.svgz=01;35:*.mng=01;35:*.pcx=01;35:*.mov=01;35:*.mpg=01;35:*.mpeg=01;35:*.m2v=01;35:*.mkv=01;35:*.webm=01;35:*.ogm=01;35:*.mp4=01;35:*.m4v=01;35:*.mp4v=01;35:*.vob=01;35:*.qt=01;35:*.nuv=01;35:*.wmv=01;35:*.asf=01;35:*.rm=01;35:*.rmvb=01;35:*.flc=01;35:*.avi=01;35:*.fli=01;35:*.flv=01;35:*.gl=01;35:*.dl=01;35:*.xcf=01;35:*.xwd=01;35:*.yuv=01;35:*.cgm=01;35:*.emf=01;35:*.axv=01;35:*.anx=01;35:*.ogv=01;35:*.ogx=01;35:*.aac=01;36:*.au=01;36:*.flac=01;36:*.mid=01;36:*.midi=01;36:*.mka=01;36:*.mp3=01;36:*.mpc=01;36:*.ogg=01;36:*.ra=01;36:*.wav=01;36:*.axa=01;36:*.oga=01;36:*.spx=01;36:*.xspf=01;36:
MAIL=/var/spool/mail/opc
PATH=/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/home/opc/.local/bin:/home/opc/bin
PWD=/home/opc/test
LANG=en_US.UTF-8
SELINUX_LEVEL_REQUESTED=
HISTCONTROL=ignoredups
SHLVL=1
HOME=/home/opc
LOGNAME=opc
SSH_CONNECTION=182.55.51.150 54522 10.0.1.150 22
LESSOPEN=||/usr/bin/lesspipe.sh %s
XDG_RUNTIME_DIR=/run/user/1000
_=/usr/bin/env
```

#### To print all environment variables using printenv command

```
XDG_SESSION_ID=172420
HOSTNAME=new-k8s
SELINUX_ROLE_REQUESTED=
TERM=xterm
SHELL=/bin/bash
HISTSIZE=1000
SSH_CLIENT=182.55.51.150 54522 22
SELINUX_USE_CURRENT_RANGE=
OLDPWD=/home/opc
SSH_TTY=/dev/pts/0
USER=opc
LS_COLORS=rs=0:di=01;34:ln=01;36:mh=00:pi=40;33:so=01;35:do=01;35:bd=40;33;01:cd=40;33;01:or=40;31;01:mi=01;05;37;41:su=37;41:sg=30;43:ca=30;41:tw=30;42:ow=34;42:st=37;44:ex=01;32:*.tar=01;31:*.tgz=01;31:*.arc=01;31:*.arj=01;31:*.taz=01;31:*.lha=01;31:*.lz4=01;31:*.lzh=01;31:*.lzma=01;31:*.tlz=01;31:*.txz=01;31:*.tzo=01;31:*.t7z=01;31:*.zip=01;31:*.z=01;31:*.Z=01;31:*.dz=01;31:*.gz=01;31:*.lrz=01;31:*.lz=01;31:*.lzo=01;31:*.xz=01;31:*.bz2=01;31:*.bz=01;31:*.tbz=01;31:*.tbz2=01;31:*.tz=01;31:*.deb=01;31:*.rpm=01;31:*.jar=01;31:*.war=01;31:*.ear=01;31:*.sar=01;31:*.rar=01;31:*.alz=01;31:*.ace=01;31:*.zoo=01;31:*.cpio=01;31:*.7z=01;31:*.rz=01;31:*.cab=01;31:*.jpg=01;35:*.jpeg=01;35:*.gif=01;35:*.bmp=01;35:*.pbm=01;35:*.pgm=01;35:*.ppm=01;35:*.tga=01;35:*.xbm=01;35:*.xpm=01;35:*.tif=01;35:*.tiff=01;35:*.png=01;35:*.svg=01;35:*.svgz=01;35:*.mng=01;35:*.pcx=01;35:*.mov=01;35:*.mpg=01;35:*.mpeg=01;35:*.m2v=01;35:*.mkv=01;35:*.webm=01;35:*.ogm=01;35:*.mp4=01;35:*.m4v=01;35:*.mp4v=01;35:*.vob=01;35:*.qt=01;35:*.nuv=01;35:*.wmv=01;35:*.asf=01;35:*.rm=01;35:*.rmvb=01;35:*.flc=01;35:*.avi=01;35:*.fli=01;35:*.flv=01;35:*.gl=01;35:*.dl=01;35:*.xcf=01;35:*.xwd=01;35:*.yuv=01;35:*.cgm=01;35:*.emf=01;35:*.axv=01;35:*.anx=01;35:*.ogv=01;35:*.ogx=01;35:*.aac=01;36:*.au=01;36:*.flac=01;36:*.mid=01;36:*.midi=01;36:*.mka=01;36:*.mp3=01;36:*.mpc=01;36:*.ogg=01;36:*.ra=01;36:*.wav=01;36:*.axa=01;36:*.oga=01;36:*.spx=01;36:*.xspf=01;36:
MAIL=/var/spool/mail/opc
PATH=/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/home/opc/.local/bin:/home/opc/bin
PWD=/home/opc/test
LANG=en_US.UTF-8
SELINUX_LEVEL_REQUESTED=
HISTCONTROL=ignoredups
SHLVL=1
HOME=/home/opc
LOGNAME=opc
SSH_CONNECTION=182.55.51.150 54522 10.0.1.150 22
LESSOPEN=||/usr/bin/lesspipe.sh %s
XDG_RUNTIME_DIR=/run/user/1000
_=/usr/bin/printenv
```

#### To print only one variable

```
[opc@new-k8s test]$ echo $PATH
/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/home/opc/.local/bin:/home/opc/bin
```

---
title: "Linux commands Part 2"
date: 2024-07-01
---

#### free -h

To check ram/memory usage in server

\-h --> Human readable format

By default `free` command will show the ram/memory usage in `KB` (Kilobytes)

```
ubuntu@manikandan:~$ free 
               total        used        free      shared  buff/cache   available
Mem:          987264      334996       85924        1304      566344      472600
Swap:              0           0           0
```

`free -h` will show in MB or GB

```
ubuntu@manikandan:~$ free -h
               total        used        free      shared  buff/cache   available
Mem:           964Mi       327Mi        82Mi       1.0Mi       553Mi       461Mi
Swap:             0B          0B          0B
```

#### df -h

To check disk usage in server

\-h --> Human readable format

By default `df` command will show the disk usage in `KB` (Kilobytes)

```
ubuntu@manikandan:~$ df
Filesystem     1K-blocks    Used Available Use% Mounted on
tmpfs              98728    1276     97452   2% /run
/dev/sda1       47143192 7437908  39688900  16% /
tmpfs             493632       0    493632   0% /dev/shm
tmpfs               5120       0      5120   0% /run/lock
/dev/sda15        106858    6182    100677   6% /boot/efi
tmpfs              98724       4     98720   1% /run/user/1001
```

```
ubuntu@manikandan:~$ df -h
Filesystem      Size  Used Avail Use% Mounted on
tmpfs            97M  1.3M   96M   2% /run
/dev/sda1        45G  7.1G   38G  16% /
tmpfs           483M     0  483M   0% /dev/shm
tmpfs           5.0M     0  5.0M   0% /run/lock
/dev/sda15      105M  6.1M   99M   6% /boot/efi
tmpfs            97M  4.0K   97M   1% /run/user/1001
```

#### which

#### man

#### id

#### hostname

#### cd ..

#### cd ../..

#### cd

#### cd ~

#### cd -

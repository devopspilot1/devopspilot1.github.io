---
title: "Linux Log and Text Processing Commands for DevOps Engineers"
date: 2024-07-01
---

# Linux Log and Text Processing Commands for DevOps Engineers

← [Back to Linux Commands](../index.md)

---

This page covers essential Linux commands used to analyze logs and process text files in real production environments.
You will learn how DevOps engineers search, filter, and extract useful information from large log files efficiently.

---

## Types of Shell

- sh
- bash (Bourne Again Shell)
- zsh
- ksh (Korn Shell)
- csh

Reference: [https://www.shiksha.com/online-courses/articles/introduction-to-types-of-shell/](https://www.shiksha.com/online-courses/articles/introduction-to-types-of-shell/)

## Redirection

```
>  Overwrites the file content, if the file already exists
>> Appends the content to the existing content in the file
```

In both cases, if the file is not present, it will create the file and write the content to it.

By default, the `echo` command prints the output to the screen. But if we use redirection arrows, it can store the output to files.

```
[opc@new-k8s ~]$ mkdir redirection
[opc@new-k8s ~]$ cd redirection/
[opc@new-k8s redirection]$ pwd
/home/opc/redirection
[opc@new-k8s redirection]$ ll
total 0
[opc@new-k8s redirection]$ echo "hello devops" > hello.txt
[opc@new-k8s redirection]$ ll
total 4
-rw-rw-r--. 1 opc opc 13 Apr 17 14:11 hello.txt
[opc@new-k8s redirection]$ cat hello.txt
hello devops
[opc@new-k8s redirection]$ echo "I am learning devops" > hello.txt
[opc@new-k8s redirection]$ ll
total 4
-rw-rw-r--. 1 opc opc 21 Apr 17 14:11 hello.txt
[opc@new-k8s redirection]$ cat hello.txt
I am learning devops
```

```
[opc@new-k8s redirection]$ pwd
/home/opc/redirection
[opc@new-k8s redirection]$ ll
total 0
[opc@new-k8s redirection]$ echo "I eat fruits daily" >> double-arrow.txt
[opc@new-k8s redirection]$ ll
total 4
-rw-rw-r--. 1 opc opc 19 Apr 17 14:13 double-arrow.txt
[opc@new-k8s redirection]$ cat double-arrow.txt
I eat fruits daily
[opc@new-k8s redirection]$ echo "I love banana" >> double-arrow.txt
[opc@new-k8s redirection]$ echo "I also like apples" >> double-arrow.txt
[opc@new-k8s redirection]$ ll
total 4
-rw-rw-r--. 1 opc opc 52 Apr 17 14:13 double-arrow.txt
[opc@new-k8s redirection]$ cat double-arrow.txt
I eat fruits daily
I love banana
I also like apples
```

## wget Command

The `wget` command is used to download binary or large files (e.g., zip, tar, tar.gz files).

```
[opc@new-k8s ~]$ pwd
/home/opc
[opc@new-k8s ~]$ mkdir wget-examples
[opc@new-k8s ~]$ cd wget-examples/
[opc@new-k8s wget-examples]$ pwd
/home/opc/wget-examples
[opc@new-k8s wget-examples]$ ll
total 0
[opc@new-k8s wget-examples]$ wget https://dlcdn.apache.org/maven/maven-3/3.9.1/binaries/apache-maven-3.9.1-bin.zip
--2023-04-17 13:27:27-- https://dlcdn.apache.org/maven/maven-3/3.9.1/binaries/apache-maven-3.9.1-bin.zip
Resolving dlcdn.apache.org (dlcdn.apache.org)... 151.101.2.132, 2a04:4e42::644
Connecting to dlcdn.apache.org (dlcdn.apache.org)|151.101.2.132|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 9143026 (8.7M) [application/zip]
Saving to: ‘apache-maven-3.9.1-bin.zip’

100%[=========================================================================================================================>] 9,143,026   24.9MB/s   in 0.4s

2023-04-17 13:27:28 (24.9 MB/s) - ‘apache-maven-3.9.1-bin.zip’ saved [9143026/9143026]

[opc@new-k8s wget-examples]$ ll
total 8932
-rw-rw-r--. 1 opc opc 9143026 Mar 15 10:00 apache-maven-3.9.1-bin.zip
```

### wget - Quiet Mode

**-q or --quiet** --> Quiet mode, will not show any logs or progress bar.

```
[opc@new-k8s wget-examples]$ wget -q https://dlcdn.apache.org/maven/maven-3/3.9.1/binaries/apache-maven-3.9.1-bin.tar.gz
[opc@new-k8s wget-examples]$ ll -h
total 18M
-rw-rw-r--. 1 opc opc 8.7M Mar 15 10:00 apache-maven-3.9.1-bin.tar.gz
-rw-rw-r--. 1 opc opc 8.8M Mar 15 10:00 apache-maven-3.9.1-bin.zip
```

## curl Command

```
[opc@new-k8s ~]$ mkdir curl-examples
[opc@new-k8s ~]$ cd curl-examples/
[opc@new-k8s curl-examples]$ pwd
/home/opc/curl-examples
[opc@new-k8s curl-examples]$ ll
total 0
[opc@new-k8s curl-examples]$ curl https://dlcdn.apache.org/maven/maven-3/3.9.1/binaries/apache-maven-3.9.1-bin.zip -o apache-maven-3.9.1-bin.zip
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 8928k  100 8928k    0     0  13.4M      0 --:--:-- --:--:-- --:--:-- 13.4M
[opc@new-k8s curl-examples]$ ll
total 8932
-rw-rw-r--. 1 opc opc 9143026 Apr 17 13:35 apache-maven-3.9.1-bin.zip
```

### curl - Silent Mode

-s or --silent --> Will not show the logs or progress bar.

```
[opc@new-k8s curl-examples]$ curl -s https://dlcdn.apache.org/maven/maven-3/3.9.1/source/apache-maven-3.9.1-src.tar.gz -o apache-maven-3.9.1-src.tar.gz
[opc@new-k8s curl-examples]$ ll -h
total 12M
-rw-rw-r--. 1 opc opc 8.8M Apr 17 13:35 apache-maven-3.9.1-bin.zip
-rw-rw-r--. 1 opc opc 2.7M Apr 17 13:38 apache-maven-3.9.1-src.tar.gz
```

## zip & unzip Commands

By default, the `unzip` command will unzip the zip package to the current directory.

```
[opc@new-k8s curl-examples]$ ll
total 11652
-rw-rw-r--. 1 opc opc 9143026 Apr 17 13:35 apache-maven-3.9.1-bin.zip
-rw-rw-r--. 1 opc opc 2784624 Apr 17 13:38 apache-maven-3.9.1-src.tar.gz
[opc@new-k8s curl-examples]$ pwd
/home/opc/curl-examples
[opc@new-k8s curl-examples]$ unzip apache-maven-3.9.1-bin.zip
Archive:  apache-maven-3.9.1-bin.zip
   creating: apache-maven-3.9.1/
   creating: apache-maven-3.9.1/lib/
   creating: apache-maven-3.9.1/boot/
   creating: apache-maven-3.9.1/lib/jansi-native/
   creating: apache-maven-3.9.1/lib/jansi-native/Windows/
   creating: apache-maven-3.9.1/lib/jansi-native/Windows/x86/
   creating: apache-maven-3.9.1/lib/jansi-native/Windows/x86_64/
   creating: apache-maven-3.9.1/bin/
   creating: apache-maven-3.9.1/conf/
   creating: apache-maven-3.9.1/conf/logging/
   creating: apache-maven-3.9.1/lib/ext/
   creating: apache-maven-3.9.1/lib/ext/hazelcast/
   creating: apache-maven-3.9.1/lib/ext/redisson/
  inflating: apache-maven-3.9.1/README.txt
  inflating: apache-maven-3.9.1/LICENSE
  inflating: apache-maven-3.9.1/NOTICE
  inflating: apache-maven-3.9.1/lib/aopalliance.license
  inflating: apache-maven-3.9.1/lib/commons-cli.license
  inflating: apache-maven-3.9.1/lib/commons-codec.license
  inflating: apache-maven-3.9.1/lib/commons-lang3.license
  inflating: apache-maven-3.9.1/lib/failureaccess.license
  inflating: apache-maven-3.9.1/lib/guava.license
  inflating: apache-maven-3.9.1/lib/guice.license
  inflating: apache-maven-3.9.1/lib/httpclient.license
  inflating: apache-maven-3.9.1/lib/httpcore.license
  inflating: apache-maven-3.9.1/lib/jansi.license
  inflating: apache-maven-3.9.1/lib/javax.annotation-api.license
  inflating: apache-maven-3.9.1/lib/javax.inject.license
  inflating: apache-maven-3.9.1/lib/jcl-over-slf4j.license
  inflating: apache-maven-3.9.1/lib/org.eclipse.sisu.inject.license
  inflating: apache-maven-3.9.1/lib/org.eclipse.sisu.plexus.license
  inflating: apache-maven-3.9.1/lib/plexus-cipher.license
  inflating: apache-maven-3.9.1/lib/plexus-component-annotations.license
  inflating: apache-maven-3.9.1/lib/plexus-interpolation.license
  inflating: apache-maven-3.9.1/lib/plexus-sec-dispatcher.license
  inflating: apache-maven-3.9.1/lib/plexus-utils.license
  inflating: apache-maven-3.9.1/lib/slf4j-api.license
  inflating: apache-maven-3.9.1/boot/plexus-classworlds.license
  inflating: apache-maven-3.9.1/lib/jansi-native/Windows/x86/jansi.dll
  inflating: apache-maven-3.9.1/lib/jansi-native/Windows/x86_64/jansi.dll
  inflating: apache-maven-3.9.1/bin/m2.conf
  inflating: apache-maven-3.9.1/bin/mvn.cmd
  inflating: apache-maven-3.9.1/bin/mvnDebug.cmd
  inflating: apache-maven-3.9.1/bin/mvn
  inflating: apache-maven-3.9.1/bin/mvnDebug
  inflating: apache-maven-3.9.1/bin/mvnyjp
  inflating: apache-maven-3.9.1/conf/logging/simplelogger.properties
  inflating: apache-maven-3.9.1/conf/settings.xml
  inflating: apache-maven-3.9.1/conf/toolchains.xml
  inflating: apache-maven-3.9.1/lib/ext/README.txt
  inflating: apache-maven-3.9.1/lib/ext/hazelcast/README.txt
  inflating: apache-maven-3.9.1/lib/ext/redisson/README.txt
  inflating: apache-maven-3.9.1/lib/jansi-native/README.txt
  inflating: apache-maven-3.9.1/boot/plexus-classworlds-2.6.0.jar
  inflating: apache-maven-3.9.1/lib/maven-embedder-3.9.1.jar
  inflating: apache-maven-3.9.1/lib/maven-settings-3.9.1.jar
  inflating: apache-maven-3.9.1/lib/maven-settings-builder-3.9.1.jar
  inflating: apache-maven-3.9.1/lib/maven-plugin-api-3.9.1.jar
  inflating: apache-maven-3.9.1/lib/maven-model-3.9.1.jar
  inflating: apache-maven-3.9.1/lib/maven-model-builder-3.9.1.jar
  inflating: apache-maven-3.9.1/lib/maven-builder-support-3.9.1.jar
  inflating: apache-maven-3.9.1/lib/maven-resolver-api-1.9.7.jar
  inflating: apache-maven-3.9.1/lib/maven-resolver-util-1.9.7.jar
  inflating: apache-maven-3.9.1/lib/maven-shared-utils-3.3.4.jar
  inflating: apache-maven-3.9.1/lib/guice-5.1.0.jar
  inflating: apache-maven-3.9.1/lib/aopalliance-1.0.jar
  inflating: apache-maven-3.9.1/lib/guava-30.1-jre.jar
  inflating: apache-maven-3.9.1/lib/failureaccess-1.0.1.jar
  inflating: apache-maven-3.9.1/lib/javax.inject-1.jar
  inflating: apache-maven-3.9.1/lib/javax.annotation-api-1.3.2.jar
  inflating: apache-maven-3.9.1/lib/plexus-utils-3.5.1.jar
  inflating: apache-maven-3.9.1/lib/plexus-sec-dispatcher-2.0.jar
  inflating: apache-maven-3.9.1/lib/plexus-cipher-2.0.jar
  inflating: apache-maven-3.9.1/lib/plexus-interpolation-1.26.jar
  inflating: apache-maven-3.9.1/lib/slf4j-api-1.7.36.jar
  inflating: apache-maven-3.9.1/lib/commons-lang3-3.8.1.jar
  inflating: apache-maven-3.9.1/lib/maven-core-3.9.1.jar
  inflating: apache-maven-3.9.1/lib/maven-repository-metadata-3.9.1.jar
  inflating: apache-maven-3.9.1/lib/maven-artifact-3.9.1.jar
  inflating: apache-maven-3.9.1/lib/maven-resolver-provider-3.9.1.jar
  inflating: apache-maven-3.9.1/lib/maven-resolver-impl-1.9.7.jar
  inflating: apache-maven-3.9.1/lib/maven-resolver-named-locks-1.9.7.jar
  inflating: apache-maven-3.9.1/lib/maven-resolver-spi-1.9.7.jar
  inflating: apache-maven-3.9.1/lib/org.eclipse.sisu.inject-0.3.5.jar
  inflating: apache-maven-3.9.1/lib/plexus-component-annotations-2.1.0.jar
  inflating: apache-maven-3.9.1/lib/maven-compat-3.9.1.jar
  inflating: apache-maven-3.9.1/lib/wagon-provider-api-3.5.3.jar
  inflating: apache-maven-3.9.1/lib/org.eclipse.sisu.plexus-0.3.5.jar
  inflating: apache-maven-3.9.1/lib/commons-cli-1.4.jar
  inflating: apache-maven-3.9.1/lib/wagon-http-3.5.3.jar
  inflating: apache-maven-3.9.1/lib/wagon-http-shared-3.5.3.jar
  inflating: apache-maven-3.9.1/lib/httpclient-4.5.14.jar
  inflating: apache-maven-3.9.1/lib/commons-codec-1.11.jar
  inflating: apache-maven-3.9.1/lib/wagon-file-3.5.3.jar
  inflating: apache-maven-3.9.1/lib/jcl-over-slf4j-1.7.36.jar
  inflating: apache-maven-3.9.1/lib/maven-resolver-connector-basic-1.9.7.jar
  inflating: apache-maven-3.9.1/lib/maven-resolver-transport-file-1.9.7.jar
  inflating: apache-maven-3.9.1/lib/maven-resolver-transport-http-1.9.7.jar
  inflating: apache-maven-3.9.1/lib/httpcore-4.4.15.jar
  inflating: apache-maven-3.9.1/lib/maven-resolver-transport-wagon-1.9.7.jar
  inflating: apache-maven-3.9.1/lib/maven-slf4j-provider-3.9.1.jar
  inflating: apache-maven-3.9.1/lib/jansi-2.4.0.jar
[opc@new-k8s curl-examples]$ ll
total 11652
drwxr-xr-x. 6 opc opc      99 Mar 15 09:39 apache-maven-3.9.1
-rw-rw-r--. 1 opc opc 9143026 Apr 17 13:35 apache-maven-3.9.1-bin.zip
-rw-rw-r--. 1 opc opc 2784624 Apr 17 13:38 apache-maven-3.9.1-src.tar.gz
```

### Unzip to Specific Directory

Using the `-d` parameter, we can extract the zip package to a different folder.
-q --> Silent mode

Let's extract to the `/tmp` folder.

```
[opc@new-k8s tmp]$ pwd
/tmp
[opc@new-k8s tmp]$ ll
total 0
[opc@new-k8s tmp]$ cd ~/curl-examples/
[opc@new-k8s curl-examples]$ ll
total 11652
-rw-rw-r--. 1 opc opc 9143026 Apr 17 13:35 apache-maven-3.9.1-bin.zip
-rw-rw-r--. 1 opc opc 2784624 Apr 17 13:38 apache-maven-3.9.1-src.tar.gz
[opc@new-k8s curl-examples]$ pwd
/home/opc/curl-examples
[opc@new-k8s curl-examples]$ unzip apache-maven-3.9.1-bin.zip -d /tmp
Archive:  apache-maven-3.9.1-bin.zip
   creating: /tmp/apache-maven-3.9.1/
   creating: /tmp/apache-maven-3.9.1/lib/
   creating: /tmp/apache-maven-3.9.1/boot/
   creating: /tmp/apache-maven-3.9.1/lib/jansi-native/
   creating: /tmp/apache-maven-3.9.1/lib/jansi-native/Windows/
   creating: /tmp/apache-maven-3.9.1/lib/jansi-native/Windows/x86/
   creating: /tmp/apache-maven-3.9.1/lib/jansi-native/Windows/x86_64/
   creating: /tmp/apache-maven-3.9.1/bin/
   creating: /tmp/apache-maven-3.9.1/conf/
   creating: /tmp/apache-maven-3.9.1/conf/logging/
   creating: /tmp/apache-maven-3.9.1/lib/ext/
   creating: /tmp/apache-maven-3.9.1/lib/ext/hazelcast/
   creating: /tmp/apache-maven-3.9.1/lib/ext/redisson/
  inflating: /tmp/apache-maven-3.9.1/README.txt
  inflating: /tmp/apache-maven-3.9.1/LICENSE
  inflating: /tmp/apache-maven-3.9.1/NOTICE
  inflating: /tmp/apache-maven-3.9.1/lib/aopalliance.license
  inflating: /tmp/apache-maven-3.9.1/lib/commons-cli.license
  inflating: /tmp/apache-maven-3.9.1/lib/commons-codec.license
  inflating: /tmp/apache-maven-3.9.1/lib/commons-lang3.license
  inflating: /tmp/apache-maven-3.9.1/lib/failureaccess.license
  inflating: /tmp/apache-maven-3.9.1/lib/guava.license
  inflating: /tmp/apache-maven-3.9.1/lib/guice.license
  inflating: /tmp/apache-maven-3.9.1/lib/httpclient.license
  inflating: /tmp/apache-maven-3.9.1/lib/httpcore.license
  inflating: /tmp/apache-maven-3.9.1/lib/jansi.license
  inflating: /tmp/apache-maven-3.9.1/lib/javax.annotation-api.license
  inflating: /tmp/apache-maven-3.9.1/lib/javax.inject.license
  inflating: /tmp/apache-maven-3.9.1/lib/jcl-over-slf4j.license
  inflating: /tmp/apache-maven-3.9.1/lib/org.eclipse.sisu.inject.license
  inflating: /tmp/apache-maven-3.9.1/lib/org.eclipse.sisu.plexus.license
  inflating: /tmp/apache-maven-3.9.1/lib/plexus-cipher.license
  inflating: /tmp/apache-maven-3.9.1/lib/plexus-component-annotations.license
  inflating: /tmp/apache-maven-3.9.1/lib/plexus-interpolation.license
  inflating: /tmp/apache-maven-3.9.1/lib/plexus-sec-dispatcher.license
  inflating: /tmp/apache-maven-3.9.1/lib/plexus-utils.license
  inflating: /tmp/apache-maven-3.9.1/lib/slf4j-api.license
  inflating: /tmp/apache-maven-3.9.1/boot/plexus-classworlds.license
  inflating: /tmp/apache-maven-3.9.1/lib/jansi-native/Windows/x86/jansi.dll
  inflating: /tmp/apache-maven-3.9.1/lib/jansi-native/Windows/x86_64/jansi.dll
  inflating: /tmp/apache-maven-3.9.1/bin/m2.conf
  inflating: /tmp/apache-maven-3.9.1/bin/mvn.cmd
  inflating: /tmp/apache-maven-3.9.1/bin/mvnDebug.cmd
  inflating: /tmp/apache-maven-3.9.1/bin/mvn
  inflating: /tmp/apache-maven-3.9.1/bin/mvnDebug
  inflating: /tmp/apache-maven-3.9.1/bin/mvnyjp
  inflating: /tmp/apache-maven-3.9.1/conf/logging/simplelogger.properties
  inflating: /tmp/apache-maven-3.9.1/conf/settings.xml
  inflating: /tmp/apache-maven-3.9.1/conf/toolchains.xml
  inflating: /tmp/apache-maven-3.9.1/lib/ext/README.txt
  inflating: /tmp/apache-maven-3.9.1/lib/ext/hazelcast/README.txt
  inflating: /tmp/apache-maven-3.9.1/lib/ext/redisson/README.txt
  inflating: /tmp/apache-maven-3.9.1/lib/jansi-native/README.txt
  inflating: /tmp/apache-maven-3.9.1/boot/plexus-classworlds-2.6.0.jar
  inflating: /tmp/apache-maven-3.9.1/lib/maven-embedder-3.9.1.jar
  inflating: /tmp/apache-maven-3.9.1/lib/maven-settings-3.9.1.jar
  inflating: /tmp/apache-maven-3.9.1/lib/maven-settings-builder-3.9.1.jar
  inflating: /tmp/apache-maven-3.9.1/lib/maven-plugin-api-3.9.1.jar
  inflating: /tmp/apache-maven-3.9.1/lib/maven-model-3.9.1.jar
  inflating: /tmp/apache-maven-3.9.1/lib/maven-model-builder-3.9.1.jar
  inflating: /tmp/apache-maven-3.9.1/lib/maven-builder-support-3.9.1.jar
  inflating: /tmp/apache-maven-3.9.1/lib/maven-resolver-api-1.9.7.jar
  inflating: /tmp/apache-maven-3.9.1/lib/maven-resolver-util-1.9.7.jar
  inflating: /tmp/apache-maven-3.9.1/lib/maven-shared-utils-3.3.4.jar
  inflating: /tmp/apache-maven-3.9.1/lib/guice-5.1.0.jar
  inflating: /tmp/apache-maven-3.9.1/lib/aopalliance-1.0.jar
  inflating: /tmp/apache-maven-3.9.1/lib/guava-30.1-jre.jar
  inflating: /tmp/apache-maven-3.9.1/lib/failureaccess-1.0.1.jar
  inflating: /tmp/apache-maven-3.9.1/lib/javax.inject-1.jar
  inflating: /tmp/apache-maven-3.9.1/lib/javax.annotation-api-1.3.2.jar
  inflating: /tmp/apache-maven-3.9.1/lib/plexus-utils-3.5.1.jar
  inflating: /tmp/apache-maven-3.9.1/lib/plexus-sec-dispatcher-2.0.jar
  inflating: /tmp/apache-maven-3.9.1/lib/plexus-cipher-2.0.jar
  inflating: /tmp/apache-maven-3.9.1/lib/plexus-interpolation-1.26.jar
  inflating: /tmp/apache-maven-3.9.1/lib/slf4j-api-1.7.36.jar
  inflating: /tmp/apache-maven-3.9.1/lib/commons-lang3-3.8.1.jar
  inflating: /tmp/apache-maven-3.9.1/lib/maven-core-3.9.1.jar
  inflating: /tmp/apache-maven-3.9.1/lib/maven-repository-metadata-3.9.1.jar
  inflating: /tmp/apache-maven-3.9.1/lib/maven-artifact-3.9.1.jar
  inflating: /tmp/apache-maven-3.9.1/lib/maven-resolver-provider-3.9.1.jar
  inflating: /tmp/apache-maven-3.9.1/lib/maven-resolver-impl-1.9.7.jar
  inflating: /tmp/apache-maven-3.9.1/lib/maven-resolver-named-locks-1.9.7.jar
  inflating: /tmp/apache-maven-3.9.1/lib/maven-resolver-spi-1.9.7.jar
  inflating: /tmp/apache-maven-3.9.1/lib/org.eclipse.sisu.inject-0.3.5.jar
  inflating: /tmp/apache-maven-3.9.1/lib/plexus-component-annotations-2.1.0.jar
  inflating: /tmp/apache-maven-3.9.1/lib/maven-compat-3.9.1.jar
  inflating: /tmp/apache-maven-3.9.1/lib/wagon-provider-api-3.5.3.jar
  inflating: /tmp/apache-maven-3.9.1/lib/org.eclipse.sisu.plexus-0.3.5.jar
  inflating: /tmp/apache-maven-3.9.1/lib/commons-cli-1.4.jar
  inflating: /tmp/apache-maven-3.9.1/lib/wagon-http-3.5.3.jar
  inflating: /tmp/apache-maven-3.9.1/lib/wagon-http-shared-3.5.3.jar
  inflating: /tmp/apache-maven-3.9.1/lib/httpclient-4.5.14.jar
  inflating: /tmp/apache-maven-3.9.1/lib/commons-codec-1.11.jar
  inflating: /tmp/apache-maven-3.9.1/lib/wagon-file-3.5.3.jar
  inflating: /tmp/apache-maven-3.9.1/lib/jcl-over-slf4j-1.7.36.jar
  inflating: /tmp/apache-maven-3.9.1/lib/maven-resolver-connector-basic-1.9.7.jar
  inflating: /tmp/apache-maven-3.9.1/lib/maven-resolver-transport-file-1.9.7.jar
  inflating: /tmp/apache-maven-3.9.1/lib/maven-resolver-transport-http-1.9.7.jar
  inflating: /tmp/apache-maven-3.9.1/lib/httpcore-4.4.15.jar
  inflating: /tmp/apache-maven-3.9.1/lib/maven-resolver-transport-wagon-1.9.7.jar
  inflating: /tmp/apache-maven-3.9.1/lib/maven-slf4j-provider-3.9.1.jar
  inflating: /tmp/apache-maven-3.9.1/lib/jansi-2.4.0.jar
[opc@new-k8s curl-examples]$ ll
total 11652
-rw-rw-r--. 1 opc opc 9143026 Apr 17 13:35 apache-maven-3.9.1-bin.zip
-rw-rw-r--. 1 opc opc 2784624 Apr 17 13:38 apache-maven-3.9.1-src.tar.gz
[opc@new-k8s curl-examples]$ cd /tmp
[opc@new-k8s tmp]$ pwd
/tmp
[opc@new-k8s tmp]$ ll
total 0
drwxr-xr-x. 6 opc opc 99 Mar 15 09:39 apache-maven-3.9.1
```

## tar Command

```
[opc@new-k8s curl-examples]$ ll
total 11652
-rw-rw-r--. 1 opc opc 9143026 Apr 17 13:35 apache-maven-3.9.1-bin.zip
-rw-rw-r--. 1 opc opc 2784624 Apr 17 13:38 apache-maven-3.9.1-src.tar.gz
[opc@new-k8s curl-examples]$ pwd
/home/opc/curl-examples
[opc@new-k8s curl-examples]$ tar --version
tar (GNU tar) 1.26
Copyright (C) 2011 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>.
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

Written by John Gilmore and Jay Fenlason.
[opc@new-k8s curl-examples]$ tar -xvf apache-maven-3.9.1-src.tar.gz
apache-maven-3.9.1/
apache-maven-3.9.1/.github/
apache-maven-3.9.1/.github/workflows/
apache-maven-3.9.1/apache-maven/
apache-maven-3.9.1/apache-maven/src/
apache-maven-3.9.1/apache-maven/src/bin/
apache-maven-3.9.1/apache-maven/src/conf/
apache-maven-3.9.1/apache-maven/src/conf/logging/
apache-maven-3.9.1/apache-maven/src/lib/
apache-maven-3.9.1/apache-maven/src/lib/ext/
apache-maven-3.9.1/apache-maven/src/lib/ext/hazelcast/
apache-maven-3.9.1/apache-maven/src/lib/ext/redisson/
apache-maven-3.9.1/apache-maven/src/lib/jansi-native/
apache-maven-3.9.1/apache-maven/src/main/
apache-maven-3.9.1/apache-maven/src/main/appended-resources/
apache-maven-3.9.1/apache-maven/src/main/appended-resources/META-INF/
apache-maven-3.9.1/apache-maven/src/main/appended-resources/licenses/
apache-maven-3.9.1/apache-maven/src/main/assembly/
apache-maven-3.9.1/apache-maven/src/site/
apache-maven-3.9.1/apache-maven/src/site/apt/
apache-maven-3.9.1/apache-maven/src/test/
apache-maven-3.9.1/apache-maven/src/test/java/
apache-maven-3.9.1/apache-maven/src/test/java/org/
apache-maven-3.9.1/apache-maven/src/test/java/org/apache/
apache-maven-3.9.1/apache-maven/src/test/java/org/apache/maven/
apache-maven-3.9.1/apache-maven/src/test/java/org/apache/maven/settings/
apache-maven-3.9.1/maven-artifact/
apache-maven-3.9.1/maven-artifact/src/
apache-maven-3.9.1/maven-artifact/src/main/
apache-maven-3.9.1/maven-artifact/src/main/java/
apache-maven-3.9.1/maven-artifact/src/main/java/org/
apache-maven-3.9.1/maven-artifact/src/main/java/org/apache/
apache-maven-3.9.1/maven-artifact/src/main/java/org/apache/maven/
apache-maven-3.9.1/maven-artifact/src/main/java/org/apache/maven/artifact/
apache-maven-3.9.1/maven-artifact/src/main/java/org/apache/maven/artifact/handler/
apache-maven-3.9.1/maven-artifact/src/main/java/org/apache/maven/artifact/metadata/
apache-maven-3.9.1/maven-artifact/src/main/java/org/apache/maven/artifact/repository/
apache-maven-3.9.1/maven-artifact/src/main/java/org/apache/maven/artifact/repository/layout/
apache-maven-3.9.1/maven-artifact/src/main/java/org/apache/maven/artifact/repository/metadata/
apache-maven-3.9.1/maven-artifact/src/main/java/org/apache/maven/artifact/resolver/
apache-maven-3.9.1/maven-artifact/src/main/java/org/apache/maven/artifact/resolver/filter/
apache-maven-3.9.1/maven-artifact/src/main/java/org/apache/maven/artifact/versioning/
apache-maven-3.9.1/maven-artifact/src/main/java/org/apache/maven/repository/
apache-maven-3.9.1/maven-artifact/src/main/java/org/apache/maven/repository/legacy/
apache-maven-3.9.1/maven-artifact/src/main/java/org/apache/maven/repository/legacy/metadata/
[opc@new-k8s curl-examples]$ ll -h
total 12M
drwxr-xr-x. 18 opc opc 4.0K Mar 15 09:39 apache-maven-3.9.1
-rw-rw-r--.  1 opc opc 8.8M Apr 17 13:35 apache-maven-3.9.1-bin.zip
-rw-rw-r--.  1 opc opc 2.7M Apr 17 13:38 apache-maven-3.9.1-src.tar.gz
[opc@new-k8s curl-examples]$ cd apache-maven-3.9.1/
[opc@new-k8s apache-maven-3.9.1]$ ll
total 108
drwxr-xr-x. 3 opc opc    50 Apr 17 13:48 apache-maven
-rw-r--r--. 1 opc opc  4726 Mar 15 09:39 CONTRIBUTING.md
-rw-r--r--. 1 opc opc 11354 Mar 15 09:39 DEPENDENCIES
-rw-r--r--. 1 opc opc   871 Mar 15 09:39 deploySite.sh
-rw-r--r--. 1 opc opc 23461 Mar 15 09:39 doap_Maven.rdf
-rw-r--r--. 1 opc opc  7487 Mar 15 09:39 Jenkinsfile
-rw-r--r--. 1 opc opc 11358 Mar 15 09:39 LICENSE
drwxr-xr-x. 3 opc opc    32 Apr 17 13:48 maven-artifact
drwxr-xr-x. 3 opc opc    32 Apr 17 13:48 maven-builder-support
drwxr-xr-x. 3 opc opc    32 Apr 17 13:48 maven-compat
drwxr-xr-x. 3 opc opc    88 Apr 17 13:48 maven-core
drwxr-xr-x. 3 opc opc    32 Apr 17 13:48 maven-embedder
drwxr-xr-x. 3 opc opc    32 Apr 17 13:48 maven-model
drwxr-xr-x. 3 opc opc    32 Apr 17 13:48 maven-model-builder
drwxr-xr-x. 3 opc opc    32 Apr 17 13:48 maven-plugin-api
drwxr-xr-x. 3 opc opc    32 Apr 17 13:48 maven-repository-metadata
drwxr-xr-x. 3 opc opc    32 Apr 17 13:48 maven-resolver-provider
drwxr-xr-x. 3 opc opc    32 Apr 17 13:48 maven-settings
drwxr-xr-x. 3 opc opc    32 Apr 17 13:48 maven-settings-builder
drwxr-xr-x. 3 opc opc    32 Apr 17 13:48 maven-slf4j-provider
-rw-r--r--. 1 opc opc   166 Mar 15 09:39 NOTICE
-rw-r--r--. 1 opc opc 28045 Mar 15 09:39 pom.xml
-rw-r--r--. 1 opc opc  4114 Mar 15 09:39 README.md
drwxr-xr-x. 3 opc opc    18 Mar 15 09:39 src
[opc@new-k8s apache-maven-3.9.1]$ du -sh .
14M     .
```

### Extract to Specific Directory

Use the `-C` argument to extract to a different directory.

By default, the `tar` command doesn't print any logs to output; if we use `-v`, it shows the logs (extracting file names).

```
[opc@new-k8s tmp]$ pwd
/tmp
[opc@new-k8s tmp]$ ll
total 0
[opc@new-k8s tmp]$ cd ~/curl-examples/
[opc@new-k8s curl-examples]$ pwd
/home/opc/curl-examples
[opc@new-k8s curl-examples]$ ll
total 11652
-rw-rw-r--. 1 opc opc 9143026 Apr 17 13:35 apache-maven-3.9.1-bin.zip
-rw-rw-r--. 1 opc opc 2784624 Apr 17 13:38 apache-maven-3.9.1-src.tar.gz
[opc@new-k8s curl-examples]$ tar -xf apache-maven-3.9.1-src.tar.gz -C /tmp
[opc@new-k8s curl-examples]$ ll
total 11652
-rw-rw-r--. 1 opc opc 9143026 Apr 17 13:35 apache-maven-3.9.1-bin.zip
-rw-rw-r--. 1 opc opc 2784624 Apr 17 13:38 apache-maven-3.9.1-src.tar.gz
[opc@new-k8s curl-examples]$ cd /tmp/
[opc@new-k8s tmp]$ ll
total 4
drwxr-xr-x. 18 opc opc 4096 Mar 15 09:39 apache-maven-3.9.1
[opc@new-k8s tmp]$ pwd
/tmp
```

### Creating Zip Files

`zip -r ZIP_FILE_NAME.zip folder_name`

or

`zip ZIP_FILE_NAME.zip file1.txt file2.txt`

**-q** --> Silent mode

```
[opc@new-k8s zip-file]$ pwd
/home/opc/zip-file
[opc@new-k8s zip-file]$ ll
total 0
drwxr-xr-x. 6 opc opc 99 Mar 15 09:39 apache-maven-3.9.1
[opc@new-k8s zip-file]$ ll apache-maven-3.9.1/
total 36
drwxr-xr-x. 2 opc opc    97 Mar 15 09:39 bin
drwxr-xr-x. 2 opc opc    76 Mar 15 09:39 boot
drwxr-xr-x. 3 opc opc    63 Mar 15 09:39 conf
drwxr-xr-x. 4 opc opc  4096 Mar 15 09:39 lib
-rw-r--r--. 1 opc opc 18644 Mar 15 09:39 LICENSE
-rw-r--r--. 1 opc opc  5036 Mar 15 09:39 NOTICE
-rw-r--r--. 1 opc opc  2533 Mar 15 09:39 README.txt
[opc@new-k8s zip-file]$ zip -r newapache-maven.zip apache-maven-3.9.1
  adding: apache-maven-3.9.1/ (stored 0%)
  adding: apache-maven-3.9.1/lib/ (stored 0%)
  adding: apache-maven-3.9.1/lib/jansi-native/ (stored 0%)
  adding: apache-maven-3.9.1/lib/jansi-native/Windows/ (stored 0%)
  adding: apache-maven-3.9.1/lib/jansi-native/Windows/x86/ (stored 0%)
  adding: apache-maven-3.9.1/lib/jansi-native/Windows/x86/jansi.dll (deflated 69%)
  adding: apache-maven-3.9.1/lib/jansi-native/Windows/x86_64/ (stored 0%)
  adding: apache-maven-3.9.1/lib/jansi-native/Windows/x86_64/jansi.dll (deflated 70%)
  adding: apache-maven-3.9.1/lib/jansi-native/README.txt (deflated 40%)
  adding: apache-maven-3.9.1/lib/ext/ (stored 0%)
  adding: apache-maven-3.9.1/lib/ext/hazelcast/ (stored 0%)
  adding: apache-maven-3.9.1/lib/ext/hazelcast/README.txt (deflated 35%)
  adding: apache-maven-3.9.1/lib/ext/redisson/ (stored 0%)
  adding: apache-maven-3.9.1/lib/ext/redisson/README.txt (deflated 34%)
  adding: apache-maven-3.9.1/lib/ext/README.txt (deflated 26%)
  adding: apache-maven-3.9.1/lib/aopalliance.license (stored 0%)
  adding: apache-maven-3.9.1/lib/commons-cli.license (deflated 65%)
  adding: apache-maven-3.9.1/lib/commons-codec.license (deflated 65%)
  adding: apache-maven-3.9.1/lib/commons-lang3.license (deflated 65%)
  adding: apache-maven-3.9.1/lib/failureaccess.license (deflated 65%)
  adding: apache-maven-3.9.1/lib/guava.license (deflated 65%)
  adding: apache-maven-3.9.1/lib/guice.license (deflated 65%)
  adding: apache-maven-3.9.1/lib/httpclient.license (deflated 65%)
  adding: apache-maven-3.9.1/lib/httpcore.license (deflated 65%)
  adding: apache-maven-3.9.1/lib/jansi.license (deflated 65%)
  adding: apache-maven-3.9.1/lib/javax.annotation-api.license (deflated 67%)
  adding: apache-maven-3.9.1/lib/javax.inject.license (deflated 65%)
  adding: apache-maven-3.9.1/lib/jcl-over-slf4j.license (deflated 65%)
  adding: apache-maven-3.9.1/lib/org.eclipse.sisu.inject.license (deflated 63%)
  adding: apache-maven-3.9.1/lib/org.eclipse.sisu.plexus.license (deflated 63%)
  adding: apache-maven-3.9.1/lib/plexus-cipher.license (deflated 65%)
  adding: apache-maven-3.9.1/lib/plexus-component-annotations.license (deflated 65%)
  adding: apache-maven-3.9.1/lib/plexus-interpolation.license (deflated 65%)
  adding: apache-maven-3.9.1/lib/plexus-sec-dispatcher.license (deflated 65%)
  adding: apache-maven-3.9.1/lib/plexus-utils.license (deflated 65%)
  adding: apache-maven-3.9.1/lib/slf4j-api.license (deflated 42%)
  adding: apache-maven-3.9.1/lib/maven-embedder-3.9.1.jar (deflated 10%)
  adding: apache-maven-3.9.1/lib/maven-settings-3.9.1.jar (deflated 8%)
  adding: apache-maven-3.9.1/lib/maven-settings-builder-3.9.1.jar (deflated 17%)
  adding: apache-maven-3.9.1/lib/maven-plugin-api-3.9.1.jar (deflated 12%)
  adding: apache-maven-3.9.1/lib/maven-model-3.9.1.jar (deflated 5%)
  adding: apache-maven-3.9.1/lib/maven-model-builder-3.9.1.jar (deflated 12%)
  adding: apache-maven-3.9.1/lib/maven-builder-support-3.9.1.jar (deflated 18%)
  adding: apache-maven-3.9.1/lib/maven-resolver-api-1.9.7.jar (deflated 14%)
  adding: apache-maven-3.9.1/lib/maven-resolver-util-1.9.7.jar (deflated 11%)
  adding: apache-maven-3.9.1/lib/maven-shared-utils-3.3.4.jar (deflated 9%)
  adding: apache-maven-3.9.1/lib/guice-5.1.0.jar (deflated 9%)
  adding: apache-maven-3.9.1/lib/aopalliance-1.0.jar (deflated 41%)
  adding: apache-maven-3.9.1/lib/guava-30.1-jre.jar (deflated 11%)
  adding: apache-maven-3.9.1/lib/failureaccess-1.0.1.jar (deflated 40%)
  adding: apache-maven-3.9.1/lib/javax.inject-1.jar (deflated 28%)
  adding: apache-maven-3.9.1/lib/javax.annotation-api-1.3.2.jar (deflated 12%)
  adding: apache-maven-3.9.1/lib/plexus-utils-3.5.1.jar (deflated 7%)
  adding: apache-maven-3.9.1/lib/plexus-sec-dispatcher-2.0.jar (deflated 18%)
  adding: apache-maven-3.9.1/lib/plexus-cipher-2.0.jar (deflated 16%)
  adding: apache-maven-3.9.1/lib/plexus-interpolation-1.26.jar (deflated 15%)
  adding: apache-maven-3.9.1/lib/slf4j-api-1.7.36.jar (deflated 12%)
  adding: apache-maven-3.9.1/lib/commons-lang3-3.8.1.jar (deflated 8%)
  adding: apache-maven-3.9.1/lib/maven-core-3.9.1.jar (deflated 10%)
  adding: apache-maven-3.9.1/lib/maven-repository-metadata-3.9.1.jar (deflated 12%)
  adding: apache-maven-3.9.1/lib/maven-artifact-3.9.1.jar (deflated 13%)
  adding: apache-maven-3.9.1/lib/maven-resolver-provider-3.9.1.jar (deflated 9%)
  adding: apache-maven-3.9.1/lib/maven-resolver-impl-1.9.7.jar (deflated 10%)
  adding: apache-maven-3.9.1/lib/maven-resolver-named-locks-1.9.7.jar (deflated 15%)
  adding: apache-maven-3.9.1/lib/maven-resolver-spi-1.9.7.jar (deflated 23%)
  adding: apache-maven-3.9.1/lib/org.eclipse.sisu.inject-0.3.5.jar (deflated 9%)
  adding: apache-maven-3.9.1/lib/plexus-component-annotations-2.1.0.jar (deflated 43%)
  adding: apache-maven-3.9.1/lib/maven-compat-3.9.1.jar (deflated 10%)
  adding: apache-maven-3.9.1/lib/wagon-provider-api-3.5.3.jar (deflated 13%)
  adding: apache-maven-3.9.1/lib/org.eclipse.sisu.plexus-0.3.5.jar (deflated 14%)
  adding: apache-maven-3.9.1/lib/commons-cli-1.4.jar (deflated 8%)
  adding: apache-maven-3.9.1/lib/wagon-http-3.5.3.jar (deflated 19%)
  adding: apache-maven-3.9.1/lib/wagon-http-shared-3.5.3.jar (deflated 8%)
  adding: apache-maven-3.9.1/lib/httpclient-4.5.14.jar (deflated 9%)
  adding: apache-maven-3.9.1/lib/commons-codec-1.11.jar (deflated 16%)
  adding: apache-maven-3.9.1/lib/wagon-file-3.5.3.jar (deflated 16%)
  adding: apache-maven-3.9.1/lib/jcl-over-slf4j-1.7.36.jar (deflated 15%)
  adding: apache-maven-3.9.1/lib/maven-resolver-connector-basic-1.9.7.jar (deflated 10%)
  adding: apache-maven-3.9.1/lib/maven-resolver-transport-file-1.9.7.jar (deflated 15%)
  adding: apache-maven-3.9.1/lib/maven-resolver-transport-http-1.9.7.jar (deflated 9%)
  adding: apache-maven-3.9.1/lib/httpcore-4.4.15.jar (deflated 10%)
  adding: apache-maven-3.9.1/lib/maven-resolver-transport-wagon-1.9.7.jar (deflated 15%)
  adding: apache-maven-3.9.1/lib/maven-slf4j-provider-3.9.1.jar (deflated 11%)
  adding: apache-maven-3.9.1/lib/jansi-2.4.0.jar (deflated 6%)
  adding: apache-maven-3.9.1/boot/ (stored 0%)
  adding: apache-maven-3.9.1/boot/plexus-classworlds.license (deflated 65%)
  adding: apache-maven-3.9.1/boot/plexus-classworlds-2.6.0.jar (deflated 14%)
  adding: apache-maven-3.9.1/bin/ (stored 0%)
  adding: apache-maven-3.9.1/bin/m2.conf (deflated 52%)
  adding: apache-maven-3.9.1/bin/mvn.cmd (deflated 64%)
  adding: apache-maven-3.9.1/bin/mvnDebug.cmd (deflated 55%)
  adding: apache-maven-3.9.1/bin/mvn (deflated 62%)
  adding: apache-maven-3.9.1/bin/mvnDebug (deflated 51%)
  adding: apache-maven-3.9.1/bin/mvnyjp (deflated 48%)
  adding: apache-maven-3.9.1/conf/ (stored 0%)
  adding: apache-maven-3.9.1/conf/logging/ (stored 0%)
  adding: apache-maven-3.9.1/conf/logging/simplelogger.properties (deflated 52%)
  adding: apache-maven-3.9.1/conf/settings.xml (deflated 63%)
  adding: apache-maven-3.9.1/conf/toolchains.xml (deflated 60%)
  adding: apache-maven-3.9.1/README.txt (deflated 57%)
  adding: apache-maven-3.9.1/LICENSE (deflated 72%)
  adding: apache-maven-3.9.1/NOTICE (deflated 58%)
[opc@new-k8s zip-file]$ ll
total 8924
drwxr-xr-x. 6 opc opc      99 Mar 15 09:39 apache-maven-3.9.1
-rw-rw-r--. 1 opc opc 9137892 Apr 17 14:39 newapache-maven.zip
```

## JSON Basics

JSON file contains key-value pairs.

A JSON file name ends with the extension ".json" (e.g., `output.json`).

```
{
  "name": "john",
  "age": "30",
  "car": "BMW",
  "games": ["cricket", "basketball", "badminton"]  
}
```

or

```
{"name":"John", "age":30, "car":null, "games": ["cricket", "basketball", "badminton"]}
```

## Processing JSON with curl

Most of the time, the `curl` command is used for calling a REST API.

In simple terms, a REST API is a URL (e.g., [https://example.com](https://example.com)). When we call that URL, we get response data.

In most cases, the response data will be in JSON format.

Actual Data in GUI : [https://github.com/vigneshsweekaran/hello-world/releases/tag/clean](https://github.com/vigneshsweekaran/hello-world/releases/tag/clean)

```
[opc@new-k8s redirection]$ curl https://api.github.com/repos/vigneshsweekaran/hello-world/releases/latest
{
  "url": "https://api.github.com/repos/vigneshsweekaran/hello-world/releases/43010389",
  "assets_url": "https://api.github.com/repos/vigneshsweekaran/hello-world/releases/43010389/assets",
  "upload_url": "https://uploads.github.com/repos/vigneshsweekaran/hello-world/releases/43010389/assets{?name,label}",
  "html_url": "https://github.com/vigneshsweekaran/hello-world/releases/tag/clean",
  "id": 43010389,
  "author": {
    "login": "vigneshsweekaran",
    "id": 40670015,
    "node_id": "MDQ6VXNlcjQwNjcwMDE1",
    "avatar_url": "https://avatars.githubusercontent.com/u/40670015?v=4",
    "gravatar_id": "",
    "url": "https://api.github.com/users/vigneshsweekaran",
    "html_url": "https://github.com/vigneshsweekaran",
    "followers_url": "https://api.github.com/users/vigneshsweekaran/followers",
    "following_url": "https://api.github.com/users/vigneshsweekaran/following{/other_user}",
    "gists_url": "https://api.github.com/users/vigneshsweekaran/gists{/gist_id}",
    "starred_url": "https://api.github.com/users/vigneshsweekaran/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/vigneshsweekaran/subscriptions",
    "organizations_url": "https://api.github.com/users/vigneshsweekaran/orgs",
    "repos_url": "https://api.github.com/users/vigneshsweekaran/repos",
    "events_url": "https://api.github.com/users/vigneshsweekaran/events{/privacy}",
    "received_events_url": "https://api.github.com/users/vigneshsweekaran/received_events",
    "type": "User",
    "site_admin": false
  },
  "node_id": "MDc6UmVsZWFzZTQzMDEwMzg5",
  "tag_name": "clean",
  "target_commitish": "master",
  "name": "Clean repo with maven application",
  "draft": false,
  "prerelease": false,
  "created_at": "2021-05-16T06:18:49Z",
  "published_at": "2021-05-16T06:26:47Z",
  "assets": [

  ],
  "tarball_url": "https://api.github.com/repos/vigneshsweekaran/hello-world/tarball/clean",
  "zipball_url": "https://api.github.com/repos/vigneshsweekaran/hello-world/zipball/clean",
  "body": ""
}
```

### Saving API Response to File

```
[opc@new-k8s ~]$ mkdir json-response
[opc@new-k8s ~]$ cd json-response/
[opc@new-k8s json-response]$ ll
total 0
[opc@new-k8s json-response]$ pwd
/home/opc/json-response
[opc@new-k8s json-response]$ curl https://api.github.com/repos/vigneshsweekaran/hello-world/releases/latest > output.json
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  2026  100  2026    0     0   2809      0 --:--:-- --:--:-- --:--:-- 2809
[opc@new-k8s json-response]$ ll
total 4
-rw-rw-r--. 1 opc opc 2026 Apr 17 14:23 output.json
[opc@new-k8s json-response]$ cat output.json
{
  "url": "https://api.github.com/repos/vigneshsweekaran/hello-world/releases/43010389",
  "assets_url": "https://api.github.com/repos/vigneshsweekaran/hello-world/releases/43010389/assets",
  "upload_url": "https://uploads.github.com/repos/vigneshsweekaran/hello-world/releases/43010389/assets{?name,label}",
  "html_url": "https://github.com/vigneshsweekaran/hello-world/releases/tag/clean",
  "id": 43010389,
  "author": {
    "login": "vigneshsweekaran",
    "id": 40670015,
    "node_id": "MDQ6VXNlcjQwNjcwMDE1",
    "avatar_url": "https://avatars.githubusercontent.com/u/40670015?v=4",
    "gravatar_id": "",
    "url": "https://api.github.com/users/vigneshsweekaran",
    "html_url": "https://github.com/vigneshsweekaran",
    "followers_url": "https://api.github.com/users/vigneshsweekaran/followers",
    "following_url": "https://api.github.com/users/vigneshsweekaran/following{/other_user}",
    "gists_url": "https://api.github.com/users/vigneshsweekaran/gists{/gist_id}",
    "starred_url": "https://api.github.com/users/vigneshsweekaran/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/vigneshsweekaran/subscriptions",
    "organizations_url": "https://api.github.com/users/vigneshsweekaran/orgs",
    "repos_url": "https://api.github.com/users/vigneshsweekaran/repos",
    "events_url": "https://api.github.com/users/vigneshsweekaran/events{/privacy}",
    "received_events_url": "https://api.github.com/users/vigneshsweekaran/received_events",
    "type": "User",
    "site_admin": false
  },
  "node_id": "MDc6UmVsZWFzZTQzMDEwMzg5",
  "tag_name": "clean",
  "target_commitish": "master",
  "name": "Clean repo with maven application",
  "draft": false,
  "prerelease": false,
  "created_at": "2021-05-16T06:18:49Z",
  "published_at": "2021-05-16T06:26:47Z",
  "assets": [

  ],
  "tarball_url": "https://api.github.com/repos/vigneshsweekaran/hello-world/tarball/clean",
  "zipball_url": "https://api.github.com/repos/vigneshsweekaran/hello-world/zipball/clean",
  "body": ""
}
```

## 🧠 Quick Quiz — Log & Text Processing

<quiz>
Which command allows you to follow a log file in real time as new lines are added?
- [ ] grep
- [x] tail -f
- [ ] less
- [ ] head

The `tail -f` command is commonly used by DevOps engineers to monitor live logs.
</quiz>

---

### 📝 Want More Practice?

To strengthen your understanding and prepare for interviews, try the **full 20-question practice quiz** based on this chapter:

👉 **[Start Log & Text Processing Quiz (20 Questions)](../../quiz/linux-commands/linux-log-text-processing/index.md)**

---

{% include-markdown "_partials/subscribe-guides.md" %}

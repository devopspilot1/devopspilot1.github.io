---
title: "Linux File and Directory Management Commands"
description: "Master linux file and directory management commands with standard to advanced techniques for DevOps engineering."
---

# Linux File and Directory Management Commands

← [Back to Linux Commands](../index.md)

---

This section covers **file and directory management commands** that DevOps engineers use daily while working with application code, logs, configuration files, and automation scripts.

---

## `mkdir` – Create Directory

Used to create a new directory.

```bash
mkdir logs
```

---

## `mkdir -p` – Create Parent Directories

Creates parent directories automatically if they do not exist.

```bash
mkdir -p app/config/nginx
```

📌 **DevOps Use Case:** Creating nested directory structures in one command.

---

## `rmdir` – Remove Empty Directory

Used to delete an **empty directory**.

```bash
rmdir old_logs
```

⚠️ If the directory is not empty, this command will fail.

---

## `rm -rf` – Remove Files and Directories Forcefully

Deletes files or directories **recursively and forcefully**.

```bash
rm -rf temp/
```

⚠️ **Warning:** This command permanently deletes data. Use with extreme caution in production.

---

## `touch` – Create Empty File

Used to create an empty file or update file timestamp.

```bash
touch app.log
```

---

## `vi` – Edit Files

Used to create or edit files using the **vi editor**.

```bash
vi config.yaml
```

📌 Common vi modes:
- Insert mode (`i`)
- Save and exit (`:wq`)
- Exit without saving (`:q!`)

---

## `cat` – View File Content

Used to print or read the content of a file.

```bash
cat file_name
```

---

## `tree` – Display Directory Structure

Displays directory structure in a tree format.

```bash
tree
```

📌 **DevOps Tip:** Useful for understanding project folder layout.

---

## `cp` – Copy Files or Directories

Used to copy files or directories.

```bash
cp source.txt destination.txt
```

Copy directories recursively:

```bash
cp -r app/ backup_app/
```

---

## `mv` – Move or Rename Files

Used to move or rename files and directories.

```bash
mv old.txt new.txt
```

---

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

## find Command

The `find` command is used to search for files or directories.

```
[opc@new-k8s ~]$ ll
total 3072036
-rw-rw-r--. 1 opc  opc         852 Apr 15 03:15 fruits.txt
-rw-rw-r--. 1 opc  opc          43 Apr 19 12:38 hello.txt
-rw-rw-r--. 1 opc  opc        9943 Apr 19 11:16 india.txt
-rwxrwxr-x. 1 opc  opc          81 Apr 15 13:27 newtest
-rw-rw-r--. 1 opc  opc        2026 Apr 19 12:06 output.json
drwxrwxr-x. 2 opc  opc          25 Nov 26  2021 prometheus
-rw-rw-r--. 1 opc  opc         282 Apr 19 12:34 states.txt
-rw-r--r--. 1 root root 3145728000 Jan 11  2022 swapfile
drwxrwxr-x. 4 opc  opc         100 Apr 15 13:04 test
-rw-rw-r--. 1 opc  opc          74 Apr 19 12:11 test.json
```

```
[opc@new-k8s ~]$ pwd
/home/opc
```

```
[opc@new-k8s ~]$ find ./ -name test.json
./test.json
```

You can also find files in a different folder.

```
[opc@new-k8s ~]$ pwd
/home/opc
```

```
[opc@new-k8s ~]$ ll /tmp
total 8
-rw-------. 1 root root 1097 Apr 20 08:40 dhclient-exit-hooksPuY.log
-rw-rw-r--. 1 opc  opc  2026 Apr 20 11:14 output.json
```

```
[opc@new-k8s ~]$ find /tmp -name output.json
/tmp/output.json
```

You can also find the file in whole file system, but it will take some time, it will check all files and directories

```
find: ‘/var/spool/at’: Permission denied
find: ‘/root’: Permission denied
/tmp/output.json
find: ‘/usr/share/polkit-1/rules.d’: Permission denied
find: ‘/usr/libexec/initscripts/legacy-actions/auditd’: Permission denied
/home/opc/output.json
find: ‘/home/vignesh’: Permission denied
find: ‘/opt/containerd’: Permission denied
```

### Find Empty Files & Directories

```
[opc@new-k8s ~]$ find ./ -empty
./test/server
./test/client/server-client
./test/hello.txt
./test/vignesh/mani/raghav
```

### Find Empty Files Only

```
[opc@new-k8s ~]$ find ./ -type f -empty
./test/server
./test/client/server-client
./test/hello.txt
```

### Find Empty Directories Only

```
[opc@new-k8s ~]$ find ./ -type d -empty
./test/vignesh/mani/raghav
```

### Find and Delete Empty Files

```
find ./ -type f -empty -exec rm -i {} ;
```

## locate Command

The `locate` command is used for quickly finding files and directories.

The `locate` command doesn't search the entire filesystem, but looks through a regularly updated file database in the system. Thus, the search completes much faster.

-i --> ignore case

```
[opc@new-k8s ~]$ locate hello
/home/opc/hello.txt
/home/opc/test/hello.txt
```

Sometimes, even deleted files are shown in the output of the `locate` command because it's not updated yet in the locate database.

-e --> argument to search the filesystem (checks existence)

```
[opc@new-k8s ~]$ pwd
/home/opc
```

```
[opc@new-k8s ~]$ ll
total 3072032
-rw-rw-r--. 1 opc  opc         852 Apr 15 03:15 fruits.txt
-rw-rw-r--. 1 opc  opc           0 Apr 20 11:46 hello.txt
-rw-rw-r--. 1 opc  opc        9943 Apr 19 11:16 india.txt
-rwxrwxr-x. 1 opc  opc          81 Apr 15 13:27 newtest
-rw-rw-r--. 1 opc  opc        2026 Apr 19 12:06 output.json
drwxrwxr-x. 2 opc  opc          25 Nov 26  2021 prometheus
-rw-rw-r--. 1 opc  opc         282 Apr 19 12:34 states.txt
-rw-r--r--. 1 root root 3145728000 Jan 11  2022 swapfile
drwxrwxr-x. 4 opc  opc          86 Apr 20 11:46 test
-rw-rw-r--. 1 opc  opc          74 Apr 19 12:11 test.json
```

```
[opc@new-k8s ~]$ locate hello.txt
/home/opc/hello.txt
/home/opc/test/hello.txt
```

```
[opc@new-k8s ~]$ rm -f hello.txt
```

```
[opc@new-k8s ~]$ locate hello.txt
/home/opc/hello.txt
/home/opc/test/hello.txt
```

```
[opc@new-k8s ~]$ locate -e hello.txt
/home/opc/test/hello.txt
```

## Practice Tasks

1. Create a directory named `project`
2. Inside it, create `logs/app`
3. Create a file named `app.log`
4. Copy `app.log` to `backup.log`
5. Rename `backup.log` to `app_backup.log`
6. Delete the `logs` directory

---

## 🧠 Quick Quiz – File Management

<quiz>
Which command creates parent directories automatically if they do not exist?
- [ ] mkdir
- [x] mkdir -p
- [ ] rmdir
- [ ] rm -rf

The `-p` option allows mkdir to create missing parent directories.
</quiz>

---

### 📝 Want More Practice?

To strengthen your understanding and prepare for interviews, try the **full 20-question practice quiz** based on this chapter:

👉 **[Start File & Directory Management Quiz (20 Questions)](../../quiz/linux-commands/linux-file-directory-commands/index.md)**

---

{% include-markdown ".partials/subscribe-guides.md" %}

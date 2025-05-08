---
title: "How to install Java and compile a single Java file"
date: 2024-07-01
---

### Install Java in the Ubuntu Operating system

Run the below command to install Java 21 in the Ubuntu operating system

```bash
sudo apt install openjdk-21-jdk
```

### Install Java in the Centos Operating system

Run the below command to install Java 21 in the Centos operating system

```bash
sudo yum install java-21-openjdk
```

### To check the Java version

Run the below command to check the installed Java version

```bash
java --version
```

**Output:**

```
ubuntu@vignesh-jenkins2:~$ java --version
openjdk 21.0.4 2024-07-16
OpenJDK Runtime Environment (build 21.0.4+7-Ubuntu-1ubuntu224.04)
OpenJDK 64-Bit Server VM (build 21.0.4+7-Ubuntu-1ubuntu224.04, mixed mode, sharing)
```

### Compiling and running a Java file

1\. Create a sample Java file **HelloWorld.java**

```java
class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World!"); 
    }
}
```

**Output:**

```
ubuntu@vignesh:~$ ll
-rw-rw-r-- 1 ubuntu ubuntu  118 Aug 12 10:18 HelloWorld.java
```

2\. Compile the Java file **HelloWorld.java**

Run the **javac** command followed by file name to compile the Java file. E.g. **javac HelloWorld.java**

```bash
javac HelloWorld.java
```

Once the compilation finishes, it will create a **HelloWorld.class** file

3\. Run the **ls -l** command to check the created **HelloWorld.class** file

```
ls -l
```

**Output:**

```
ubuntu@vignesh:~$ ll
-rw-rw-r-- 1 ubuntu ubuntu 427 Aug 12 10:24 HelloWorld.class
-rw-rw-r-- 1 ubuntu ubuntu 118 Aug 12 10:18 HelloWorld.java
```

4\. Run the Java program

Type the **java** command following the Filename without extension to run the Java program E.g. java HelloWorld

```bash
java HelloWorld
```

**Output:**

```
ubuntu@vignesh:~$ java HelloWorld 
Hello, World!
```

### Why do we need to compile the Java code?

The Java code is only understood by humans, computers/machines cannot understand this code. The computer can understand only 0's and 1's

So the Java compiler will convert the Java code to machine understandable code

### What is a compiler?

- A compiler is a program that inputs a **high-level language** and outputs a **low-level language** (such as assembly or machine code).

- It is a computer program that converts programming language code into machine code (human-readable code to a binary 0 and 1 bit language for a computer processor to understand).

- The computer then executes the machine code to complete the task.

### Key points of Compiler:

- Compilers check all types of errors, limits, and ranges.

- It takes longer to run and also requires more memory.

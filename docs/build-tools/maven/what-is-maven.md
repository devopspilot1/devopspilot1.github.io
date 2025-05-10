---
title: "What is Maven?"
date: 2024-08-12
---

Maven is a **build automation** and **project management tool** used primarily in **Java** projects.

Here are some reasons why Maven is widely used:

**Build Automation**: Maven automates the build process, including compiling code, running tests, packaging the application (e.g., creating JAR/WAR files), and generating reports. This reduces manual work and the likelihood of errors.

**Dependency Management**: Maven automatically downloads and links libraries and dependencies required for your project. This ensures that all the necessary dependencies are available and correctly versioned, making it easier to manage complex projects.

**Standardized Project Structure**: Maven enforces a standard directory layout and build process. This consistency makes it easier to understand and navigate projects, especially when working in teams.

**Reference:** [click here](https://maven.apache.org/what-is-maven.html)

### Why do you need Maven?

The main purpose of Maven is to **build automation** and **dependency management**

When you start working on the Java project, initially you will create 1 or 2 files, compiling those Java files and running the Java program should be fine.

But when your project grows, you will start creating multiple Java files (E.g. 50 Java files), then compiling each Java file will be a boring task. To automate this build process maven is used effectively

After compiling, using Maven you can easily run the unit test case and package them as (jar, war) for deployment

During compilation, your project might depend on external libraries (dependencies), this can be easily defined in pom.xml and automatically downloaded and linked by Maven.

### **Java Program without Maven**

1\. Create a sample **Calculator.java** file

This Java code has methods(add, subtract) to do the **addition** and **subtraction** of two numbers defined in the variables **num1**, and **num2** and finally **print the output**.

```java
public class Calculator {
    // Method to add two numbers
    public double add(double num1, double num2) {
        return num1 + num2;
    }

    // Method to subtract two numbers
    public double subtract(double num1, double num2) {
        return num1 - num2;
    }

    public static void main(String[] args) {
        Calculator calculator = new Calculator();

        double num1 = 3;
        double num2 = 2;

        System.out.println("Sum: " + calculator.add(num1, num2));
        System.out.println("Difference: " + calculator.subtract(num1, num2));
    }
}
```

2\. Run the **ll** command to check Calculator.java file is created

```bash
ll
```

**Output:**

```
ubuntu@vignesh-jenkins2:~/java$ ll
-rw-rw-r-- 1 ubuntu ubuntu  598 Aug 12 13:14 Calculator.java
```

3\. Compile the Java file **Calculator.java**

Run the **javac** command followed by file name to compile the Java file. E.g. **javac Calculator.java**

```bash
javac Calculator.java
```

Once the compilation finishes, it will create a **HelloWorld.class** file

 4. Run the **ll** command to check the created **Calculator.class** file

**Output:**

```
ubuntu@vignesh-jenkins2:~/java$ ll
-rw-rw-r-- 1 ubuntu ubuntu 1086 Aug 12 13:20 Calculator.class
-rw-rw-r-- 1 ubuntu ubuntu  598 Aug 12 13:14 Calculator.java
```

5\. Run the Calculator Java program

Type the **java** command following the Filename without extension to run the Java program E.g. **java Calculator**

```bash
java Calculator
```

**Output:**

```
ubuntu@vignesh-jenkins2:~/java$ java Calculator
Sum: 5.0
Difference: 1.0
```

6\. Create a Unit Test Java file for the Calculator Program

**Unit test** is a process to test the **method** or **small unit** in a program.

In the above program, you have **2 methods add and subtract**. Unit test is used to test whether these 2 methods will give a correct output when you give different inputs (scenarios).

**JUnit** is a widely used **unit testing framework** for Java programming language

Create a file **CalculatorTest.java**

```java
import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class CalculatorTest {

    @Test
    public void testAdd() {
        Calculator calculator = new Calculator();
        double result = calculator.add(10, 5);
        assertEquals(15, result, 0);
    }

    @Test
    public void testSubtract() {
        Calculator calculator = new Calculator();
        double result = calculator.subtract(10, 5);
        assertEquals(5, result, 0);
    }
}
```

The above Java file will refer to the **Calculator** Java file and call the **add** method by passing two numbers (10, 5), expecting the **result to be 15**. If the **add** method returns 15, then this test case is a **pass**.

Similarly, it calls the **subtract** method by passing two numbers (10, 5), expecting the **result to be 5**. If the **subtract** method returns 5, then the test case is a **pass** else **fail**.

It uses the JUnit **assertEquals** methods to check whether the output is Equal to your expected value or not.

7\. Run the **ll** command to check **CalculatorTest.java** file is created

```bash
ll
```

**Output:**

```
ubuntu@vignesh-jenkins2:~/java$ ll
-rw-rw-r-- 1 ubuntu ubuntu 1086 Aug 12 13:20 Calculator.class
-rw-rw-r-- 1 ubuntu ubuntu  598 Aug 12 13:14 Calculator.java
-rw-rw-r-- 1 ubuntu ubuntu  468 Aug 12 13:47 CalculatorTest.java
```

8\. Compile the Test Java file **CalculatorTest.java**

Run the following command to compile the **CalculatorTest.java**

```bash
javac CalculatorTest.java
```

**Output:**

```
ubuntu@vignesh-jenkins2:~/java$ javac CalculatorTest.java
CalculatorTest.java:1: error: package org.junit does not exist
import org.junit.Test;
                ^
CalculatorTest.java:2: error: package org.junit does not exist
import static org.junit.Assert.assertEquals;
                       ^
CalculatorTest.java:2: error: static import only from classes and interfaces
import static org.junit.Assert.assertEquals;
^
CalculatorTest.java:6: error: cannot find symbol
    @Test
     ^
  symbol:   class Test
  location: class CalculatorTest
CalculatorTest.java:13: error: cannot find symbol
    @Test
     ^
  symbol:   class Test
  location: class CalculatorTest
CalculatorTest.java:10: error: cannot find symbol
        assertEquals(15, result, 0);
        ^
  symbol:   method assertEquals(int,double,int)
  location: class CalculatorTest
CalculatorTest.java:17: error: cannot find symbol
        assertEquals(5, result, 0);
        ^
  symbol:   method assertEquals(int,double,int)
  location: class CalculatorTest
7 errors
```

Compilation fails since it depends on the **junit** Java library

9\. Download the Junit library file

In Java library files are available in the **.jar** extension.

Run the following command to download the 2 jar files. **junit library** depends on the **hamcrest-core** library. This is called **transitive dependency**

```bash
wget https://repo1.maven.org/maven2/junit/junit/4.13.2/junit-4.13.2.jar
wget https://repo1.maven.org/maven2/org/hamcrest/hamcrest-core/1.3/hamcrest-core-1.3.jar
```

**Output:**

```
ubuntu@vignesh-jenkins2:~/java$ wget https://repo1.maven.org/maven2/junit/junit/4.13.2/junit-4.13.2.jar
--2024-08-12 14:22:37-- https://repo1.maven.org/maven2/junit/junit/4.13.2/junit-4.13.2.jar
Resolving repo1.maven.org (repo1.maven.org)... 151.101.40.209, 2a04:4e42:a::209
Connecting to repo1.maven.org (repo1.maven.org)|151.101.40.209|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 384581 (376K) [application/java-archive]
Saving to: ‘junit-4.13.2.jar’

junit-4.13.2.jar                    100%[================================================================>] 375.57K   417KB/s    in 0.9s    

2024-08-12 14:22:38 (417 KB/s) - ‘junit-4.13.2.jar’ saved [384581/384581]
```

```
ubuntu@vignesh-jenkins2:~/java$ wget https://repo1.maven.org/maven2/org/hamcrest/hamcrest-core/1.3/hamcrest-core-1.3.jar
--2024-08-12 14:22:44-- https://repo1.maven.org/maven2/org/hamcrest/hamcrest-core/1.3/hamcrest-core-1.3.jar
Resolving repo1.maven.org (repo1.maven.org)... 151.101.40.209, 2a04:4e42:a::209
Connecting to repo1.maven.org (repo1.maven.org)|151.101.40.209|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 45024 (44K) [application/java-archive]
Saving to: ‘hamcrest-core-1.3.jar’

hamcrest-core-1.3.jar               100%[================================================================>]  43.97K   177KB/s    in 0.2s    

2024-08-12 14:22:46 (177 KB/s) - ‘hamcrest-core-1.3.jar’ saved [45024/45024]
```

 10. Run the **ll** command to see the downloaded files

```bash
ll
```

**Output:**

```
ubuntu@vignesh-jenkins2:~/java$ ll
-rw-rw-r-- 1 ubuntu ubuntu   1086 Aug 12 13:20 Calculator.class
-rw-rw-r-- 1 ubuntu ubuntu    598 Aug 12 13:14 Calculator.java
-rw-rw-r-- 1 ubuntu ubuntu    468 Aug 12 13:47 CalculatorTest.java
-rw-rw-r-- 1 ubuntu ubuntu  45024 Jul  9  2012 hamcrest-core-1.3.jar
-rw-rw-r-- 1 ubuntu ubuntu 384581 Feb 13  2021 junit-4.13.2.jar
```

11 Compile the Test Java file **CalculatorTest.java**

You need to pass the **jar files as parameters** to the **javac** command to refer to the jar files during compilation

Run the following command to compile

```bash
javac -cp .:junit-4.13.2.jar:hamcrest-core-1.3.jar CalculatorTest.java
```

Once the compilation finishes, it will create a **CalculatorTest.class** file

 12. Run the **ll** command to check the created **CalculatorTest.class** file

```bash
ll
```

**Output:**

```
ubuntu@vignesh-jenkins2:~/java$ ll
-rw-rw-r-- 1 ubuntu ubuntu   1086 Aug 12 13:20 Calculator.class
-rw-rw-r-- 1 ubuntu ubuntu    598 Aug 12 13:14 Calculator.java
-rw-rw-r-- 1 ubuntu ubuntu    603 Aug 12 14:29 CalculatorTest.class
-rw-rw-r-- 1 ubuntu ubuntu    468 Aug 12 13:47 CalculatorTest.java
-rw-rw-r-- 1 ubuntu ubuntu  45024 Jul  9  2012 hamcrest-core-1.3.jar
-rw-rw-r-- 1 ubuntu ubuntu 384581 Feb 13  2021 junit-4.13.2.jar
```

13\. Run the JUnit Test

Run the following command to run the **CalculatorTest** to test the program

```
java -cp .:junit-4.13.2.jar:hamcrest-core-1.3.jar org.junit.runner.JUnitCore CalculatorTest
```

**Output:**

```
ubuntu@vignesh-jenkins2:~/java$ java -cp .:junit-4.13.2.jar:hamcrest-core-1.3.jar org.junit.runner.JUnitCore CalculatorTest
JUnit version 4.13.2
..
Time: 0.018

OK (2 tests)
```

Both the test cases are passed.

You can see the **difficulties in maintaining the dependencies**. For a big project, there could be **hundreds of dependencies**, with Maven this can be easily managed.

14\. Cleanup the compiled class files and downloaded jar files

Run the following command to delete the **Calculator.class**, **CalculatorTest.class**, **junit-4.13.2.jar** and **hamcrest-core-1.3.jar**

```bash
rm -f *.class *.jar
```

Verify the files are deleted

```
ll
```

**Output:**

```
ubuntu@vignesh-jenkins2:~/java$ ll
-rw-rw-r-- 1 ubuntu ubuntu  598 Aug 12 13:14 Calculator.java
-rw-rw-r-- 1 ubuntu ubuntu  468 Aug 12 13:47 CalculatorTest.java
```

### **Java Program with Maven**

Maven expects the **Java files** to be in a **proper folder structure** with **pox.xml** in the root folder like this

```
├── pom.xml
└── src
    ├── main
    │   └── java
    │       └── Calculator.java
    └── test
        └── java
            └── CalculatorTest.java
```

1\. Create **src/main/java** folder and move **Calculator.java** into it

All **development Java files** are kept inside the **src/main/java** folder as per the Maven folder structure

Run the following command to create the **src/main/java** folder

```bash
mkdir -p src/main/java
```

Check folder is created

```bash
ll
tree
```

**Output:**

```
ubuntu@vignesh-jenkins2:~/java$ ll
-rw-rw-r-- 1 ubuntu ubuntu  598 Aug 12 13:14 Calculator.java
-rw-rw-r-- 1 ubuntu ubuntu  468 Aug 12 13:47 CalculatorTest.java
drwxrwxr-x 3 ubuntu ubuntu 4096 Aug 13 14:26 src/
```

```
ubuntu@vignesh-jenkins2:~/java$ tree
├── Calculator.java
├── CalculatorTest.java
└── src
    └── main
        └── java
```

Run the following command to move the **Calculator.java** into **src/main/java** folder

```bash
mv Calculator.java src/main/java
```

Verify **Calculator.java** file moved into **src/main/java**

```bash
tree
```

**Output:**

```
ubuntu@vignesh-jenkins2:~/java$ tree
├── CalculatorTest.java
└── src
    └── main
        └── java
            └── Calculator.java
```

2\. Create **src/test/java** folder and move **CalculatorTest.java** into it

All **Unit Test Java files** are kept inside the **src/test/java** folder as per the Maven folder structure

Run the following command to create the **src/test/java** folder

```bash
mkdir -p src/test/java
```

Check folder is created

```bash
tree
```

**Output:**

```
ubuntu@vignesh-jenkins2:~/java$ tree
├── CalculatorTest.java
└── src
    ├── main
    │   └── java
    │       └── Calculator.java
    └── test
        └── java
```

Run the following command to move the **CalculatorTest.java** into the **src/test/java** folder

```bash
mv CalculatorTest.java src/test/java
```

Verify **CalculatorTest.java** file moved into **src/test/java**

```bash
tree
```

**Output:**

```
ubuntu@vignesh-jenkins2:~/java$ tree
└── src
    ├── main
    │   └── java
    │       └── Calculator.java
    └── test
        └── java
            └── CalculatorTest.java
```

3\. Create a **pom.xml** file in the root folder

**pom.xml** file contains information about the project and configuration details used by Maven to build the project

pom.xml should be kept in the root folder

**mvn** command should be executed from where the **pom.xml** is located.

Maven **identifies** this as a **Maven project** by **identifying the pom.xml** file and its information

Create pox.xml file

```java
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.example</groupId>
    <artifactId>calculator-project</artifactId>
    <version>1.0-SNAPSHOT</version>

    <build>
      <plugins>
        <plugin>
          <artifactId>maven-compiler-plugin</artifactId>
          <version>3.12.1</version>
        </plugin>
      </plugins>
    </build>
    <dependencies>
        <!-- JUnit dependency -->
        <dependency>
            <groupId>junit</groupId>
            <artifactId>junit</artifactId>
            <version>4.13.2</version>
            <scope>test</scope>
        </dependency>
    </dependencies>
</project>
```

pox.xml has important fields like **groupId**, **artifactId,** and **version** to track the project details

Now dependencies like **JUnit** can be easily defined under the **dependency block** in pom.xml

During **compilation**, it **automatically downloads the jar files and keeps** them inside the **~/.m2** folder

One more important thing, it automatically **downloads the transitive dependency**, you do not need to define it in the pom.xml

Here **hamcrest-core-1.3.jar** is a transitive dependency for the Junit library, Maven will automatically download it

Final folder structure

```bash
tree
```

**Output:**

```
ubuntu@vignesh-jenkins2:~/java$ tree
├── pom.xml
└── src
    ├── main
    │   └── java
    │       └── Calculator.java
    └── test
        └── java
            └── CalculatorTest.java
```

4\. Compile the Java program using the Maven command

Run the following Maven command to compile the Maven project

```
mvn compile
```

Output:

```
ubuntu@vignesh-jenkins2:~/java$ mvn compile
[INFO] Scanning for projects...
[INFO] 
[INFO] -------------------< com.example:calculator-project >-------------------
[INFO] Building calculator-project 1.0-SNAPSHOT
[INFO] --------------------------------[ jar ]---------------------------------
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-resources-plugin/2.6/maven-resources-plugin-2.6.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-resources-plugin/2.6/maven-resources-plugin-2.6.pom (8.1 kB at 5.6 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-plugins/23/maven-plugins-23.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-plugins/23/maven-plugins-23.pom (9.2 kB at 67 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-parent/22/maven-parent-22.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-parent/22/maven-parent-22.pom (30 kB at 189 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/apache/11/apache-11.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/apache/11/apache-11.pom (15 kB at 95 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-resources-plugin/2.6/maven-resources-plugin-2.6.jar
```

```
Downloaded from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-compiler-javac/2.14.2/plexus-compiler-javac-2.14.2.jar (23 kB at 63 kB/s)
Downloaded from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-utils/4.0.0/plexus-utils-4.0.0.jar (192 kB at 509 kB/s)
[INFO] Recompiling the module because of changed source code.
[WARNING] File encoding has not been set, using platform encoding UTF-8, i.e. build is platform dependent!
[INFO] Compiling 1 source file with javac [debug target 1.8] to target/classes
[WARNING] bootstrap class path not set in conjunction with -source 8
[WARNING] source value 8 is obsolete and will be removed in a future release
[WARNING] target value 8 is obsolete and will be removed in a future release
[WARNING] To suppress warnings about obsolete options, use -Xlint:-options.
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time:  16.675 s
[INFO] Finished at: 2024-08-13T15:13:55Z
[INFO] ------------------------------------------------------------------------
```

It creates a class file inside the **target/classes** folder

```bash
tree
```

**Output:**

```
ubuntu@vignesh-jenkins2:~/java$ tree
├── pom.xml
├── src
│   ├── main
│   │   └── java
│   │       └── Calculator.java
│   └── test
│       └── java
│           └── CalculatorTest.java
└── target
    ├── classes
    │   └── Calculator.class
    ├── generated-sources
    │   └── annotations
    └── maven-status
        └── maven-compiler-plugin
            └── compile
                └── default-compile
                    ├── createdFiles.lst
                    └── inputFiles.lst
```

5\. Compile the Java program using the Maven command

Run the following Maven command to run the **Junit test**

```bash
mvn test
```

When you run the **mvn test**, it compiles first and then executes the Junit test cases.

**Output:**

```
ubuntu@vignesh-jenkins2:~/java$ mvn test
[INFO] Scanning for projects...
[INFO] 
[INFO] -------------------< com.example:calculator-project >-------------------
[INFO] Building calculator-project 1.0-SNAPSHOT
[INFO] --------------------------------[ jar ]---------------------------------
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-surefire-plugin/2.12.4/maven-surefire-plugin-2.12.4.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-surefire-plugin/2.12.4/maven-surefire-plugin-2.12.4.pom (10 kB at 13 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire/2.12.4/surefire-2.12.4.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire/2.12.4/surefire-2.12.4.pom (14 kB at 104 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-surefire-plugin/2.12.4/maven-surefire-plugin-2.12.4.jar
```

```
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-providers/2.12.4/surefire-providers-2.12.4.pom (2.3 kB at 20 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-junit4/2.12.4/surefire-junit4-2.12.4.jar
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-junit4/2.12.4/surefire-junit4-2.12.4.jar (37 kB at 313 kB/s)

-------------------------------------------------------
 T E S T S
-------------------------------------------------------
Running CalculatorTest
Tests run: 2, Failures: 0, Errors: 0, Skipped: 0, Time elapsed: 0.141 sec

Results :

Tests run: 2, Failures: 0, Errors: 0, Skipped: 0

[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time:  10.415 s
[INFO] Finished at: 2024-08-13T15:17:01Z
[INFO] ------------------------------------------------------------------------
```

Test class files are kept inside the **target/test-classes** folder

```
tree
```

**Output:**

```
ubuntu@vignesh-jenkins2:~/java$ tree
├── pom.xml
├── src
│   ├── main
│   │   └── java
│   │       └── Calculator.java
│   └── test
│       └── java
│           └── CalculatorTest.java
└── target
    ├── classes
    │   └── Calculator.class
    ├── generated-sources
    │   └── annotations
    ├── generated-test-sources
    │   └── test-annotations
    ├── maven-status
    │   └── maven-compiler-plugin
    │       ├── compile
    │       │   └── default-compile
    │       │       ├── createdFiles.lst
    │       │       └── inputFiles.lst
    │       └── testCompile
    │           └── default-testCompile
    │               ├── createdFiles.lst
    │               └── inputFiles.lst
    ├── surefire-reports
    │   ├── CalculatorTest.txt
    │   └── TEST-CalculatorTest.xml
    └── test-classes
        └── CalculatorTest.class
```

6\. Package the program and create a Jar file

With Maven you can package your Java program/application into a **JAR/WAR** package

**JAR** can be created and used in another Java program as a library.

Similarly, **WAR** can be created to deploy to the **Tomcat Webserver** to see your application from a Browser like **Chrome**

Add this **maven-jar-plugin** **plugin code** under the **plugins block** in the **pom.xml** to generate a **jar** file

```java
<!-- Jar plugin to specify the main class -->
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-jar-plugin</artifactId>
    <version>3.2.0</version>
    <configuration>
        <archive>
            <manifest>
                <mainClass>Calculator</mainClass>
            </manifest>
        </archive>
    </configuration>
</plugin>
```

Final pom.xml after adding the **maven-jar-plugin** **plugin**

```
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.example</groupId>
    <artifactId>calculator-project</artifactId>
    <version>1.0-SNAPSHOT</version>

    <build>
      <plugins>
        <plugin>
          <artifactId>maven-compiler-plugin</artifactId>
          <version>3.12.1</version>
        </plugin>
    
        <!-- Jar plugin to specify the main class -->
        <plugin>
          <groupId>org.apache.maven.plugins</groupId>
          <artifactId>maven-jar-plugin</artifactId>
          <version>3.2.0</version>
          <configuration>
            <archive>
              <manifest>
                <mainClass>Calculator</mainClass>
              </manifest>
            </archive>
          </configuration>
        </plugin>    
      </plugins>
    </build>
    <dependencies>
        <!-- JUnit dependency -->
        <dependency>
            <groupId>junit</groupId>
            <artifactId>junit</artifactId>
            <version>4.13.2</version>
            <scope>test</scope>
        </dependency>
    </dependencies>
</project>
```

Run the following command to create a Jar package

```bash
mvn clean package
```

When you run the **mvn clean package**, it deletes the existing target folder, compiles freshly, executes the Junit test cases, and then creates the Jar file

**Output:**

```
ubuntu@vignesh-jenkins2:~/java$ mvn clean package
[INFO] Scanning for projects...
[INFO] 
[INFO] -------------------< com.example:calculator-project >-------------------
[INFO] Building calculator-project 1.0-SNAPSHOT
[INFO] --------------------------------[ jar ]---------------------------------
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-jar-plugin/3.2.0/maven-jar-plugin-3.2.0.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-jar-plugin/3.2.0/maven-jar-plugin-3.2.0.pom (7.3 kB at 8.1 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-plugins/33/maven-plugins-33.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-plugins/33/maven-plugins-33.pom (11 kB at 75 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-jar-plugin/3.2.0/maven-jar-plugin-3.2.0.jar
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-jar-plugin/3.2.0/maven-jar-plugin-3.2.0.jar (29 kB at 188 kB/s)
```

```
[INFO] Building jar: /home/ubuntu/java/target/calculator-project-1.0-SNAPSHOT.jar
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time:  16.728 s
[INFO] Finished at: 2024-08-15T11:09:33Z
[INFO] ------------------------------------------------------------------------
```

The jar file is here **target/calculator-project-1.0-SNAPSHOT.jar**

7\. Execute the Jar file to run the Java program

Run the following command to run the program

```bash
java -jar target/calculator-project-1.0-SNAPSHOT.jar
```

Output:

```
ubuntu@vignesh-jenkins2:~/java$ java -jar target/calculator-project-1.0-SNAPSHOT.jar
Sum: 15.0
Difference: 5.0
```

Maven is very useful in the CI/CD process to automate the building of application

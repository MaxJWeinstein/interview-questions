# Results for the Software Interview Problems

# Problem - 1

## C++ Docker Image

The main issue was the filesystem. It originally dumped the _contents_ of `src` into `/usr/src`, so they were in the same directory level as the Makefile. I originally fixed it by moving the source code into `/usr/src/src`, but decided to move everything one level deeper to be less confusing. The other issue was that the final executable gets built in `target`, not the working directory.

```Dockerfile
# Get the GCC preinstalled image from Docker Hub
FROM gcc

# Specify the working directory
WORKDIR /usr/src/lru_cpp

# Copy the current folder which contains C++ source code to the Docker image under /usr/src/lru_cpp/src
COPY src src
COPY Makefile .

# Use GCC to compile the Test.cpp source file
RUN make

# Run the program output from the previous step
CMD ["target/lru_cpp"]
```

## Python Docker Image

This image was basically fine. The only adjustment I made was to specify `python3` in the command.

```Dockerfile
# Get the python3 preinstalled image from Docker Hub
FROM python:3

# Copy the source code to the destination
COPY src /usr/src/

# Specify the working directory
WORKDIR /usr/src/

# Run the program output from the previous step
CMD ["python3","__init__.py"]
```

## Java Docker Image

This Dockerfile didn't copy over the pom.xml file, and the CMD command was written incorrectly. Like the C++ image, I also changed the file structure to avoid having `/usr/src/src`.

````Dockerfile
FROM maven

# Specify the working directory
WORKDIR /usr/src/lru_java

COPY src src
COPY pom.xml .

# Use maven to package the jar assuming the tests passed
RUN mvn package

# Run the program output from the previous step
CMD ["java", "-jar", "target/lru-java-0.0.1.jar"]```
````

# Problem - 2

## C++ Build

Once the Dockerfile was fixed, I had no issues with building or running the C++ image. I actually had no other changes to make to the C++ code.

## Java Build

The POM file had a few issues:

-   A typo: `maven.jar.verison` instead of `maven.jar.version`
-   The JDK version needed to be specified
-   The maven JAR plugin configuration needed to specify the main class

The source code had these issues:

-   The main class was missing an import for `java.util.HashSet`
-   The test class was missing the `@Test` decorator over `testLRULastInsertIsHead`

## Python Run

There were no problems with running the Python files. All I had to do was finish the implementation.

# Problem - 3

-   C++ Docker Run Output

```bash

interview-questions$ docker build -t mom-edit:cpp c++
    ...
interview-questions$ docker run mom-edit:cpp
5 4 1 3

```

-   Java Docker Run Output

```bash

interview-questions$ docker build -t mom-edit:java java
    ...
interview-questions$ docker run mom-edit:java
5 4 1 3

```

-   Python Docker Run Output

```bash

interview-questions$ docker build -t mom-edit:python python
    ...
interview-questions$ docker run mom-edit:python
5 4 1 3

```

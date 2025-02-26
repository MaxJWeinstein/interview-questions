# Results for the Software Interview Problems

# Problem - 1

-   C++ Docker Image

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

-   Python Docker Image

```Dockerfile
# Get the python3 preinstalled image from Docker Hub
FROM python:3

# Copy the source code to the destination
COPY src /usr/src/

# Specify the working directory
WORKDIR /usr/src/

# Run the program output from the previous step
CMD ["python","__init__.py"]
```

-   Java Docker Image

````Dockerfile
FROM maven:3.9.9-amazoncorretto-21

# Specify the working directory
WORKDIR /usr/src/lru_java

COPY src src
COPY pom.xml .

# Use maven to package the jar assuming the tests passed
RUN mvn package -e -X

# Run the program output from the previous step
CMD ["java", "-jar", "target/lru-java-0.0.1.jar"]```

# Problem - 2

-   C++ Build

````

template - area for input

```

-   Java Build

```

template - area for input

```

-   Python Run

```

template - area for input

```

# Problem - 3

-   C++ Docker Run Output

```

template - area for input

```

-   Java Docker Run Output

```

template - area for input

```

-   Python Docker Run Output

```

template - area for input

```

```

FROM maven:3.9.9-amazoncorretto-21

# Specify the working directory
WORKDIR /usr/src/lru_java

COPY src src
COPY pom.xml .

# Use maven to package the jar assuming the tests passed
RUN mvn package -e -X

# Run the program output from the previous step
CMD ["java", "-jar", "target/lru-java-0.0.1.jar"]

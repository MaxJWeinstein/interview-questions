FROM maven:3.9.9-amazoncorretto-21

COPY src tmp/src
COPY pom.xml /tmp/pom.xml

# Specify the working directory
WORKDIR /tmp

# Use maven to package the jar assuming the tests passed
RUN mvn package -e -X

# Run the program output from the previous step
CMD ["java", "-jar", "target/lru-java-0.0.1.jar"]

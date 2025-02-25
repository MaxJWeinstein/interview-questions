# Get the GCC preinstalled image from Docker Hub
FROM gcc

# Specify the working directory
WORKDIR /usr/src/

# Copy the current folder which contains C++ source code to the Docker image under /usr/src
COPY src src
COPY Makefile Makefile

# Use GCC to compile the Test.cpp source file
RUN make

# Run the program output from the previous step
CMD ["target/lru_cpp"]

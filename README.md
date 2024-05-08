# Gem5 Docker

A Docker Container that installs all the dependencies in a Ubuntu 22.04 container and prepares the enviroment for compilation

## Usage

On a terminal type

```bash
docker build .
```

To build the Docker Image

## How to create a new container

To create a new container using this image you can use the default docker run command, but first you need to find the build ID of the image generated in the previous step. To do this type

```bash
docker image list
```

The image, currently, has a TAG of \<none\> and a Repository of \<none\>, the IMAGE ID can be found here. After that just run the docker run command 

```bash
docker run -it --name gem5 -p7000:7000 IMAGE_ID
```

Then you will have a working enviroment ready to use the Gem5
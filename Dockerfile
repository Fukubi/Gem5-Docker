FROM ubuntu:22.04

WORKDIR /gem5

RUN ln -fs /usr/share/zoneinfo/America/Recife /etc/localtime && \
    apt update -y && \
    DEBIAN_FRONTEND=noninteractive apt install -y build-essential git m4 scons zlib1g zlib1g-dev libprotobuf-dev protobuf-compiler libprotoc-dev libgoogle-perftools-dev python3-dev python3-pip libboost-all-dev pkg-config python3-tk gdb-multiarch gcc-aarch64-linux-gnu cpp-aarch64-linux-gnu libc6-dev-arm64-cross && \
    git clone https://github.com/gem5/gem5 . && \
    pip install -r requirements.txt

RUN mkdir shared

COPY . .

EXPOSE 7000/tcp

CMD ["/bin/bash"]

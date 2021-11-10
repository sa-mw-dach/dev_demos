FROM docker.io/nvidia/cuda:11.3.0-cudnn8-devel-ubi8

RUN dnf -y install python3 python3-pip
RUN dnf -y install python3-devel

ENTRYPOINT ["tail", "-f", "/dev/null"]

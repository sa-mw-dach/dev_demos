FROM centos:8

RUN dnf -y install python3

RUN dnf -y install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm
RUN dnf -y install kernel-devel-$(uname -r) kernel-headers-$(uname -r)

RUN dnf -y install dnf-plugins-core
RUN dnf -y config-manager --add-repo https://developer.download.nvidia.com/compute/cuda/repos/rhel8/x86_64/cuda-rhel8.repo
RUN dnf -y install cuda

ENTRYPOINT ["tail", "-f", "/dev/null"]

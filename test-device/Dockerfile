FROM ubuntu:22.04

RUN apt-get update && apt-get install -y openssh-server

RUN useradd -m netadmin && echo 'netadmin:netadmin123' | chpasswd

RUN sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config

RUN mkdir -p /run/sshd

RUN echo 'hostname sw1' > /home/netadmin/config.txt

CMD ["/usr/sbin/sshd", "-D"]
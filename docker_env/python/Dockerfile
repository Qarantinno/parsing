FROM phusion/baseimage:0.11

# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]

RUN apt-get update -yqq && \
    apt-get install -yqq build-essential libssl-dev libffi-dev python-dev git

RUN apt-get install -yqq python3-pip

RUN mkdir /etc/service/install_deps
COPY install_deps.sh /etc/service/install_deps/run
RUN chmod +x /etc/service/install_deps/run

COPY ./crontab /etc/crontab

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
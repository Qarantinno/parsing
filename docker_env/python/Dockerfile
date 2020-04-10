FROM phusion/baseimage:0.11

# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]

RUN apt-get update -yqq && \
    apt-get install -yqq build-essential libssl-dev libffi-dev python-dev git wget

RUN apt-get install -yqq python3-pip

RUN apt-get -yqq install software-properties-common
RUN add-apt-repository -y ppa:openjdk-r/ppa
RUN apt-get update

RUN apt-get -yqq install openjdk-8-jdk

ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64/
RUN export JAVA_HOME

RUN mkdir -p /opt \
    && wget http://dl.google.com/linux/deb/pool/main/g/google-chrome-unstable/google-chrome-unstable_78.0.3904.17-1_amd64.deb \
    && apt-get install -fyqq ./google-chrome-unstable_78.0.3904.17-1_amd64.deb

RUN mkdir -p /etc/my_init.d
COPY install_deps.sh /etc/my_init.d/050_install_deps.sh
RUN chmod +x /etc/my_init.d/050_install_deps.sh

RUN mkdir /etc/service/selenium_stanalone
COPY chrome_start.sh /etc/service/selenium_stanalone/run
RUN chmod +x /etc/service/selenium_stanalone/run

#logs of cron in tail -f /var/mail/root
RUN apt-get install -yqq postfix \
    && mkfifo /var/spool/postfix/public/pickup

COPY ./crontab /etc/crontab

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
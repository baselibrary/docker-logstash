FROM baselibrary/java:8
MAINTAINER ShawnMa <qsma@thoughtworks.com>

## Version
ENV LOGSTASH_MAJOR   2.1
ENV LOGSTASH_VERSION 1:2.1.3-1

## Repository
RUN \
  apt-key adv --keyserver keyserver.ubuntu.com --recv-keys D88E42B4 &&\
  echo "deb http://packages.elastic.co/logstash/2.1/debian stable main" > /etc/apt/sources.list.d/logstash.list

## Packages
RUN \
  apt-get update &&\
  apt-get install -y logstash=$LOGSTASH_VERSION &&\
  rm -rf /var/lib/apt/lists/*

## Environments
ENV PATH   /opt/logstash/bin:$PATH

## Scripts
ADD docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod a+x            /docker-entrypoint.sh

EXPOSE 9200 9300

ENTRYPOINT ["/docker-entrypoint.sh"]

VOLUME ["/var/lib/logstash"]

CMD ["logstash", "agent"]



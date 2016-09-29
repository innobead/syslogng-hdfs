FROM centos:centos7

RUN cd /etc/yum.repos.d; \
    curl -k -LO https://copr.fedorainfracloud.org/coprs/czanik/syslog-ng38/repo/epel-7/czanik-syslog-ng38-epel-7.repo

RUN yum install -y epel-release; \
    yum -y update; \
    yum install -y java-1.8.0-openjdk; \
    yum install -y syslog-ng syslog-ng-java; \
    yum clean all;

ADD hadoop/libs/* /opt/hadoop/libs/

ADD conf/openjdk-libjvm.conf /etc/ld.so.conf.d/openjdk-libjvm.conf
RUN ldconfig

EXPOSE 514
EXPOSE 601
EXPOSE 6514

ENTRYPOINT ["/usr/sbin/syslog-ng", "-F"]

# Syslog-ng & HDFS integration
A syslog-ng log redirects to HDFS.

## Configurations

***syslog-ng.conf***

    @version: 3.8
    @module mod-java
    @include "scl.conf"
    
    source s_syslog {
        network(
            ip("127.0.0.1")
            port(7777)
            transport("tcp")
        );
    };
    
    destination d_file {
        file("/var/log/output");
    };
    
    destination d_hdfs {
        hdfs(
            client-lib-dir("/opt/hadoop/libs")
            hdfs-uri("hdfs://hadoop:9000")
            hdfs-file("/syslog/log.txt")
        );
    };
    
    log {
        source(s_syslog);
        destination(d_file);
        destination(d_hdfs);
    };


## Usage
1. Up docker containers

> docker-compose up

2. Input message to syslog log file, to see it redirects to HDFS

> docker exec syslognghdfs_syslog_1 /bin/bash -c "send_syslog.py"
> docker exec syslognghdfs_syslog_1 /bin/bash -c "cat /var/log/output"
> docker exec syslognghdfs_hadoop_1 /usr/local/hadoop/bin/hadoop fs -cat /syslog/*

## Notes
1. Need to make sure libjvm.so existed and refresh shared lib cache
2. Need to copy hadoop common libraries (version the same from the hadoop instance) for syslog-ng hdfs plugin

> <hadoop distribution>/share/hadoop/common/*.jar including files under libs too

3. There is no syslog-ng 3.8.x available on EPEL7 repo, need to use unofficial ones mentioned in
 [syslog-ng github](https://github.com/balabit/syslog-ng)
 
4. The same HDFS libs dependency as Flum HDFS


scrbie-kafka
============
功能： 通过修改scribe源代码，充分利用scribe的高性能，和可靠性，结合librdkafka，把日志直接导入到kafk集群
优点： 能够减少日志在磁盘存放，直接导入kafka
不足： 受限librdkafka，导入速度每秒钟至少到20wmsg/s, 45M/s

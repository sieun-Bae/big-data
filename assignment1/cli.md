<h2>Connecting docker</h2>
docker ps
docker exec -it 9db318e92220 /bin/bash

<h2>HDFS 명령어 정리</h2>
https://blog.voidmainvoid.net/175
https://wikidocs.net/25326

<br>
<p>
1. Estimate minimum Namenode RAM size for HDFS with 1 PB capacity, block size 64 MB, average metadata size for each block is 300 B, replication factor is 3. Provide the formula for calculations and the result.
1PB / (64MB * 3) * 300 B = 1.56GB
</p>
<p>
2. HDDs in your cluster have the following characteristics: average reading speed is 60 MB/s, seek time is 5 ms. You want to spend 0.5 % time for seeking the block, i.e. seek time should be 200 times less than the time to read the block. Estimate the minimum block size.
block size: x
max block reading time: 5ms * 200 = 1s
reading speed: 60/1s = x/1s
x = 60MB
<br>
Check the calculations and the result, they should both be correct.

block_size / 60 MB/s * 0.5 / 100 >= 5 ms
block_size >= 60 MB/s * 0.005 s / 0.005 = 60 MB
So, the minimum block size is 60 MB or 64 MB.
</p>
<p>
To complete this task use the 'HDFS CLI Playground' or online sandbox item.

Create text file ‘test.txt’ in a local fs. Use HDFS CLI to make the following operations:

сreate directory ‘assignment1’ in your home directory in HDFS (you can use a relative path or prescribe it explicitly "/user/jovyan/...")
put test.txt in it
output the size and the owner of the file
revoke ‘read’ permission for ‘other users’
read the first 10 lines of the file
rename it to ‘test2.txt’.
Provide all the commands to HDFS CLI.

</p>
<pre><code>
hdfs dfs -mkdir /assignment1
hdfs dfs -touchz /assignment1/test.txt
hdfs dfs -put ~/test.txt /assignment1/test.txt
hdfs dfs -ls /assignment1
hdfs dfs -chmod o-r /assignment1/test.txt
hdfs dfs -mv /assignment1/test.txt /assignment1/test2.txthdfs dfs -cat /assignment1/test.txt | head -10

<br>
Check the commands, they should be like these:

$ hdfs dfs -mkdir assignment1
$ hdfs dfs -put test.txt assignment1/
$ hdfs dfs -ls assignment1/test.txt or hdfs dfs -stat "%b %u" assignment1/test.txt
$ hdfs dfs -chmod o-r assignment1/test.txt
$ hdfs dfs -cat assignment1/test.txt | head -10
$ hdfs dfs -mv assignment1/test.txt assignment1/test2.txt

There can be the following differences:

‘hdfs dfs’ and ‘hadoop fs’ are the same
absolute paths are also allowed: ‘/user/<username>/assignment1/test.txt’ instead of ‘assignment1/test.txt’
the permissions argument can be in an octal form, like 0640
the ‘text’ command can be used instead of ‘cat’


</code></pre>
Use HDFS CLI to investigate the file ‘/data/wiki/en_articles_part/articles-part’ in HDFS:

• get blocks and their locations in HDFS for this file, show the command without an output
<pre><code>
hdfs fsck /data/wiki/en_articles_part/articles-part -files -blocks -locations </code></pre>

<br>
Blocks and locations of ‘/data/wiki/en_articles_part/articles-part’:

$ hdfs fsck /data/wiki/en_articles_part/articles-part -files -blocks -locations
Block information (block id may be different):
$ hdfs fsck -blockId blk_1073971670
It outputs the block locations, example (nodes list will be different):

Block replica on datanode/rack: some_node_hostname/default-rack is HEALTHY
Connecting to namenode via http://localhost:50070/fsck?ugi=root&files=1&blocks=1&locations=1&path=%2Fdata%2Fwiki%2Fen_articles_part%2Farticles-part
FSCK started by root (auth:SIMPLE) from /127.0.0.1 for path /data/wiki/en_articles_part/articles-part at Mon Mar 01 06:25:58 GMT 2021
/data/wiki/en_articles_part/articles-part 76861985 bytes, 1 block(s):  OK
0. BP-1438385845-172.17.0.5-1601399187625:blk_1073741828_1004 len=76861985 Live_repl=1 [DatanodeInfoWithStorage[127.0.0.1:50010,DS-1ae0b599-12dc-4f10-a75e-d84f6e8a92ea,DISK]]

Status: HEALTHY
 Total size:	76861985 B
 Total dirs:	0
 Total files:	1
 Total symlinks:		0
 Total blocks (validated):	1 (avg. block size 76861985 B)
 Minimally replicated blocks:	1 (100.0 %)
 Over-replicated blocks:	0 (0.0 %)
 Under-replicated blocks:	0 (0.0 %)
 Mis-replicated blocks:		0 (0.0 %)
 Default replication factor:	1
 Average block replication:	1.0
 Corrupt blocks:		0
 Missing replicas:		0 (0.0 %)
 Number of data-nodes:		1
 Number of racks:		1
FSCK ended at Mon Mar 01 06:25:58 GMT 2021 in 9 milliseconds

The filesystem under path '/data/wiki/en_articles_part/articles-part' is HEALTHY

• get the information about any block of the file, show the command and the block locations from the output
<pre><code>
hdfs fsck /data/wiki/en_articles_part/articles-part
</code></pre>

FSCK started by root (auth:SIMPLE) from /127.0.0.1 for path /data/wiki/en_articles_part/articles-part at Mon Mar 01 06:27:24 GMT 2021
.Status: HEALTHY
 Total size:	76861985 B
 Total dirs:	0
 Total files:	1
 Total symlinks:		0
 Total blocks (validated):	1 (avg. block size 76861985 B)
 Minimally replicated blocks:	1 (100.0 %)
 Over-replicated blocks:	0 (0.0 %)
 Under-replicated blocks:	0 (0.0 %)
 Mis-replicated blocks:		0 (0.0 %)
 Default replication factor:	1
 Average block replication:	1.0
 Corrupt blocks:		0
 Missing replicas:		0 (0.0 %)
 Number of data-nodes:		1
 Number of racks:		1
FSCK ended at Mon Mar 01 06:27:24 GMT 2021 in 1 milliseconds


The filesystem under path '/data/wiki/en_articles_part/articles-part' is HEALTHY

<p>
5. Look at the picture of Namenode web interface from a real Hadoop cluster.

Show the total capacity of this HDFS installation, used space and total data nodes in the cluster.

- total capacity : 1.44 TB
- used space : 282.78 MB (0.02%)
- total datanodes : 1.44 TB

<br>
Total capacity: 2.14 TB

Used space: 242.12 GB (=DFS Used) or 242.12+35.51 = 277.63 GB (=DFS Used + Non DFS Used) - the latter answer is more precise, but the former is also possible

Data nodes in the cluster: 4
</p>
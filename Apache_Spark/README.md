# Apache Spark

- Its a unified analytic engine that allows you to process data at a huge scale in a distributed manner.

<h3> Spark Architecture </h3> 

- Driver Program
  - Hosts Spark context 
  - Separate process (JVM) 
  - Launches tasks
  - Several Services 
    - SparkEnv
    - DAGScheduler
    - TaskScheduler
    - SparkUI

- Spark Application 

 - The code that you write
 - Use SparkContext as the entry point
 - Creates the DAG
 - Internally, spark creates stages (Physical execution plan) 

- SparkSession
  - Wraps SparkContext
  - Encapsulates SparkContext, SQLContext, HiveContext...

- Cluster manager
  - Driver interact with cluster manager
  - Responsible for all of the resource allocation in spark
  - yarn, kubernetes, mesos - are all the available cluster manager in spark

- Worker 
  - Compute nodes in cluster
  - Runs the spark application code
  - Worker has executor. It consist of several task. Task is physical stage of execution.

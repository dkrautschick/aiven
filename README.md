# How to create a quick Kafka example with Aiven

This tutorial should show how to create a quick example setup for using the Kafka platform in
the Aiven Cloud offering including proper monitoring with a Grafana dashboard.

## Sign up to Aiven using the free tier offering

You can register for free on the Aiven web console and use a free tier offering which allows
to use the services for a particular time to evaluate it.

![Screenshot01](https://github.com/dkrautschick/aiven/blob/main/screenshots/AivenKafkaWalkThrough_screenshot01.jpg)

## create the relevant services

After creating your account and login you can create services.

![Screenshot02](https://github.com/dkrautschick/aiven/blob/main/screenshots/AivenKafkaWalkThrough_screenshot02.jpg)

At least create a Kafka service with a name of your choice. I recommend also to create the InfluxDB and Grafana
service immediately to integrate all of those later. 

![Screenshot03](https://github.com/dkrautschick/aiven/blob/main/screenshots/AivenKafkaWalkThrough_screenshot03.jpg)

You also have the possibility to select the cloud vendor underneath and many other settings. 
For this demo you can go with whatever you want. The setup for Grafana and InfluxDB is similar.
Choose your prefered name and go with the defaults.

![Screenshot04](https://github.com/dkrautschick/aiven/blob/main/screenshots/AivenKafkaWalkThrough_screenshot04.jpg)

Now you can observe the creation and the status of all services in the "Services" page and wait a few moments
until everything is deployed and in green status "Running" to be sure that everything is ready to go.

![Screenshot05](https://github.com/dkrautschick/aiven/blob/main/screenshots/AivenKafkaWalkThrough_screenshot05.jpg)

For the Kafka service please got to the "Topics" page and create one topic with a name of your choice.

![Screenshot07](https://github.com/dkrautschick/aiven/blob/main/screenshots/AivenKafkaWalkThrough_screenshot07.jpg)

## Use an easy example like reviewable in the attached Python script aiven.py

Now with the Kafka service and one topic in place you can send data it. As an example
you may use the included script 

https://github.com/dkrautschick/aiven/blob/main/aiven.py

For the connection you have to check out the connection data on the service page in the 
Aiven console. Additionally you have to put the encryption and certificate files to the
correct location. For this example place the certificates in the same location where 
you've saved the python script. 

Just copy the connection details in the console and download the files and store them to your
location of choice.

![Screenshot06](https://github.com/dkrautschick/aiven/blob/main/screenshots/AivenKafkaWalkThrough_screenshot06.jpg)

```
# ls -alh
total 24K
drwxrwxr-x   2 postgres postgres   75 Oct 20 00:50 .
drwx------. 35 postgres postgres 4.0K Oct 19 21:28 ..
-rwxrwxrwx   1 postgres postgres 1.6K Oct 20 10:29 aiven.py
-rwxrwxrwx   1 postgres postgres 1.6K Oct 20 00:50 ca.pem
-rwxrwxrwx   1 postgres postgres 1.6K Oct 20 00:50 service.cert
-rwxrwxrwx   1 postgres postgres 2.5K Oct 20 00:50 service.key
```

The connection information has to be inserted in the part where the Kafka connection
is initiated in the script like you can see in the code snipplet

```
#init Kafka connection 

producer = KafkaProducer(
 bootstrap_servers='<hostname>:<port>',
 security_protocol="SSL",
 ssl_cafile="./ca.pem",
 ssl_certfile="./service.cert",
 ssl_keyfile="./service.key",
```

You also have to change the name of your topic in the script. In my example the topic name
is called "dirk".

```
...
# Kafka upload 
   
   producer.send(
    'dirk',
    value=
       {
...
```

It may be necessary to add some modules depending how prepared your station is.
At least you have to install the kafka and the random module to run the script.

```
...
 # pip3 install kafka-python
 # pip3 install random-python
...
```

## Run the script on any Linux box prepared for Python

If everything is ready you can simply start the script. It will go over a loop with a bit
waiting time so that you can see and observe progress for some time.

```
# python3 aiven.py

```

## Review the results of the Kafka console

Now with some data in Kafka you can use the Kafka page to observe and review the content in the related topics
In the sidebar of the Kafka service page you can open the "Topics" page and click on the topic you've used in your script.

![Screenshot07](https://github.com/dkrautschick/aiven/blob/main/screenshots/AivenKafkaWalkThrough_screenshot07.jpg)

First you get an overview for the topic with some configuration possibilities. We are interested what is already
in the queue so we click on "Messages"

![Screenshot08](https://github.com/dkrautschick/aiven/blob/main/screenshots/AivenKafkaWalkThrough_screenshot08.jpg)

On the "Messages" page you can review the existing messages. For refreshing the view just click on "Fetch Messages"
and depending what you want to see tick "Decode from base64" to see the complete content in plain text for our example when
you tick the drop down arrow on the message.

As you can see the exmplae script is sending some messages with an unique ID, some x and y coordinates from a 
sensor and a timestamp with a date. 

![Screenshot09](https://github.com/dkrautschick/aiven/blob/main/screenshots/AivenKafkaWalkThrough_screenshot09.jpg)

So now you have now a example Kafka setup with one topic and one producer sending messages. So far so good!

## Attach a InfluxDB and Grafana service for monitoring the Kafka setup

With the Kafka setup no running we want to add some monitoring capabilites. For this we have to integrate all three
created services together in 2 steps.

First we go to the "Integrations" page of the Kafka service and select "Store Metrics" to connect the Influx database
as a time-series database storing the monitoring metrics. Just select the created service in the collection.

![Screenshot10](https://github.com/dkrautschick/aiven/blob/main/screenshots/AivenKafkaWalkThrough_screenshot10.jpg)

The second step is to open the "Integration" page from the Grafana service and add a "Grafana Metrics Dashboard"
to connect the InfluxDB as a source for the whole monitoring metric data.

![Screenshot11](https://github.com/dkrautschick/aiven/blob/main/screenshots/AivenKafkaWalkThrough_screenshot11.jpg)

## Connect to Grafana and enjoy the prepared dashboard for monitoring

After integrating all services together you can now go to the Grafana service and open the monitoring part.
The link to the Grafana platform is noted on the main page of the service. On the same page you'll also find 
the login credentials which you can easily copy to login into Grafana

![Screenshot12](https://github.com/dkrautschick/aiven/blob/main/screenshots/AivenKafkaWalkThrough_screenshot12.jpg)

After login you can simply search vor "Aiven Kaf" to quickly find the predefined Dashboard and open it. 

![Screenshot13](https://github.com/dkrautschick/aiven/blob/main/screenshots/AivenKafkaWalkThrough_screenshot13.jpg)

That will lead to a monitoring overview where you can check the environment in realtime.

![Screenshot14](https://github.com/dkrautschick/aiven/blob/main/screenshots/AivenKafkaWalkThrough_screenshot14.jpg)

That's it. Now you can observe the example objects and the behaviour of the Kafka streams and build many more scenarios
based on this foundational setup.

Have fun!

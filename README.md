# How to create a quick Kafka example with Aiven

## Sign up to Aiven using the free tier offering

![Screenshot01]((https://github.com/dkrautschick/aiven/screenshots/AivenKafkaWalkThrough_screenshot01.jpg)

## create the relevant services

![Screenshot02]((https://github.com/dkrautschick/aiven/blob/main/screenshots/AivenKafkaWalkThrough_screenshot02.jpg)
...

![Screenshot03]((https://github.com/dkrautschick/aiven/blob/main/screenshots/AivenKafkaWalkThrough_screenshot03.jpg)

![Screenshot04]((https://github.com/dkrautschick/aiven/blob/main/screenshots/AivenKafkaWalkThrough_screenshot04.jpg)

![Screenshot05]((https://github.com/dkrautschick/aiven/blob/main/screenshots/AivenKafkaWalkThrough_screenshot05.jpg)


## Take an easy example like reviewable in the attached Python script aiven.py

![Screenshot06]((https://github.com/dkrautschick/aiven/blob/main/screenshots/AivenKafkaWalkThrough_screenshot06.jpg)

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

```
 # pip3 install kafka-python
 # pip3 install random-python
```


## Run the script on any Linux box prepared for Python

```
# python3 aiven.py

```

## Review the results of the Kafka console

![Screenshot07]((https://github.com/dkrautschick/aiven/blob/main/screenshots/AivenKafkaWalkThrough_screenshot07.jpg)

![Screenshot08]((https://github.com/dkrautschick/aiven/blob/main/screenshots/AivenKafkaWalkThrough_screenshot08.jpg)

![Screenshot09]((https://github.com/dkrautschick/aiven/blob/main/screenshots/AivenKafkaWalkThrough_screenshot09.jpg)

## Attach a InfluxDB and Grafana service for monitoring the Kafka setup

![Screenshot10]((https://github.com/dkrautschick/aiven/blob/main/screenshots/AivenKafkaWalkThrough_screenshot10.jpg)

![Screenshot11]((https://github.com/dkrautschick/aiven/blob/main/screenshots/AivenKafkaWalkThrough_screenshot11.jpg)

## Connect to Grafana and enjoy the prepared dashboard for monitoring

![Screenshot12]((https://github.com/dkrautschick/aiven/blob/main/screenshots/AivenKafkaWalkThrough_screenshot12.jpg)

![Screenshot13]((https://github.com/dkrautschick/aiven/blob/main/screenshots/AivenKafkaWalkThrough_screenshot13.jpg)

![Screenshot14]((https://github.com/dkrautschick/aiven/blob/main/screenshots/AivenKafkaWalkThrough_screenshot14.jpg)

That's it. Now you can observe the example objects and the behaviour of the Kafka streams and build many more scenarios
based on this foundational setup.

Have fun!

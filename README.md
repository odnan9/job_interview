# job_interview

In order to test the script I created some log files similar to what the script is expected to process.

Using the bash script described in the question, I created another bash script to generate some random data.

Here is the test_algorithm I used:

```
#!/bin/bash

for s in $(seq 0 10000); do
	printf "%d,%d.%02d,%d.%02d,%d.%02d,%d.%02d\n" $(( ( RANDOM % 10000000 )  + 1 )) $(( ( RANDOM % 100 )  + 1 )) $(( ( RANDOM % 99 )  + 1 ))  $(( ( RANDOM % 100 )  + 1 )) $(( ( RANDOM % 99 )  + 1 ))  $(( ( RANDOM % 100 )  + 1 )) $(( ( RANDOM % 99 )  + 1 ))  $(( ( RANDOM % 100 )  + 1 )) $(( ( RANDOM % 99 )  + 1 ))
done
```


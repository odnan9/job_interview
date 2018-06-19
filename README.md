# job_interview


In order to test the script I follow did two different tests.

## First test
Some log files where created in order to used them with the script. The expected result of the process is know for different  different values to the percentage so we know if the script is processing the logs correctly or not.

## Second test
More log files similar to what the script is expected to process where created using the bash script described in the question and the script test_algorithm was created to generate some random data to test that the script is able to handle bigger amount of data.

Here is the test_algorithm I used:
```
#!/bin/bash

for s in $(seq 0 10000); do
	printf "%d,%d.%02d,%d.%02d,%d.%02d,%d.%02d\n" $(( ( RANDOM % 10000000 )  + 1 )) $(( ( RANDOM % 100 )  + 1 )) $(( ( RANDOM % 99 )  + 1 ))  $(( ( RANDOM % 100 )  + 1 )) $(( ( RANDOM % 99 )  + 1 ))  $(( ( RANDOM % 100 )  + 1 )) $(( ( RANDOM % 99 )  + 1 ))  $(( ( RANDOM % 100 )  + 1 )) $(( ( RANDOM % 99 )  + 1 ))
done
```

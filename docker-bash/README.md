This is a simple bash script that kills the process (if any) running on port.

When I have multiple Docker projects running in my machine, sometimes it gets messy with the ports being used by the 
databases, web services, queues, etc.

When I can't start e.g Kapacitor because of its port being already in use, I usually run:
```bash
sudo netstat -nlp | grep :9092
tcp6       0      0 :::9092                 :::*                    LISTEN      1271/kapacitord   
```
And then
```bash
sudo kill -9 1271
```

The following script tries to simplify this by running it in a single command. It also supports receiving a list of 
ports as input, and it will try to kill all processes running on them.


## Usage ##

First time, you will need to give execution permissions to the script with `chmod`.
Then, launch the program with the port numbers, e.g `5432` and `9092` to kill the processes running a Postgres database 
and Kapacitor respectively on these ports (you will be asked to input your sudo password).

```bash
chmod u+x kill_ps_on_port.sh
./kill_ps_on_port.sh 5432 9092
```

Another option is to copy the content of the script inside a function in your `~/.bashrc` file:
```bash
kill_ps_on_port () {
for arg in "$@"
do
    proc=$(sudo lsof -t -i:$arg)
    if [ -z "$proc" ]
    then
        echo "No process found using port $arg"
    else
        echo "Killing process $proc"
        k=$(sudo kill -9 $proc)
        ret_code=$?
        if [ $ret_code != 0 ]
        then
            echo "Can't kill process"
        fi
    fi
done
}
```

And then you can use it from your command line calling the function's name:
```bash
source ~/.bashrc    # only the first time
kill_ps_on_port 5432 9092
```

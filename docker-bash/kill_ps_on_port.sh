for port in "$@"
do
    procs=$(sudo lsof -t -i:$port)
	if [ -z "$procs" ]
    then
	    echo "No process found using port $port"
    else
        for proc in $procs
        do
            echo "Process $proc using port $port"
            echo "Killing process $proc"
            k=$(sudo kill -9 $proc)
            ret_code=$?
            if [ $ret_code != 0 ]
            then
                echo "Can't kill process"
            fi
        done
    fi
done

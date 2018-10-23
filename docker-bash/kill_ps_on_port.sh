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
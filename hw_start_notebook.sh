#. /usr/local/Ascend/ascend-toolkit/set_env.sh
#export PYTHONPATH=/usr/local/Ascend/thirdpart/aarch64/acllite:$PYTHONPATH

if [ $# -eq 1 ];then
    jupyter lab --ip $1 --allow-root --no-browser
else
    jupyter lab --ip 192.168.31.160 --allow-root --no-browser
fi


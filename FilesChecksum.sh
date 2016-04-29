# !/bin/bash

if [ $# != 1 ];then
    echo "Need one parameter: Input dir"
    exit -1
fi

inputdir=$1
if [ ! -d ${inputdir} ]; then
    echo "Input dir is invalid"
    exit -1
fi

allFiles=$(ls -rt ${inputdir})
#echo ${allFiles}
for file in ${allFiles}
do
    file=${inputdir}\/${file}
   ./FileChecksum $file
done

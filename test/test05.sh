echo 'test s with any non-whitespace character may be used to delimit a substitute command'

echo "testcase: seq 1 5 | python3 ../slippy.py 'sX[15]XzzzX'"
value=`seq 1 5 | python3 ../slippy.py 'sX[15]XzzzX'`
res=$?
true=`seq 1 5 | sed -E 'sX[15]XzzzX'`

if [[ $value == $true ]];then
    echo 'Success! output:' $true
else
    echo 'Wrong! Your Output: '
    echo $value
    echo 'Expected Output: '
    echo $true    
fi

echo "testcase: seq 1 5 | python3 ../slippy.py 's?[15]?zzz?'"
value=`seq 1 5 | python3 ../slippy.py 's?[15]?zzz?'`
res=$?
true=`seq 1 5 | sed -E 's?[15]?zzz?'`

if [[ $value == $true ]];then
    echo 'Success! output:' $true
else
    echo 'Wrong! Your Output: '
    echo $value
    echo 'Expected Output: '
    echo $true    
fi


echo "testcase: seq 1 5 | python3 ../slippy.py 'sX[15]Xz/z/zX'"
value=`seq 1 5 | python3 ../slippy.py 'sX[15]Xz/z/zX'`
res=$?
true=`seq 1 5 | sed -E 'sX[15]Xz/z/zX'`

if [[ $value == $true ]];then
    echo 'Success! output:' $true
else
    echo 'Wrong! Your Output: '
    echo $value
    echo 'Expected Output: '
    echo $true    
fi
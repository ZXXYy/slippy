echo 'test p'

echo 'testcase: seq 65 85 | python3 ../slippy.py '/^7/p''
value=`seq 65 85 | python3 ../slippy.py '/^7/p'`
res=$?
true=`seq 65 85 | sed -E '/^7/p'`

if [[ $value == $true ]];then
    echo 'Success! output:' $true
else
    echo 'Wrong! Your Output: '
    echo $value
    echo 'Expected Output: '
    echo $true    
fi

echo 'testcase: seq 1 5 | python3 ../slippy.py 'p''
value=`seq 1 5 | python3 ../slippy.py 'p'`
res=$?
true=`seq 1 5 | sed -E 'p'`

if [[ $value == $true ]];then
    echo 'Success! output:' $true
    exit 0
else
    echo 'Wrong! Your Output: '
    echo $value
    echo 'Expected Output: '
    echo $true    
    exit 1
fi
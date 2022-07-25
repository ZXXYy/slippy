echo 'test d'

echo "testcase: seq 11 20 | python3 ../slippy.py '/[1357]/d'"
value=`seq 11 20 | python3 ../slippy.py '/[1357]/d'`
res=$?
true=`seq 11 20 | sed -E '/[1357]/d'`

if [[ $value == $true ]];then
    echo 'Success! output:' $true
else
    echo 'Wrong! Your Output: '
    echo $value
    echo 'Expected Output: '
    echo $true    
fi

echo "testcase: seq 1 100 | python3 ../slippy.py '/.{2}/d'"
value=`seq 1 100 | python3 ../slippy.py '/.{2}/d'`
res=$?
true=`seq 1 100 | sed -E '/.{2}/d'`

if [[ $value == $true ]];then
    echo 'Success! output:' $true
else
    echo 'Wrong! Your Output: '
    echo $value
    echo 'Expected Output: '
    echo $true    
fi

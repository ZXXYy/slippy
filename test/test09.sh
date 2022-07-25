echo "test branch append change insert"
echo "testcase: seq 5 9 | python3 ../slippy.py '3a hello'"
value=`seq 5 9 | python3 ../slippy.py '3a hello'`
res=$?
true=`seq 5 9 | sed - E '3a hello'`

if [[ $value == $true ]];then
    echo 'Success! output:' $true
else
    echo 'Wrong! Your Output: '
    echo $value
    echo 'Expected Output: '
    echo $true    
fi
echo "testcase: seq 5 9 | python3 ../slippy.py '3c hello'"
value=`seq 5 9 | python3 ../slippy.py '3c hello'`
res=$?
true=`seq 5 9 | sed - E '3c hello'`

if [[ $value == $true ]];then
    echo 'Success! output:' $true
else
    echo 'Wrong! Your Output: '
    echo $value
    echo 'Expected Output: '
    echo $true    
fi
echo "testcase: seq 5 9 | python3 ../slippy.py '3i hello'"
value=`seq 5 9 | python3 ../slippy.py '3i hello'`
res=$?
true=`seq 5 9 | sed - E '3i hello'`

if [[ $value == $true ]];then
    echo 'Success! output:' $true
else
    echo 'Wrong! Your Output: '
    echo $value
    echo 'Expected Output: '
    echo $true    
fi

echo 'test multi commands'

echo "testcase: seq 1 5 | python3 ../slippy.py '4q;/2/d'"
value=`seq 1 5 | python3 ../slippy.py '4q;/2/d'`
res=$?
true=`seq 1 5 | sed -E '4q;/2/d'`

if [[ $value == $true ]];then
    echo 'Success! output:' $true
else
    echo 'Wrong! Your Output: '
    echo $value
    echo 'Expected Output: '
    echo $true    
fi

echo "testcase: seq 1 20 | python3 ../slippy.py '/2$/,/8$/d;4,6p'"
value=`seq 1 20 | python3 ../slippy.py '/2$/,/8$/d;4,6p'`
res=$?
true=`seq 1 20 | sed -E '/2$/,/8$/d;4,6p'`

if [[ $value == $true ]];then
    echo 'Success! output:' $true
else
    echo 'Wrong! Your Output: '
    echo $value
    echo 'Expected Output: '
    echo $true    
fi


echo "testcase: seq 1 5 | python3 ../slippy.py '4q\n/2/d'"
value=`seq 1 5 | python3 ../slippy.py '4q
/2/d'`
res=$?
true=`seq 1 5 | sed -E '4q
/2/d'`

if [[ $value == $true ]];then
    echo 'Success! output:' $true
else
    echo 'Wrong! Your Output: '
    echo $value
    echo 'Expected Output: '
    echo $true    
fi
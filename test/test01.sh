echo 'test q'

echo 'testcase: seq 1 5 | python3 ../slippy.py '3q''
value=`seq 1 5 | python3 ../slippy.py '3q'`
res=$?
true=`seq 1 5 | sed '3q'`

if [[ $value == $true ]];then
    echo 'Success! output:' $true
else
    echo 'Wrong! Your Output: '
    echo $value
    echo 'Expected Output: '
    echo $true    
fi

echo 'testcase: seq 500 600 | python3 ../slippy.py '/^.+5$/q''
value=`seq 500 600 | python3 ../slippy.py '/^.+5$/q'`
res=$?
true=`seq 500 600 | sed -E '/^.+5$/q'`

if [[ $value == $true ]];then
    echo 'Success! output:' $true
else
    echo 'Wrong! Your Output: '
    echo $value
    echo 'Expected Output: '
    echo $true    
fi

echo 'testcase: seq 100 1000 | ../slippy.py  '/1{3}/q''
value=`seq 100 1000 | python3 ../slippy.py '/^.+5$/q'`
res=$?
true=`seq 100 1000 | sed -E '/^.+5$/q'`

if [[ $value == $true ]];then
    echo 'Success! output:' $true
else
    echo 'Wrong! Your Output: '
    echo $value
    echo 'Expected Output: '
    echo $true 
fi

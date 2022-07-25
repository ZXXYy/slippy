echo 'test address'

echo 'test one address'
echo 'testcase: seq 1 5 | python3 ../slippy.py '3d''
value=`seq 1 5 | python3 ../slippy.py '3d'`
res=$?
true=`seq 1 5 | sed '3d'`

if [[ $value == $true ]];then
    echo 'Success! output:' $true
else
    echo 'wrong! Your Output: '
    echo $value
    echo 'Expected Output: '
    echo $true    
fi

echo 'test two address'
echo 'testcase: seq 1 5 | python3 ../slippy.py '2,4d''
value=`seq 1 5 | python3 ../slippy.py '3d'`
res=$?
true=`seq 1 5 | sed '3d'`

if [[ $value == $true ]];then
    echo 'Success! output:' $true
else
    echo 'wrong! Your Output: '
    echo $value
    echo 'Expected Output: '
    echo $true    
fi

echo 'test 0 address'
echo 'testcase: seq 1 5 | python3 ../slippy.py 's/[1]/zzz/''
value=`seq 1 5 | python3 ../slippy.py 's/[1]/zzz/'`
res=$?
true=`seq 1 5 | sed 's/[1]/zzz/'`

if [[ $value == $true ]];then
    echo 'Success! output:' $true
else
    echo 'wrong! Your Output: '
    echo $value
    echo 'Expected Output: '
    echo $true    
fi

echo "test '$' address"
echo "testcase: seq 1 5 | python3 ../slippy.py '$d'"
value=`seq 1 5 | python3 ../slippy.py '$d'`
res=$?
true=`seq 1 5 | sed -E '$d'`

if [[ $value == $true ]];then
    echo 'Success! output:' $true
else
    echo 'wrong! Your Output: '
    echo $value
    echo 'Expected Output: '
    echo $true    
fi


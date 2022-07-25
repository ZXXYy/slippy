echo 'test s'

echo "testcase: seq 1 5 | python3 ../slippy.py 's/[15]/zzz/'"
value=`seq 1 5 | python3 ../slippy.py 's/[15]/zzz/'`
res=$?
true=`seq 1 5 | sed -E 's/[15]/zzz/'`

if [[ $value == $true ]];then
    echo 'Success! output:' $true
else
    echo 'Wrong! Your Output: '
    echo $value
    echo 'Expected Output: '
    echo $true    
fi

echo "testcase: echo Hello Andrew | python3 ../slippy.py 's/e//g'"
value=`echo Hello Andrew | python3 ../slippy.py 's/e//g'`
res=$?
true=`echo Hello Andrew | sed -E 's/e//g'`

if [[ $value == $true ]];then
    echo 'Success! output:' $true
else
    echo 'Wrong! Your Output: '
    echo $value
    echo 'Expected Output: '
    echo $true    
fi


echo "testcase: seq 51 60 | python3 ../slippy.py '5s/5/9/g'"
value=`seq 51 60 | python3 ../slippy.py '5s/5/9/g'`
res=$?
true=`seq 51 60 | sed -E '5s/5/9/g'`

if [[ $value == $true ]];then
    echo 'Success! output:' $true
else
    echo 'Wrong! Your Output: '
    echo $value
    echo 'Expected Output: '
    echo $true    
fi
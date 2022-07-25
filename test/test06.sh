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

echo "testcase: echo 'Punctuation characters include . , ; :' | python3 ../slippy.py 's/;/semicolon/g;/;/q'"
value=`echo 'Punctuation characters include . , ; :' | python3 ../slippy.py 's/;/semicolon/g;/;/q'`
res=$?
true=`echo 'Punctuation characters include . , ; :' | sed -E 's/;/semicolon/g;/;/q'`

if [[ $value == $true ]];then
    echo 'Success! output:' $true
else
    echo 'Wrong! Your Output: '
    echo $value
    echo 'Expected Output: '
    echo $true    
fi
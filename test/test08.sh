echo 'test comments and space'

echo "testcase: seq 24 43 | python3 ../slippy.py ' 3, 17  d  # comment'"
value=`seq 24 43 | python3 ../slippy.py ' 3, 17  d  # comment'`
res=$?
true=`seq 24 43 | sed -E ' 3, 17  d  '`

if [[ $value == $true ]];then
    echo 'Success! output:' $true
else
    echo 'Wrong! Your Output: '
    echo $value
    echo 'Expected Output: '
    echo $true    
fi


echo "testcase: seq 24 43 | python3 ../slippy.py '/2/d # delete  ;  4  q # quit'"
value=`seq 24 43 | python3 ../slippy.py '/2/d # delete  ;  4  q # quit'`
res=$?
true=`seq 24 43 | sed -E '/2/d ;  4  q'`

if [[ $value == $true ]];then
    echo 'Success! output:' $true
else
    echo 'Wrong! Your Output: '
    echo $value
    echo 'Expected Output: '
    echo $true    
fi

# echo "testcase: seq 1 5 | python3 ../slippy.py '4q\n/2/d'"
# value=`seq 1 5 | python3 ../slippy.py '4q
# /2/d'`
# res=$?
# true=`seq 1 5 | sed -E '4q
# /2/d'`

# if [[ $value == $true ]];then
#     echo 'Success! output:' $true
# else
#     echo 'Wrong! Your Output: '
#     echo $value
#     echo 'Expected Output: '
#     echo $true    
# fi
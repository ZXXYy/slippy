echo 'test -f command line option'

echo "testcase: echo /2/d >> commands.slippy; seq 1 5 | python3 ../slippy.py -f commands.slippy"
value=`echo /2/d >> commands.slippy; seq 1 5 | python3 ../slippy.py -f commands.slippy`
res=$?
true=`seq 1 5 | sed -f commands.slippy`

if [[ $value == $true ]];then
    echo 'Success! output:' $true
else
    echo 'Wrong! Your Output: '
    echo $value
    echo 'Expected Output: '
    echo $true    
fi
rm commands.slippy


echo "testcase: seq 1 2 > two.txt;seq 1 5 > five.txt;python3 ../slippy.py '4q;/2/d' two.txt five.txt"
value=`seq 1 2 > two.txt;seq 1 5 > five.txt;python3 ../slippy.py '4q;/2/d' two.txt five.txt`
res=$?
true=`sed '4q;/2/d'  two.txt five.txt`

if [[ $value == $true ]];then
    echo 'Success! output:' $true
else
    echo 'Wrong! Your Output: '
    echo $value
    echo 'Expected Output: '
    echo $true    
fi
rm *.txt

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
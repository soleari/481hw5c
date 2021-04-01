#!/bin/bash

#compute line coverage of the entire test suite : 37.97%

#run given subset of test-suite

for i in $* ; do
    pngFile="large-png-suite/"$i".png"
    echo $pngFile
    ./pngtest $pngFile
done

#compute line covereage of that subset and ouput to text file
gcov *.c > output.txt

#find if line coverage from text file
    #tail -f output.txt | grep "37.97%"
#if line coverage == $ORIGCOV --> is interestng , exit 1
#if line coverage != $ORIGCOV --> not interesting , exit 0

if [ tail -f output.txt | grep "37.97%"] ; then #FOUND SAME COVERAGE - INTERESTING
    rm *.gcda pngout.png
    exit 1
fi

#ELSE - NOT INTERSTING
rm *.gcda pngout.png
exit 0

#remove gcov before each exit
# rm *.gcda pngout.png





#python3 delta.py 1639 ./is-same-cov.sh
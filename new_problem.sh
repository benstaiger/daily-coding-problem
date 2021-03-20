#!/bin/bash

# if python
if [ "$1" == "python" ]
then
    OUTPDIR=problem_$2
    cp -r python-template $OUTPDIR 
    mv $OUTPDIR/impl.py $OUTPDIR/problem_$2.py
    mv $OUTPDIR/tests/test_example.py $OUTPDIR/tests/test_problem$2.py
fi

# if cpp
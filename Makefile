sample.pdf:sample.dat
    python sample.py
    
sample.dat:
    c++ -o samp sample.c
    ./samp 1 1 1 >sample.dat
    
   
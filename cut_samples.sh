
FILES="data/A_tests_down_1/"
for file in $FILES*; do
    python2 plot.py $file 1
done
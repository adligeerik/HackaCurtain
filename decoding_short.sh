
FILES="data/A_tests_down_1/"
for file in $FILES*_short.dat; do
    python2 decode_man.py $file
done
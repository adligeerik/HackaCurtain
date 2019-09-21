
FILES="data/B_up_down/"
for file in $FILES*_short.dat; do
    python2 decode_man.py $file
done
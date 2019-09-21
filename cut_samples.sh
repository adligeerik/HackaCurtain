
FILES="data/B_up_down/"
for file in $FILES*; do
    echo $file
    python2 plot.py $file 
done
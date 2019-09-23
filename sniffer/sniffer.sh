
while true; do
    sleep 1
    for file in data/*.dat; do
        echo "$file"
        python2 ../decode_man.py $file >> "log.txt" 
        rm $file
    done
done
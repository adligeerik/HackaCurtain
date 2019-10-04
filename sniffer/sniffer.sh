
while true; do
    sleep 1
    for file in *.dat; do
        echo "$file"
        python2 ../decode_man.py  $file 1 #>> "log.txt" 
        #rm $file
    done
done

# Failinimi: generate_data.sh
# Kirjeldus: Käivitab generate_data.py 10 korda ja salvestab andmed data kausta .txt failidesse
# Autor: Taissija Rychkova

x=1
while [ "$x" -le 10 ]
do
	python3 generate_data.py > ../data/data${x}.txt
	x=$((x+1))
done

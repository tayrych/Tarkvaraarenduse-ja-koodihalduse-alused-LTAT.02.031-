## Bash eksperiment

Selle eksperimendi käigus testisin töötamist git bashˇis ja baaskäsude kasutamist

### Kasutatud käsud:
1:
cd ja gitclone -  direktooriumi loomiseks ja Git repo arvutisse allalaadimiseks

2:
git branch -  kontrollisin, mis harud on repos olemas
git checkout -b bash_eksperiment - lõin uue haru nimega bash_eksperiment
mkdir bash_eksperiment - lõin kausta bash_eksperiment

3:
cd bash_eksperiment/ - läksin üle bash_eksperiment kausta
mkdir data scripts results - lõin kolm alamkataloogi
touch readme.md - lõin tühja readme faili

4:
touch scripts/generate_data.py - lõin pythoni koodi faili
nano scripts/generate_data.py - kirjutasin nano editoris koodi faili sisse. Siis salvestasin ctrl+O ja exit ctrl+X

5:
touch scripts/generate_data.sh - lõin sh koodi faili 

(koodis kasutatud asjad : 
-le - less or equal
while sth; do - tsükli loomine)

6:
cat data/*.txt | sort -n | uniq -c > results/summary_total_unique_numbers_counted.txt - tegin kõigist saadud andmefailist
üks üldine fail | sorteerisin numbreid (-n) | filtreerisin duplikaadid ja arvutasin unikaalsete arvude esinemist (-c) -> 
salvestasin tulemust faili kaustat results/

7:
nano readme.md - teen praegu kirjutamas 

8: 
cd .. - l'ksin bash_eksperiment kaustast v'lja 
echo "bash_eksperiment/data/" >> .gitignore
echo "bash_eksperiment/results/" >> .gitignore  - Muutsin .gitignore faili, et jätta data ja results kataloogid git 
jälgimisest välja

git add . - lisasin kõik tehtud muudatused staging area-le
git commit -m "Valmis bash_eksperiment" - salvestasin muudatusi kohalikult
git push origin bash_eksperiment - laadisin muudatusi serverile üles



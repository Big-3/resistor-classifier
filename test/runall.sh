FILES=$(pwd);

for entry in "$FILES"/test*
do
	echo "running test $entry"
	python $entry
done
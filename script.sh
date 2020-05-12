s1=$(git status -uno | awk '/is/ {print $4}')

if [ "$s1" == "up-to-date" ]
then
  echo "App Up to Date"
  exit 0
else
  echo "App needs update"
fi

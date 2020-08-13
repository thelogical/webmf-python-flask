cd /usr/src/app
rm -rf test-results
python test.py > /dev/null
if python test_reports.py; then
    exit 0
else
    exit $?
fi

cd /usr/src/app
rm -rf test-results
python test.py > /dev/null
python test_reports.py

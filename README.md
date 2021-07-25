# problema_uno

curl -i -X POST -F "name=@sample.csv" -F "date=2021-07-21" localhost:8000/api/upload
curl -i -X GET localhost:8000/api/files
curl -i -X GET localhost:8000/api/data

python3 manage.py runscript db_empty
python3 manage.py runscript data_load
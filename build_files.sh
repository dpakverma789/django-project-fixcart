echo "======> INSTALLING REQUIREMENTS <======"
pip install -r requirements.txt --break-system-packages

echo "======> COLLECTING STATIC FILES <======"
python3.12 manage.py collectstatic --noinput

echo "======> APPLYING MIGRATIONS <======"
python3.12 manage.py migrate --noinput
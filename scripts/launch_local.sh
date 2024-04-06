cd frontend
npm run build
cp -a build/ ../backend/static
cd ../backend
python app.py

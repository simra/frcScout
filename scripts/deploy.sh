if ! command -v npm &> /dev/null
then
    echo "npm could not be found"
    echo "Installing npm..."
    apt-get update
    apt-get install -y nodejs npm
fi

echo "Using npm version: $(npm -v)"
echo "Using node version: $(node -v)"

echo "Python dependencies..."
cat requirements.txt

cd backend
rm -rf static/build
cd ../frontend
npm install
npm run build
cp -a build/ ../backend/static

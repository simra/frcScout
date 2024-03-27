if ! command -v npm &> /dev/null
then
    echo "npm could not be found"
    echo "Installing npm..."
    sudo apt-get update
    sudo apt-get install -y nodejs npm
fi

if ! command -v pip &> /dev/null
then
    echo "pip could not be found"
    echo "Installing pip..."
    sudo apt-get update
    sudo apt-get install -y python3-pip
fi

echo "Using npm version: $(npm -v)"
echo "Using node version: $(node -v)"

cd backend
pip install -r requirements.txt
rm -rf static/build
cd ../frontend
npm install
npm run build
cp -a build/ ../backend/static

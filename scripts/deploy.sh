if ! command -v npm &> /dev/null
then
    echo "npm could not be found"
    echo "Installing npm..."
    sudo apt-get update
    sudo apt-get install -y nodejs npm
fi

cd backend
pip install -r requirements.txt
rm -rf static/build
cd ../frontend
npm install
npm run build
cp -a build/ ../backend/static

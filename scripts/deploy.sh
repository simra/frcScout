if ! command -v npm &> /dev/null
then
    echo "npm could not be found"
    echo "Installing npm..."
    apt-get update
    apt-get install -y nodejs npm
fi

echo "Using npm version: $(npm -v)"
echo "Using node version: $(node -v)"

cd backend
rm -rf static/build
cd ../frontend
npm install
npm run build
cp -a build/ ../backend/static
cd ..

# create a deployment branch and commit the build
git checkout -b deploy
git pull azure main
# recursively add all the contents of backend/static/build
git add -f backend/static/build
git commit -m "Deploying build to Azure"
git push azure deploy:main
git checkout main
git branch -D deploy

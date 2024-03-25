# FRC Bracket Simulator

## Local development:
The flask back end is in `backend/`, ReactTS front end in `frontend/`.  To launch it for local debugging, run `. scripts/launch_local.sh` and navigate to `http://localhost:3000/`.

You will need to set up a .env file like so:
```
DATA_FOLDER=./data
TBA_API_KEY=<a blue alliance API key>
REACT_APP_API_BASE_URL=/
```
*Note:* If you build for deployment the build folder will be in static/build and navigating to `http://localhost:5000` will render this build. If you are editing for local development use port 3000 or you won't see your changes.

## Report Generation
Model generation is in `backend/OPR.py`.  See `scripts/runScoutingReport` for an example of how it's used.  runScoutingReport needs updating to latest TBA.py API.


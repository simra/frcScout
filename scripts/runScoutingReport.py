import os
import sys
sys.path.append('./backend/')
from OPR import OPR
from TBA import TBA
import pickle
import os
import logging

DATA_FOLDER = 'backend/data'
os.environ['DATA_FOLDER'] = DATA_FOLDER
tba = TBA(year=2024, district='pnw')
all_matches = tba.matches
models = {}
opr = None

def create_model(district, event, match_type, force_recompute=False):
    '''
    district: string, the district to filter by. eg 'pnw', 'all' for all districts
    event: string, the event to filter by. eg. '2024wasno', 'all' for all events
    match_type: string, the match type to filter by. eg. 'qm', 'all' for all match types
    force_recompute: bool, if True, recompute the model even if it already exists
    '''

    model_key=f'{district}_{event}_{match_type}'
    model_fn = f'{DATA_FOLDER}/model_{model_key}.pkl'
  
    if not os.path.exists(model_fn) or force_recompute or all_matches['last_modified'] > os.stat(model_fn).st_mtime:
        selected_district = [m.key for m in all_matches['events']] if district == 'all' else \
            [m.key for m in all_matches['events'] if m.district and m.district.abbreviation==district]
        
        print(f'{len(all_matches["matches"])} events')

        data = [m for k in all_matches['matches'] for m in all_matches['matches'][k]]
        data = [m for m in data if m.winning_alliance!='' and m.score_breakdown is not None]
        print(f'Found {len(data)} matches')

        def in_scope(m):
            return ((event == 'all' and m.event_key in selected_district) \
                or (m.event_key == event)) \
                    and (match_type == 'all' or m.comp_level == match_type)

        selected_matches = list(filter(in_scope, data))

        teams = set()
        for m in selected_matches:
            for t in m.alliances.red.team_keys:
                teams.add(t)
            for t in m.alliances.blue.team_keys:
                teams.add(t)

        teams = list(sorted(teams))
        logging.debug('Teams: %s', len(teams))
        
        opr = OPR(selected_matches, teams)
        opr.data_timestamp = all_matches['last_modified']
        logging.debug('Saving %s', model_fn)
        with open(model_fn, 'wb') as f:
            pickle.dump(opr, f)

    with open(model_fn, 'rb') as f:
        logging.debug('Loading %s', model_fn)
        models[model_key] = pickle.load(f)

def get_model(model_key):
    if model_key not in models:
        create_model(*model_key.split('_'))
    assert model_key in models
    return models[model_key]


def runScoutingReport(event_key):
    opr = get_model('pnw_all_all')
    
    event_teams = tba.fetch_event_teams(event_key)

    for t in event_teams:
        o = opr.opr_lookup[t.key]
        output = (t.team_number, t.nickname, o['opr']['mu'], o['opr']['sigma'], o['dpr']['mu'], o['dpr']['sigma'], o['tpr']['mu'], o['tpr']['sigma'])
        print(','.join(map(str, output)))

runScoutingReport('2024pncmp')
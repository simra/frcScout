import React, { useState, useEffect } from 'react';
import { DragDropContext } from 'react-beautiful-dnd';
import Select from 'react-select';
import EventForm from './EventForm';
import { Team } from '../types/TeamTypes';
import AllianceSlot from './AllianceSlot';
import RatingsView from './RatingsView';
import TeamList from './TeamList';
import SingleMatchSimulator from './SingleMatchSimulator';

function AllianceComponent() {
  const [district, setDistrict] = useState(localStorage.getItem('district') || '');
  const [modelEvent, setModelEvent] = useState(localStorage.getItem('modelEvent') || '');
  const [matchType, setMatchType] = useState(localStorage.getItem('matchType') || '');
  const [density, setDensity] = useState<{ [key: number]: { [key: string]: number } }>({});
  const [overall, setOverall] = useState<{ [key: string]: number }>({});
  const [alliance1, setAlliance1] = useState('');
  const [alliance2, setAlliance2] = useState('');
  const [modelMethod, setModelMethod] = useState('opr');
  const [bracketMethod, setBracketMethod] = useState('opr');
  const [spread, setSpread] = useState<number | null>(null);
  const [sigma, setSigma] = useState<number | null>(null);
  const [pRed, setPRed] = useState<number | null>(null);

  const [leftTeams, setLeftTeams] = useState<Team[]>(
    () => {
      const savedTeams = localStorage.getItem('teams');
      return savedTeams ? JSON.parse(savedTeams) : [];
    }
  );
  const [allTeams, setAllTeams] = useState<Team[]>(() => {
    const savedTeams = localStorage.getItem('allteams');
    return savedTeams ? JSON.parse(savedTeams) : [];
  }
  );

  // we will move these to a separate component
  const [slots, setSlots] = useState<Array<Array<{ team: Team | null }>>>(() => {
    const savedSlots = localStorage.getItem('slots');
    return savedSlots ? JSON.parse(savedSlots) : Array.from({ length: 8 }, () => [{ team: null }, { team: null }, { team: null }]);
  });

  useEffect(() => {
    localStorage.setItem('teams', JSON.stringify(leftTeams));
    localStorage.setItem('allteams', JSON.stringify(allTeams));
    localStorage.setItem('district', district);
    localStorage.setItem('modelEvent', modelEvent);
    localStorage.setItem('matchType', matchType);
    localStorage.setItem('slots', JSON.stringify(slots));
  }, [leftTeams, district, modelEvent, matchType, slots, allTeams]);

  const handleTeamsUpdate = (district: string, model_event: string, match_type: string, teams: Team[]) => {
    setLeftTeams(teams);
    setAllTeams(teams);
    setDistrict(district);
    setModelEvent(model_event);
    setMatchType(match_type);
  };

  const handlePropUpdate = (district: string, model_event: string, match_type: string) => {
    setDistrict(district);
    setModelEvent(model_event);
    setMatchType(match_type);
  }

  const clearBrackets = () => {
    setSlots(Array.from({ length: 8 }, () => [{ team: null }, { team: null }, { team: null }]));
    setOverall({});
  }

  const updateBrackets = () => {
    // map slots to a json payload formatted {A1: [team1, team2, team3], A2: [team4, team5, team6], ...}
    var payload = slots.reduce<{ [key: string]: string[] }>((acc, alliance, index) => {
      acc['A' + (index + 1)] = alliance.map(slot => slot.team ? slot.team.team : '');
      return acc;
    }, {});
    console.log(payload);
    // POST alliances to /model/district_model_event_match_type/bracket
    let baseUrl = process.env.REACT_APP_API_BASE_URL || 'http://localhost:5000';
    let url = `${baseUrl}/model/${district}_${modelEvent}_${matchType}/bracket/${bracketMethod}`;
    // POST the alliances to the url using fetch:
    fetch(url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(payload)
    }).then(response => response.json())
      .then(data => {
        console.log(data);
        setDensity(data['density']);
        setOverall(data['overall']);
      });

  }

  const predictMatch = () => {
    var a1 = Number(alliance1[1]) - 1;
    var a2 = Number(alliance2[1]) - 1;
    var red = slots[a1].map(slot => slot.team ? slot.team.team : '').join(',');
    var blue = slots[a2].map(slot => slot.team ? slot.team.team : '').join(',');

    // POST alliances to /model/district_model_event_match_type/bracket
    let baseUrl = process.env.REACT_APP_API_BASE_URL || 'http://localhost:5000';
    // /model/<model_key>/predict/<red>/<blue>
    let url = `${baseUrl}/model/${district}_${modelEvent}_${matchType}/predict/${red}/${blue}/${modelMethod}`;
    // POST the alliances to the url using fetch:
    fetch(url)
      .then(response => response.json())
      .then(data => {
        setSpread(data['spread']);
        setSigma(data['sigma']);
        setPRed(data['pRed']);
      });
  }

  const handleDragEnd = (result: any) => {
    console.log('drag end', result.destination);
    const { source, destination } = result;
    if (!destination) {
      return;
    }

    if (source.droppableId === 'left' && destination.droppableId.startsWith('droppable-')) {
      const team = leftTeams[source.index];
      let newTeams = leftTeams.filter((_, index) => index !== source.index);
      let row = parseInt(destination.droppableId.split('-')[1]) - 1;
      let col = parseInt(destination.droppableId.split('-')[2]);
      const destinationSlot = slots[row][col];
      if (destinationSlot.team) {
        // If it does, remove that team from the slots and add it back to the leftTeams array
        let existingTeams = newTeams.map(team => team.team);
        if (!existingTeams.includes(destinationSlot.team.team)) {
          newTeams = [...newTeams, destinationSlot.team as Team];
        }
      }
      setLeftTeams(newTeams);
      setSlots(slots.map((alliance, index) => (index === row) ?
        alliance.map((slot, index2) => index2 === col ? { team: team } : slot) : alliance));
    }
  };


  const modeloptions = [
    { label: "OPR", value: "opr" },
    { label: "DPR", value: "dpr" },
    { label: "TPR", value: "tpr" }
  ];

  return (
    <DragDropContext onDragEnd={handleDragEnd}>
      <EventForm
        district={district}
        modelEvent={modelEvent}
        matchType={matchType}
        onTeamsUpdate={handleTeamsUpdate}
        onPropUpdate={handlePropUpdate} />
      <div className='alliance-component'>
        <TeamList leftTeams={leftTeams} />
        <div className='alliance-list'>
          <div style={{ width: '100%', textAlign: 'right', paddingRight: '10px', boxSizing: 'border-box' }}>% Win</div>
          <hr></hr>
          {Array.from({ length: 8 }, (_, i) => i + 1).map(id => (
            <AllianceSlot id={id} slots={slots} overall={overall} />
          ))}
          <div className='form-group-bracket'>
            <label>Method:</label>
            <Select options={modeloptions}
              onChange={(e) => setBracketMethod(e?.value || '')}
              className='input-field'></Select>
          </div>
          <button onClick={updateBrackets}>Run Brackets</button> <button onClick={clearBrackets}>Clear Brackets</button>
        </div>
        <SingleMatchSimulator
          alliance1={{ value: alliance1, setState: setAlliance1 }}
          alliance2={{ value: alliance2, setState: setAlliance2 }}
          setAlliance2={setAlliance2}
          modeloptions={modeloptions}
          setModelMethod={setModelMethod}
          predictMatch={predictMatch}
          spread={spread}
          sigma={sigma}
          pRed={pRed} />
      </div>
      <div className='ratings-container'>
        <RatingsView teams={allTeams} />
      </div>
    </DragDropContext>
  );
}

export default AllianceComponent;

/* 
 {density && Object.keys(density).map((match)=> {
                  let outcome = density[Number(match)];
                  return (
                    <div>M{match}: {Object.keys(outcome).map((key) => ` ${key}: ${outcome[key]/10}` )}
                  </div>)})}
                  */
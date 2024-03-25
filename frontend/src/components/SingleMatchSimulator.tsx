import React from 'react';
import GaussianPlot from './GaussianPlot';
import Select from 'react-select';
import { AllianceState } from '../types/AllianceState';

class SingleMatchSimulatorProps {
    alliance1: AllianceState = new AllianceState();
    alliance2: AllianceState = new AllianceState();
    setAlliance2: (alliance2: string) => void = () => {};
    modeloptions: { value: string; label: string }[] = [];
    setModelMethod: (modelMethod: string) => void = () => {};
    predictMatch: () => void = () => {};
    spread: number | null = null;
    sigma: number | null = null;
    pRed: number | null = null;
}



function SingleMatchSimulator({ 
    alliance1,     
    alliance2, 
    modeloptions, 
    setModelMethod, 
    predictMatch, 
    spread, 
    sigma, 
    pRed 
  }: SingleMatchSimulatorProps) {
    return (
      <div className='bracket-list'>
        <h2>Single Match</h2>
        <div className='form-group'>
          <label>Red:</label><input type="text" value={alliance1.value} onChange={e => alliance1.setState(e.target.value)} className="input-field"></input>
        </div>
        <div className='form-group'>
          <label> Blue:</label><input type="text" value={alliance2.value} onChange={e => alliance2.setState(e.target.value)} className="input-field"></input>
        </div>
        <div className='form-group'>
          <label>Method:</label><Select options={modeloptions} onChange={(e) => setModelMethod(e?.value || '')} className='input-field'></Select>
        </div>
        <button onClick={predictMatch}>Run Match</button>
        <hr></hr>
        {spread && <div>Spread: {spread.toFixed(2)}</div>}
        {sigma && <div>Sigma: {sigma.toFixed(2)}</div>}
        {pRed && <div>Red Win: {(pRed * 100).toFixed(2)}%</div>}
        {spread && sigma && <GaussianPlot mean={spread} sigma={sigma} />}
      </div>
    );
  }

  export default SingleMatchSimulator
import React from 'react';
import StrictModeDroppable from './StrictModeDroppable';
import {  DroppableProvided, Draggable, DraggableProvided } from 'react-beautiful-dnd';
import { scaleLinear } from 'd3-scale';

import { Team } from '../types/TeamTypes';


const renderStats = (team: Team) => {
    // return each stat to two decimal places
    return `OPR: ${team.stats.opr.mu.toFixed(2)}\nDPR: ${team.stats.dpr.mu.toFixed(2)}\nTPR: ${team.stats.tpr.mu.toFixed(2)}`;
  }

class TeamListProps {
    leftTeams: Team[] = [];
}

function TeamList({ leftTeams } : TeamListProps ) {
    let colorScale = scaleLinear<string>()
      .domain([Math.min(...leftTeams.map(team => team.stats.opr.mu)), Math.max(...leftTeams.map(team => team.stats.opr.mu))])
      .range(['lightgreen', 'red']); 
  
    return (
      <StrictModeDroppable droppableId="left">
        {(provided: DroppableProvided) => (
          <div ref={provided.innerRef} {...provided.droppableProps} className="team-list">
            {leftTeams.sort((a, b) => b.stats.tpr.mu - a.stats.tpr.mu).map((team, index) => {                       
              let calcBackgroundColor = colorScale(team.stats.opr.mu)
              return (
                <Draggable key={team.team} draggableId={team.team} index={index}>
                  {(provided: DraggableProvided) => { 
                    const style = {
                      backgroundColor: calcBackgroundColor,                      
                      ...provided.draggableProps.style,
                    };
                    const title=renderStats(team);
                    return (
                      <div ref={provided.innerRef} {...provided.draggableProps} {...provided.dragHandleProps} style={style} title={title} className="team-div">                            
                        {team.number+' '+team.nickname}
                      </div>
                    )
                  }}
                </Draggable>
              )
            })}
          </div>
        )}
      </StrictModeDroppable>
    );
  }

export default TeamList ;
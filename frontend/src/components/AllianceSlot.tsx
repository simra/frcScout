import React from 'react';
import StrictModeDroppable from './StrictModeDroppable';
import {  DroppableProvided,  DroppableStateSnapshot } from 'react-beautiful-dnd';
import { Team } from '../types/TeamTypes';

class AllianceSlotProps {
    id: number = 0;
    slots: {
        team: Team | null;
    }[][] = [];
    overall: {
        [key: string]: number;
    } = {};
}

function AllianceSlot({ id, slots, overall } : AllianceSlotProps) {
    return (
      <div key={id} className='alliance-slots'>
        <div style={{ marginRight: '10px' }}>A{id}</div>
        {slots[id-1].map((slot, index) => (
          <StrictModeDroppable key={index} droppableId={`droppable-${id}-${index}`}>
            {(provided : DroppableProvided, snapshot: DroppableStateSnapshot) => (
              <div
                ref={provided.innerRef}
                style={{ backgroundColor: snapshot.isDraggingOver ? 'lightblue' : 'lightgrey' }}
                {...provided.droppableProps}
                title={`OPR: ${slot.team?.stats.opr.mu}\nDPR: ${slot.team?.stats.dpr.mu}\nTPR: ${slot.team?.stats.tpr.mu}`}                         
                className = 'alliance-slot'
              >
                {slot.team? slot.team.number : 'Drop team here'}
                {provided.placeholder}
              </div>
            )}
          </StrictModeDroppable>
        ))}
        <div className='overall-value'>{overall && ('A'+id) in overall ? overall['A'+id]/10 : ''}</div>
      </div>
    );
  }

  export default AllianceSlot;
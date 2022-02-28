import React, { useState } from 'react';
import { DragDropContext, Droppable, Draggable } from 'react-beautiful-dnd';
import courses from './courses.js';
import {reorder, verticalList} from './vertical.js';

// Move item from one list to another list
const move = (allLists, source, destination, droppableSource, droppableDestination) => {
  const sourceClone = Array.from(source);
  const destClone = Array.from(destination);
  const [removed] = sourceClone.splice(droppableSource.index, 1);
  destClone.splice(droppableDestination.index, 0, removed);
  
  const result = {...allLists};
  result[droppableSource.droppableId] = sourceClone;
  result[droppableDestination.droppableId] = destClone;

  return result;
};

function MultipleDragList() {
  const [listsStates, setLists] = useState({
    list1: courses,
    list2: [],
    list3: []
  });

  const onDragEnd = (result) => {
    if (!result.destination) return;

    // move inside same list
    if (result.source.droppableId === result.destination.droppableId) {
      const reorderResult = reorder(
        listsStates[result.source.droppableId], 
        result.source.index, 
        result.destination.index);
      const newListsStates = {...listsStates};
      newListsStates[result.destination.droppableId] = reorderResult;
      setLists(newListsStates);
    }

    // interlist movement
    else {
      const newListsStates = move(
        listsStates,
        listsStates[result.source.droppableId],
        listsStates[result.destination.droppableId],
        result.source,
        result.destination
      );
      setLists(newListsStates);
    }
  };

  return (
    <div style={{ 'display': 'flex' }}>
      <DragDropContext onDragEnd={onDragEnd}>
        <Droppable droppableId="list1">
          {(provided, snapshot) => (
            verticalList(listsStates['list1'], provided, snapshot)
          )} 
        </Droppable>
        <Droppable droppableId="list2">
          {(provided, snapshot) => (
            verticalList(listsStates['list2'], provided, snapshot)
          )}
        </Droppable>
        <Droppable droppableId="list3">
          {(provided, snapshot) => (
            verticalList(listsStates['list3'], provided, snapshot)
          )}
        </Droppable>
      </DragDropContext>
    </div>
  );
}

export default MultipleDragList
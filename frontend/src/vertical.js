import React, { useState } from "react";
import { DragDropContext, Droppable, Draggable } from "react-beautiful-dnd";
import courses from './courses.js';

const grid = 10;

const getItemStyle = (isDragging, draggableStyle) => ({
  userSelect: "none",
  padding: grid * 2,
  margin: `0 0 ${grid}px 0`,
  background: isDragging ? 'lightgreen' : 'white',
  ...draggableStyle
});

const getListStyle = isDraggingOver => ({
  background: isDraggingOver ? 'lightblue' : 'lightgrey',
  padding: grid,
  width: 250
});

// reorder items within a list
const reorder = (list, startIndex, endIndex) => {
  const result = Array.from(list);
  const [removed] = result.splice(startIndex, 1);
  result.splice(endIndex, 0, removed);
  return result;
};

const verticalList = (items, provided, snapshot) => {
  return (
  <div
    ref={provided.innerRef}
    style={getListStyle(snapshot.isDraggingOver)}>
    {items.map((item, index) => (
      <Draggable
        key={item.id}
        draggableId={item.id}
        index={index}>
        {(provided, snapshot) => (
          <div
            ref={provided.innerRef}
            {...provided.draggableProps}
            {...provided.dragHandleProps}
            style={getItemStyle(
              snapshot.isDragging,
              provided.draggableProps.style
            )}>
              <div><b>{item.id}</b></div>
              <div>{item.content}</div>
          </div>
        )}
      </Draggable>
    ))}
    {provided.placeholder}
  </div>
  );
}

function VerticalDragList() {
  const [courseStates, setCourses] = useState(courses);
  const onDragEnd = (result) => {
    if(!result.destination) return;
    const newCourses = reorder(courseStates, result.source.index, result.destination.index);
    setCourses(newCourses);
  }

  return (
    <DragDropContext onDragEnd={onDragEnd}>
      <Droppable droppableId="droppable">
        {(provided, snapshot) => (
          verticalList(courseStates, provided, snapshot)
        )} 
      </Droppable>
    </DragDropContext>
  );
}


export default VerticalDragList;
export {reorder, getItemStyle, getListStyle, verticalList};
import React, { Component } from 'react';
import { DragDropContext, Droppable, Draggable } from 'react-beautiful-dnd';
import courses from './courses.js';

const reorder = (list, startIndex, endIndex) => {
  const result = Array.from(list);
  const [removed] = result.splice(startIndex, 1);
  result.splice(endIndex, 0, removed);

  return result;
};

// Move item from one list to other
const move = (source, destination, droppableSource, droppableDestination) => {
  const sourceClone = Array.from(source);
  const destClone = Array.from(destination);
  const [removed] = sourceClone.splice(droppableSource.index, 1);

  destClone.splice(droppableDestination.index, 0, removed);

  const result = {};
  result[droppableSource.droppableId] = sourceClone;
  result[droppableDestination.droppableId] = destClone;

  return result;
};

const grid = 10;

const getItemStyle = (isDragging, draggableStyle) => ({
  userSelect: 'none',
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

function verticalList(items, provided, snapshot) {
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

class MultipleDragList extends Component {
  state = {
    list1: courses,
    list2: [],
    list3: []
  };

  // Defining unique ID for multiple lists
  id2List = {
    droppable1: 'list1',
    droppable2: 'list2',
    droppable3: 'list3'
  };

  getList = id => this.state[this.id2List[id]];

  onDragEnd = result => {
    const { source, destination } = result;

    if (!destination) {
      return;
    }

    // Sorting in same list
    if (source.droppableId === destination.droppableId) {
      const items = reorder(
        this.getList(source.droppableId),
        source.index,
        destination.index
      );

      let state = { list1: items };

      if (source.droppableId === 'droppable2') {
        state = { list2: items };
      }
      if (source.droppableId === 'droppable3') {
        state = { list3: items };
      }

      this.setState(state);
    }
    // Interlist movement
    else {
      const result = move(
        this.getList(source.droppableId),
        this.getList(destination.droppableId),
        source,
        destination
      );

      if (source.droppableId === 'droppable1') {
        this.setState({
          list1 : result[source.droppableId]
        });
      } else if (source.droppableId === 'droppable2') {
        this.setState({
          list2 : result[source.droppableId]
        });
      } else if (source.droppableId === 'droppable3') {
        this.setState({
          list3 : result[source.droppableId]
        });
      }
      
      if (destination.droppableId === 'droppable1') {
        this.setState({
          list1 : result[destination.droppableId]
        });
      } else if (destination.droppableId === 'droppable2') {
        this.setState({
          list2 : result[destination.droppableId]
        });
      } else if (destination.droppableId === 'droppable3') {
        this.setState({
          list3 : result[destination.droppableId]
        });
      }
    }
  };

  render() {
    return (
      <div style={{ 'display': 'flex' }}>
        <DragDropContext onDragEnd={this.onDragEnd}>
          <Droppable droppableId="droppable1">
            {(provided, snapshot) => (
              verticalList(this.state.list1, provided, snapshot)
            )} 
          </Droppable>
          <Droppable droppableId="droppable2">
            {(provided, snapshot) => (
              verticalList(this.state.list2, provided, snapshot)
            )}
          </Droppable>
          <Droppable droppableId="droppable3">
            {(provided, snapshot) => (
              verticalList(this.state.list3, provided, snapshot)
            )}
          </Droppable>
        </DragDropContext>
      </div>
    );
  }
}

export default MultipleDragList
export {courses, reorder};
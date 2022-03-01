import React from 'react'
import Card from 'react-bootstrap/Card'
import { Draggable } from 'react-beautiful-dnd'

/* eslint-disable react/prop-types */

function CourseCard (props) {
  const {
    id,
    content,
    index
  } = props

  const grid = 10

  const getItemStyle = (isDragging, draggableStyle) => ({
    userSelect: 'none',
    padding: grid * 2,
    margin: `0 0 ${grid}px 0`,
    height: 150,
    background: isDragging ? 'lightgreen' : 'lightgrey',
    ...draggableStyle
  })

  return (
      <Draggable
        key={id}
        draggableId={id}
        index={index}
      >
        {(provided, snapshot) => (
          <div
            border="dark"
            ref={provided.innerRef}
            {...provided.draggableProps}
            {...provided.dragHandleProps}
            style={getItemStyle(
              snapshot.isDragging,
              provided.draggableProps.style
            )}
          >
            <Card.Title style={{ fontSize: '16px' }}>{id}</Card.Title>
            <Card.Body style={{ fontSize: '14px' }}>{content}</Card.Body>
          </div>
        )}
      </Draggable>
  )
}

export default CourseCard

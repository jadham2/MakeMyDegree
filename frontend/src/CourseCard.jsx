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

  const getItemStyle = (isDragging, draggableStyle) => ({
    userSelect: 'none',
    margin: '0 0 10px 0',
    width: '175px',
    height: '150px',
    'max-width': '175px',
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
          <Card
            border="dark"
            ref={provided.innerRef}
            {...provided.draggableProps}
            {...provided.dragHandleProps}
            style={getItemStyle(
              snapshot.isDragging,
              provided.draggableProps.style
            )}
          >
            <Card.Body>
              <Card.Title style={{ 'text-align': 'center', fontSize: '16px' }}><strong>{id}</strong></Card.Title>
              <Card.Text style={{ 'text-align': 'center' }}>{content}</Card.Text>
            </Card.Body>
          </Card>
        )}
      </Draggable>
  )
}

export default CourseCard

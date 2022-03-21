import React from 'react'
import Card from 'react-bootstrap/Card'
import styled from '@emotion/styled'
import { Draggable } from 'react-beautiful-dnd'

/* eslint-disable react/prop-types */

const CardWrapper = styled(Card)`
  user-select: none;
  margin: 10px;
  width: 175px;
  height: 125px;
  background: ${props => props.isdragging ? 'lightgreen' : 'lightgrey'};
  ${props => props.draggablestyle};
`

function CourseCard (props) {
  const {
    id,
    content,
    index
  } = props

  return (
      <Draggable
        key={id}
        draggableId={id}
        index={index}
      >
        {(provided, snapshot) => (
          <CardWrapper
            border="dark"
            ref={provided.innerRef}
            {...provided.draggableProps}
            {...provided.dragHandleProps}
            isdragging={snapshot.isDragging ? 1 : 0}
            draggablestyle={provided.draggableProps.style}
          >
            <Card.Body>
              <Card.Title style={{ textAlign: 'center', fontSize: '16px' }}><strong>{id}</strong></Card.Title>
              <Card.Text style={{ textAlign: 'center' }}>{content}</Card.Text>
            </Card.Body>
          </CardWrapper>
        )}
      </Draggable>
  )
}

export default CourseCard

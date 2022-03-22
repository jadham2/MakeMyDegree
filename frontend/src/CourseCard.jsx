import React from 'react'
import Card from 'react-bootstrap/Card'
import styled from '@emotion/styled'
import { Draggable } from 'react-beautiful-dnd'

/* eslint-disable react/prop-types */

const CardWrapper = styled(Card)`
  user-select: none;
  box-shadow: 2px 1px 2px 1px rgba(0, 0, 0, 0.17);
  margin: 10px;
  width: 175px;
  height: 125px;
  background: ${props => props.isdragging ? 'lightgreen' : 'white'};
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

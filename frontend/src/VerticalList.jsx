import React from 'react'
import Card from 'react-bootstrap/Card'
import { Droppable } from 'react-beautiful-dnd'
import CourseCard from './CourseCard'

/* eslint-disable react/prop-types */

function VerticalList (props) {
  const {
    id,
    initialCourses
  } = props

  // const grid = 10

  const getListStyle = (isDraggingOver) => ({
    background: isDraggingOver ? 'lightblue' : 'white',
    width: '250px',
    overflowY: 'auto',
    maxHeight: '820px'
  })

  return (
      <Droppable droppableId={id}>
        {(provided, snapshot) => (
          <Card
            border="primary"
            className="m-3"
            {...provided.droppableProps}
            ref={provided.innerRef}
            style={getListStyle(snapshot.isDraggingOver)}
          >
            <Card.Body>
              {initialCourses.map(({ id, content }, index) => (
                <CourseCard key={id} id={id} content={content} index={index} />
              ))}
            </Card.Body>
            {provided.placeholder}
          </Card>
        )}
      </Droppable>
  )
}

export default VerticalList

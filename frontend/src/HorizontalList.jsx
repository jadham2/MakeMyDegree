import React from 'react'
import Card from 'react-bootstrap/Card'
import Stack from 'react-bootstrap/Stack'
import { Droppable } from 'react-beautiful-dnd'
import CourseCard from './CourseCard'

/* eslint-disable react/prop-types */

function HorizontalList (props) {
  const {
    id,
    initialCourses
  } = props

  const grid = 10

  const getListStyle = (isDraggingOver) => ({
    background: isDraggingOver ? 'lightblue' : 'white',
    padding: grid,
    width: 500,
    height: 200,
    'overflow-x': 'auto',
    'overflow-y': 'hidden'
  })

  return (
      <Droppable droppableId={id} direction='horizontal'>
        {(provided, snapshot) => (
          <Card
            border="primary"
            className="m-3"
            {...provided.droppableProps}
            ref={provided.innerRef}
            style={getListStyle(snapshot.isDraggingOver)}
          >
            <Stack direction="horizontal" gap={3}>
              {initialCourses.map(({ id, content }, index) => (
                <CourseCard key={id} id={id} content={content} index={index} />
              ))}
            </Stack>
            {provided.placeholder}
          </Card>
        )}
      </Droppable>
  )
}

export default HorizontalList

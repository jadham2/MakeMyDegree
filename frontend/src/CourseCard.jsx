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
    course,
    setSelectedCourse,
    index
  } = props

  return (
    <div onClick={() => setSelectedCourse(course)}>
      <Draggable
        key={course.course_id}
        draggableId={course.course_id.toString()}
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
              <Card.Title style={{ textAlign: 'center', fontSize: '16px' }}><strong>{course.course_tag}</strong></Card.Title>
              <Card.Text style={{ textAlign: 'center' }}>{course.course_name}</Card.Text>
            </Card.Body>
          </CardWrapper>
        )}
      </Draggable>
    </div>
  )
}

// const areEqual = (prevProps, nextProps) => {
//   if (prevProps.course === nextProps.course) {
//     return true
//   }
//   return false
// }

export default CourseCard
// export default React.memo(CourseCard, areEqual)

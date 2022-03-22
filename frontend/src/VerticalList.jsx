import React from 'react'
import Card from 'react-bootstrap/Card'
import Form from 'react-bootstrap/Form'
import styled from '@emotion/styled'
import { Droppable } from 'react-beautiful-dnd'
import CourseCard from './CourseCard'

/* eslint-disable react/prop-types */

const scrollContainerHeight = 712

const Wrapper = styled.div`
  background: ${({ isDraggingOver }) =>
  isDraggingOver ? 'lightblue' : 'white'};
  display: flex;
  flex-direction: column;
  opacity: ${({ isDropDisabled }) => (isDropDisabled ? 0.5 : 'inherit')};
  padding: $10px;
  border: $10px;
  padding-bottom: 0;
  transition: background-color 0.2s ease, opacity 0.1s ease;
  user-select: none;
  width: 250px;
`

const DropZone = styled.div`
  /* stop the list collapsing when empty */
  min-height: 150px;
  min-width: 175px;
  /*
    not relying on the items for a margin-bottom
    as it will collapse when the list is empty
  */
  padding-bottom: $20px;
`

const ScrollContainer = styled.div`
  display: flex;
  justify-content: center;
  overflow-x: hidden;
  overflow-y: auto;
  scrollbar-width: none;
  max-height: ${scrollContainerHeight}px;
`

function InnerCourseList (props) {
  const {
    courses,
    provided
  } = props

  return (
  <DropZone ref={provided.innerRef}>
    {courses.map(({ id, content }, index) => (
      <CourseCard key={id} id={id} content={content} index={index} />
    ))}
    {provided.placeholder}
  </DropZone>
  )
}

function VerticalList (props) {
  const {
    id,
    initialCourses
  } = props

  return (
    <Card
      border="primary"
      className="m-3"
    >
      <Card.Body>
        <Form.Group className="mb-3">
          <Form.Label><b>Search Class</b></Form.Label>
          <Form.Control placeholder="Enter Class Name"/>
        </Form.Group>
        <Droppable droppableId={id}>
          {(provided, snapshot) => (
            <Wrapper
              isDraggingOver={snapshot.isDraggingOver}
              {...provided.droppableProps}
            >
              <ScrollContainer>
                <InnerCourseList courses={initialCourses} provided={provided} />
              </ScrollContainer>
            </Wrapper>
          )}
        </Droppable>
      </Card.Body>
    </Card>
  )
}

export default VerticalList

import React, { useState } from 'react'
import Card from 'react-bootstrap/Card'
import Form from 'react-bootstrap/Form'
import styled from '@emotion/styled'
import { Droppable } from 'react-beautiful-dnd'
import CourseCard from './CourseCard'
import { Search } from '@styled-icons/bootstrap'

/* eslint-disable react/prop-types */
/* eslint-disable camelcase */

const scrollContainerHeight = 712

const CourseSearch = styled(Search)`
  height: 30px;
  width: 30px;
  text: 'center';
`

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
    setSelectedCourse,
    provided,
    searchText
  } = props

  return (
    <DropZone ref={provided.innerRef}>
      {courses.map((course, index) => (
        course.course_name.toLowerCase().includes(searchText) || course.course_tag.toLowerCase().includes(searchText)
          ? <CourseCard key={course.course_id} course={course} setSelectedCourse={setSelectedCourse} index={index} />
          : null
      ))}
      {provided.placeholder}
    </DropZone>
  )
}

function VerticalList (props) {
  const {
    id,
    setSelectedCourse,
    initialCourses
  } = props

  const [searchText, setSearchText] = useState('')

  const handleInput = (e) => {
    const delayFn = setTimeout(() => {
      setSearchText(e.target.value.toLowerCase())
      console.log(searchText)
    }, 1000)
    return () => clearTimeout(delayFn)
  }

  return (
    <Card
      className="m-3"
      backgroud-color='#fff8e7'
      style={{ boxShadow: '2px 1px 2px 1px rgba(0, 0, 0, 0.17)' }}
    >
      <Card.Body>
        <Form.Group className="mb-3">
          <Form.Label><CourseSearch/><b> Search Class</b></Form.Label>
          <Form.Control onChange={handleInput} placeholder="Enter Class Name"/>
        </Form.Group>
        <Droppable droppableId={id}>
          {(provided, snapshot) => (
            <Wrapper
              isDraggingOver={snapshot.isDraggingOver}
              {...provided.droppableProps}
            >
              <ScrollContainer>
                <InnerCourseList searchText={searchText} courses={initialCourses} setSelectedCourse={setSelectedCourse} provided={provided} />
              </ScrollContainer>
            </Wrapper>
          )}
        </Droppable>
      </Card.Body>
    </Card>
  )
}

export default VerticalList

import React from 'react'
import Card from 'react-bootstrap/Card'
import styled from '@emotion/styled'
import { Droppable } from 'react-beautiful-dnd'
import CourseCard from './CourseCard'

/* eslint-disable react/prop-types */

const Wrapper = styled.div`
  background-color: ${({ isDraggingOver }) =>
    isDraggingOver ? 'lightblue' : 'white'};
  display: flex;
  flex-direction: column;
  padding: $10px;
  user-select: none;
  transition: background-color 0.1s ease;
  margin: $10px;
`

const DropZone = styled.div`
  display: flex;
  /*
    Needed to avoid growth in list due to lifting the first item
    Caused by display: inline-flex strangeness
  */
  align-items: start;
  /* stop the list collapsing when empty */
  min-width: 100px;
  /* stop the list collapsing when it has no items */
  min-height: 150px;
`

const ScrollContainer = styled.div`
  overflow: auto;
`

// $ExpectError - not sure why
const Container = styled.div`
  /* flex child */
  flex-grow: 1;
  /*
    flex parent
    needed to allow width to grow greater than body
  */
  display: inline-flex;
`

function HorizontalList (props) {
  const {
    id,
    initialCourses
  } = props

  return (
      <Droppable droppableId={id} direction='horizontal'>
        {(provided, snapshot) => (
          <Card
            border="primary"
            className="m-3"
          >
            <Wrapper
              isDraggingOver={snapshot.isDraggingOver}
              {...provided.droppableProps}
              >
                <ScrollContainer>
                  <Container>
                    <DropZone ref={provided.innerRef}>
                      {initialCourses.map(({ id, content }, index) => (
                        <CourseCard key={id} id={id} content={content} index={index} />
                      ))}
                      {provided.placeholder}
                    </DropZone>
                  </Container>
                </ScrollContainer>
              </Wrapper>
          </Card>
        )}
      </Droppable>
  )
}

export default HorizontalList

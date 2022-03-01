import React, { useState } from 'react'
import Col from 'react-bootstrap/Col'
import Row from 'react-bootstrap/Row'
import { DragDropContext } from 'react-beautiful-dnd'
import VerticalList from './VerticalList'
import HorizontalList from './HorizontalList'
import courses from './courses'
import Card from 'react-bootstrap/Card'
import exampleDescription from './exampleDescription'
import exampleDegree from './exampleDegree'

function CoursePlanner () {
  const [courseStates, setCourseStates] = useState({
    allCourses: courses,
    Fa2019: [],
    Sp2020: [],
    Sm2020: [],
    Fa2020: [],
    Sp2021: [],
    Sm2021: [],
    Fa2021: [],
    Sp2022: [],
    Sm2022: [],
    Fa2022: [],
    Sp2023: []
  })

  const move = (allLists, source, destination, droppableSource, droppableDestination) => {
    const sourceClone = Array.from(source)
    const destClone = Array.from(destination)
    const [removed] = sourceClone.splice(droppableSource.index, 1)
    destClone.splice(droppableDestination.index, 0, removed)

    const result = { ...allLists }
    result[droppableSource.droppableId] = sourceClone
    result[droppableDestination.droppableId] = destClone

    return result
  }

  const reorder = (list, startIndex, endIndex) => {
    const result = Array.from(list)
    const [removed] = result.splice(startIndex, 1)
    result.splice(endIndex, 0, removed)

    return result
  }

  const onDragEnd = (result) => {
    if (!result.destination) return

    // move inside same list
    if (result.source.droppableId === result.destination.droppableId) {
      const reorderResult = reorder(
        courseStates[result.source.droppableId],
        result.source.index,
        result.destination.index
      )
      const newCourseStates = { ...courseStates }
      newCourseStates[result.destination.droppableId] = reorderResult

      setCourseStates(newCourseStates)
    } else {
      const newCourseStates = move(
        courseStates,
        courseStates[result.source.droppableId],
        courseStates[result.destination.droppableId],
        result.source,
        result.destination
      )
      setCourseStates(newCourseStates)
    }
  }

  return (
      <Col>
        <div style={{ display: 'flex' }}>
          <DragDropContext onDragEnd={onDragEnd}>
            <Col xs={3} lg={2}>
            <VerticalList id="allCourses" initialCourses={courseStates.allCourses} />
            </Col>
            <Col xs={6} lg={8}>
              <Row>
                <Col>
                  <Row>
                    <Card border="primary" className="m-3" style={{ 'flex-grow': 1, overflow: 'auto', 'max-height': 620 }}>
                      {Object.keys(courseStates).slice(1).map((id, index) => (
                        <>
                        <h5>{id}</h5>
                        <HorizontalList key={index} id={id} initialCourses={courseStates[id]} />
                        </>
                      ))}
                    </Card>
                  </Row>
                  <Row lg={200}>
                    <Card border="primary" className="m-3" style={{ 'flex-grow': 1, overflow: 'auto', height: 180 }}>
                      <Card.Body>
                        {exampleDescription}
                      </Card.Body>
                    </Card>
                  </Row>
                </Col>
              </Row>
            </Col>
            <Col xs={3} lg={2}>
              <Card border="primary" className="m-3" style={{ 'flex-grow': 1, overflow: 'auto', maxHeight: '820px' }}>
                <Card.Body>
                  {exampleDegree}
                </Card.Body>
              </Card>
            </Col>
          </DragDropContext>
        </div>
      </Col>
  )
}

export default CoursePlanner

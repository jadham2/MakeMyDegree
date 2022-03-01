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
    Sp2023: [],
    noCourses: []
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
                <Row lg={600}>
                  <Card border="primary" className="m-3" style={{ 'flex-grow': 1, overflow: 'auto', 'max-height': 620 }}>
                    <h5>Fa2019</h5>
                    <HorizontalList id="Fa2019" initialCourses={courseStates.Fa2019} />
                    <h5>Sp2020</h5>
                    <HorizontalList id="Sp2020" initialCourses={courseStates.Sp2020} />
                    <h5>Sm2020</h5>
                    <HorizontalList id="Sm2020" initialCourses={courseStates.Sm2020} />
                    <h5>Fa2020</h5>
                    <HorizontalList id="Fa2020" initialCourses={courseStates.Fa2020} />
                    <h5>Sp2021</h5>
                    <HorizontalList id="Sp2021" initialCourses={courseStates.Sp2021} />
                    <h5>Sm2021</h5>
                    <HorizontalList id="Sm2021" initialCourses={courseStates.Sm2021} />
                    <h5>Fa2021</h5>
                    <HorizontalList id="Fa2021" initialCourses={courseStates.Fa2021} />
                    <h5>Sp2022</h5>
                    <HorizontalList id="Sp2022" initialCourses={courseStates.Sp2022} />
                    <h5>Sm2022</h5>
                    <HorizontalList id="Sm2022" initialCourses={courseStates.Sm2022} />
                    <h5>Fa2022</h5>
                    <HorizontalList id="Fa2022" initialCourses={courseStates.Fa2022} />
                    <h5>Sp2023</h5>
                    <HorizontalList id="Sp2023" initialCourses={courseStates.Sp2023} />
                  </Card>
                </Row>
                <Row lg={200}>
                  <Card border="primary" className="m-3" style={{ 'flex-grow': 1, overflow: 'auto', height: 180 }}>
                    <Card.Body>
                      {exampleDescription}
                    </Card.Body>
                  </Card>
                </Row>
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

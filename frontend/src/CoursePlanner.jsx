import React, { useEffect, useState } from 'react'
import Col from 'react-bootstrap/Col'
import Row from 'react-bootstrap/Row'
import { DragDropContext } from 'react-beautiful-dnd'
import VerticalList from './VerticalList'
import HorizontalList from './HorizontalList'
import Card from 'react-bootstrap/Card'
import exampleDescription from './exampleDescription'
import exampleDegree from './exampleDegree'
import axios from 'axios'

const termMapper = (term) => {
  switch (term.substring(0, 2)) {
    case 'Fa':
      return 'Fall ' + term.substring(2)
    case 'Sp':
      return 'Spring ' + term.substring(2)
    case 'Sm':
      return 'Summer ' + term.substring(2)
    default:
      return term
  }
}

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

function CoursePlanner () {
  const [courseStates, setCourseStates] = useState({
    allCourses: [],
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

  useEffect(() => {
    axios.get('http://localhost:8000/api/courses').then(res => {
      setCourseStates({
        allCourses: res.data,
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
    })
  }, [])

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
      <Col className="d-flex">
        <DragDropContext onDragEnd={onDragEnd}>
          <Col xs={4} lg={2}>
            <VerticalList id="allCourses" initialCourses={courseStates.allCourses} />
          </Col>
          <Col xs={4} lg={8}>
            <Row>
              <Col>
                <Card border="primary" className="m-3 p-3" style={{ flexGrow: 1, overflowY: 'auto', maxHeight: 620 }}>
                  {Object.keys(courseStates).slice(1).map((id) => (
                    <React.Fragment key={id}>
                      <h5 style={{ marginLeft: '17px' }}><strong>{termMapper(id)}</strong></h5>
                      <HorizontalList id={id} initialCourses={courseStates[id]} />
                    </React.Fragment>
                  ))}
                </Card>
              </Col>
            </Row>
            <Row>
              <Col>
                <Card border="primary" className="m-3" style={{ flexGrow: 1, overflow: 'auto', height: 180 }}>
                  <Card.Body>
                    {exampleDescription}
                  </Card.Body>
                </Card>
              </Col>
            </Row>
          </Col>
          <Col xs={4} lg={2}>
            <Card border="primary" className="m-3" style={{ flexGrow: 1, overflow: 'auto', height: '832px', maxHeight: '832px' }}>
              <Card.Body>
                {exampleDegree}
              </Card.Body>
            </Card>
          </Col>
        </DragDropContext>
      </Col>
  )
}

export default CoursePlanner

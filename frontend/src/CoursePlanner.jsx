import React, { useState } from 'react'
import Col from 'react-bootstrap/Col'
import { DragDropContext } from 'react-beautiful-dnd'
import VerticalList from './VerticalList'
import HorizontalList from './HorizontalList'
import courses from './courses'

function CoursePlanner () {
  const [courseStates, setCourseStates] = useState({
    allCourses: courses,
    Fa2019: [],
    Sp2020: [],
    Sm2020: [],
    Fa2020: [],
    Sp2021: [],
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
            <Col xs='auto'>
            <VerticalList id="allCourses" initialCourses={courseStates.allCourses} />
            </Col>
            <Col xs={8}>
              <HorizontalList id="Fa2019" initialCourses={courseStates.Fa2019} />
              <HorizontalList id="Sp2020" initialCourses={courseStates.Sp2020} />
              <HorizontalList id="Fa2020" initialCourses={courseStates.Fa2020} />
              <HorizontalList id="Sp2021" initialCourses={courseStates.Sp2021} />
            </Col>
            <Col xs='auto'>
            <VerticalList id="noCourses" initialCourses={courseStates.noCourses} />
            </Col>
          </DragDropContext>
        </div>
      </Col>
  )
}

export default CoursePlanner

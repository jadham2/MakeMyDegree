import React, { useState } from 'react'
import Col from 'react-bootstrap/Col'
import { DragDropContext } from 'react-beautiful-dnd'
import VerticalList from './VerticalList'
import courses from './courses'

function CoursePlanner () {
  const [courseStates, setCourseStates] = useState({
    allCourses: courses,
    Fa2019: [],
    Sp2020: [],
    Sm2020: [],
    Fa2020: [],
    Sp2021: []
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
            <VerticalList id="allCourses" initialCourses={courseStates.allCourses} />
            <VerticalList id="Fa2019" initialCourses={courseStates.Fa2019} />
          </DragDropContext>
        </div>
      </Col>
  )
}

export default CoursePlanner

import React, { useEffect, useState } from 'react'
import { Col, Row, Card } from 'react-bootstrap'
import { DragDropContext } from 'react-beautiful-dnd'
import VerticalList from './VerticalList'
import HorizontalList from './HorizontalList'
import axios from 'axios'

/* eslint-disable react/prop-types */

const termMapper = (term) => {
  switch (term.substring(0, 2)) {
    case 'Fa':
      return 'Fall ' + term.substring(2)
    case 'Sp':
      return 'Spring ' + term.substring(2)
    case 'Su':
      return 'Summer ' + term.substring(2)
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

function CoursePlanner (props) {
  const {
    update,
    userID,
    userPlan,
    setUserPlan,
    degreeID
  } = props

  const [degree, setDegree] = useState({})
  const [courseStates, setCourseStates] = useState({ allCourses: [], ...userPlan })
  const [tags, setTags] = useState({})
  const [selectedCourse, setSelectedCourse] = useState({})
  const [selectedCourseTags, setSelectedCourseTags] = useState([])
  const [selectedCourseRequisites, setSelectedCourseRequisites] = useState({})
  const [selectedCourseDescription, setSelectedCourseDescription] = useState('')
  const [selectedCourseTerms, setSelectedCourseTerms] = useState([])

  useEffect(() => {
    axios.get(`http://localhost:8000/api/degrees/${degreeID}`).then(res => {
      setDegree(res.data)
    })
    axios.get('http://localhost:8000/api/courses').then(res => {
      let allCourses = res.data.map(({ description, terms, ...keepAttrs }) => keepAttrs)
      Object.values(courseStates).forEach(toRemove => {
        allCourses = allCourses.filter(ar => !toRemove.find(rm => (rm.course_id === ar.course_id)))
      })
      setCourseStates({ ...courseStates, allCourses: allCourses })
    })
    axios.get(`http://localhost:8000/api/users/${userID}/fetch_user_degree`).then(res => {
      setTags(res.data)
    })
  }, [])

  useEffect(() => {
    if (selectedCourse.course_id) {
      axios.get(`http://localhost:8000/api/courses/${selectedCourse.course_id}/fetch_tags_from_course`).then(res => {
        setSelectedCourseTags(res.data.tags)
      })
      axios.get(`http://localhost:8000/api/courses/${selectedCourse.course_id}/fetch_requisites_from_course`).then(res => {
        console.log(res.data)
        setSelectedCourseRequisites(res.data)
      })
      axios.get(`http://localhost:8000/api/courses/${selectedCourse.course_id}`).then(res => {
        setSelectedCourseDescription(res.data.description)
        setSelectedCourseTerms(res.data.terms)
      })
    }
  }, [selectedCourse])

  useEffect(() => {
    setUserPlan(courseStates)
  }, [courseStates])

  useEffect(() => {
    axios.get(`http://localhost:8000/api/users/${userID}/fetch_user_degree`).then(res => {
      setTags(res.data)
    })
  }, [update])

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

  const sortedTerms = Object.keys(courseStates).slice(1).sort((a, b) => {
    const seasonToNum = { Sp: '1', Su: '2', Fa: '3' }
    const aSeason = a.substring(0, 2)
    const bSeason = b.substring(0, 2)
    return Number(a.substring(2) + seasonToNum[aSeason]) - Number(b.substring(2) + seasonToNum[bSeason])
  })

  return (
      <Col className="d-flex">
        <DragDropContext onDragEnd={onDragEnd}>
          <Col xs={4} lg={2}>
            <VerticalList id="allCourses" setSelectedCourse={setSelectedCourse} initialCourses={courseStates.allCourses} />
          </Col>
          <Col xs={4} lg={8}>
            <Row>
              <Col>
                <Card className="m-3 p-3" style={{ boxShadow: '2px 1px 2px 1px rgba(0, 0, 0, 0.17)', flexGrow: 1, scrollbarWidth: 'none', overflowY: 'auto', maxHeight: 620 }}>
                  {sortedTerms.map((id) => (
                    <React.Fragment key={id}>
                      <h5 style={{ marginLeft: '17px' }}><strong>{termMapper(id)}</strong></h5>
                      <HorizontalList id={id} setSelectedCourse={setSelectedCourse} initialCourses={courseStates[id]} />
                    </React.Fragment>
                  ))}
                </Card>
              </Col>
            </Row>
            <Row>
              <Col>
                <Card className="m-3" style={{ boxShadow: '2px 1px 2px 1px rgba(0, 0, 0, 0.17)', flexGrow: 1, scrollbarWidth: 'none', overflow: 'auto', height: 180 }}>
                  <Card.Body>
                    {Object.keys(selectedCourse).length > 0
                      ? <React.Fragment>
                          <h3>{selectedCourse.course_name}</h3>
                          <h4>Course Details</h4>
                          <h5>Associated Tags:</h5>
                          <ul>
                            {selectedCourseTags.map((tag, index) => (
                              <li key={index}>{tag}</li>
                            ))}
                          </ul>
                          <h5>Normally Offered:</h5>
                          <p>
                            {selectedCourseTerms.map((term, index) => (
                              <span key={index}>{termMapper(term)}{index !== (selectedCourseTerms.length - 1) && ', '}</span>
                            ))}
                          </p>
                          <h5>Requisites:</h5>
                          <ul>
                            <li>Prerequisites
                              <ul>
                              {Object.keys(selectedCourseRequisites).length > 0 && selectedCourseRequisites.requisites.pre.map((requisite, index) => (
                                <li key={index}>{requisite}</li>
                              ))}
                              </ul>
                            </li>
                            <li>Corequisites
                              <ul>
                              {Object.keys(selectedCourseRequisites).length > 0 && selectedCourseRequisites.requisites.co.map((requisite, index) => (
                                <li key={index}>{requisite}</li>
                              ))}
                              </ul>
                            </li>
                          </ul>
                          <h5>Catalog Description</h5>
                          <p>{selectedCourseDescription}</p>
                        </React.Fragment>
                      : <h3>Select a course to view details</h3>
                    }
                  </Card.Body>
                </Card>
              </Col>
            </Row>
          </Col>
          <Col xs={4} lg={2}>
            <Card backgroud-color='#fff8e7' className="m-3" style={{ boxShadow: '2px 1px 2px 1px rgba(0, 0, 0, 0.17)', flexGrow: 1, scrollbarWidth: 'none', overflow: 'auto', height: '832px', maxHeight: '832px' }}>
              <Card.Body>
                <h3>{degree.degree_name}</h3>
                {Object.entries(tags).map(([key, value]) => (
                  <React.Fragment key={key}>
                    <h5>{value.tag_name}</h5>
                    Tag Rule: {value.tag_rule} credits
                    {value.tag_rule.split(' ')[0] === '>='
                      ? <p><span style={ value.user_credits < value.total_credits ? { color: 'red' } : { color: 'green' }}>{value.user_credits}/{value.total_credits}</span> credits</p>
                      : <p><span style={ value.user_credits > value.total_credits ? { color: 'red' } : { color: 'green' }}>{value.user_credits}/{value.total_credits}</span> credits</p>
                    }
                  </React.Fragment>
                ))}
              </Card.Body>
            </Card>
          </Col>
        </DragDropContext>
      </Col>
  )
}

export default CoursePlanner

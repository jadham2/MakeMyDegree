import React, { useEffect, useState } from 'react'
import {
  Container, Row, Col, Button, Modal
} from 'react-bootstrap'
import CoursePlanner from './CoursePlanner'
import Login from './Login'
import axios from 'axios'

/* eslint-disable react/prop-types */

function App () {
  const [userID, setUserID] = useState()
  const [name, setName] = useState()
  const [degree, setDegree] = useState()
  const [userPlan, setUserPlan] = useState({})
  const [update, forceUpdate] = useState(0)
  const [show, setShow] = useState(false)
  const [audit, setAudit] = useState({})

  const handleClose = () => setShow(false)

  useEffect(() => {
    if (userID) {
      axios.get(`http://localhost:8000/api/users/${userID}`).then(res => {
        setName(res.data.name)
        setUserPlan(res.data.curr_plan)
        setDegree(res.data.degree)
      })
    }
  }, [userID])

  const handleSubmit = (event) => {
    event.preventDefault()

    const relevantCourses = { ...userPlan }
    delete relevantCourses.allCourses

    axios.put(`http://localhost:8000/api/users/${userID}/update`, {
      relevantCourses
    }).then(res => {
      setAudit(res.data)
    })
    forceUpdate(update + 1)
    setShow(true)
  }

  if (!userID) {
    return <Login setUserID={setUserID} />
  } else {
    return (
        <Container fluid>
          {Object.keys(audit).length > 0 &&
            <Modal show={show} onHide={handleClose}>
              <Modal.Header closeButton>
                <Modal.Title>Audit Results</Modal.Title>
              </Modal.Header>
              <Modal.Body>
                <h4>Requisite Conflicts</h4>
                {Object.keys(audit.requisites).length > 0
                  ? <p>
                      {Object.entries(audit.requisites).map(([key, value]) => (
                        <div key={key}>
                          <strong>{key}: </strong>
                          {value.co.map((course, index) => (
                            <span key={index}>{course} (corequisite){(index !== (value.co.length - 1) || value.pre.length > 0) && ', '}</span>
                          ))}
                          {value.pre.map((course, index) => (
                            <span key={index}>{course} (prerequisite){index !== (value.pre.length - 1) && ', '}</span>
                          ))}
                        </div>
                      ))}
                    </p>
                  : <p>You&apos;re all good!</p>
                }
              </Modal.Body>
              <Modal.Footer>
                <Button variant="primary" onClick={handleClose}>
                  Close
                </Button>
              </Modal.Footer>
            </Modal>
          }
          <Row>
            <Col xs={4} lg={2} className="d-flex align-items-end justify-content-center" >
              {name
                ? <h4>Username: {name}</h4>
                : <h4>loading...</h4>
              }
            </Col>
            <Col xs={4} lg={8} align="center" className="mt-3">
              <h1>MakeMyDegree</h1>
            </Col>
            <Col xs={4} lg={2} className="d-flex align-items-end justify-content-center">
              <Button onClick={handleSubmit} className="w-75" variant="primary">Submit Plan</Button>
            </Col>
          </Row>
          <Row>
            {degree && userPlan
              ? <CoursePlanner update={update} userID={userID} userPlan={userPlan} setUserPlan={setUserPlan} degreeID={degree} />
              : <h1>loading...</h1>
          }
          </Row>
        </Container>
    )
  }
}

export default App

import React, { useEffect, useState } from 'react'
import {
  Container, Row, Col, Button
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

  useEffect(() => {
    if (userID) {
      axios.get(`http://localhost:8000/api/users/${userID}`).then(res => {
        setName(res.data.name)
        setUserPlan(res.data.curr_plan)
        setDegree(res.data.degree)
      })
    }
  }, [userID])

  if (!userID) {
    return <Login setUserID={setUserID} />
  } else {
    return (
        <Container fluid>
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
              <Button className="w-75" variant="primary">Submit Plan</Button>
            </Col>
          </Row>
          <Row>
            {degree && userPlan
              ? <CoursePlanner userID={userID} userPlan={userPlan} setUserPlan={setUserPlan} degreeID={degree} />
              : <h1>loading...</h1>
          }
          </Row>
        </Container>
    )
  }
}

export default App

import React, { useState } from 'react'
import {
  Container, Row, Col, Button
} from 'react-bootstrap'
import CoursePlanner from './CoursePlanner'
import Login from './Login'

/* eslint-disable react/prop-types */

function App () {
  const [userID, setUserID] = useState()

  if (!userID) {
    return <Login setUserID={setUserID} />
  }

  return (
    <Container fluid>
      <Row>
        <Col xs={4} lg={2} className="d-flex align-items-end justify-content-center" >
          <h4>Name: Jess Adham</h4>
        </Col>
        <Col xs={4} lg={8} align="center" className="mt-3">
          <h1>MakeMyDegree</h1>
        </Col>
        <Col xs={4} lg={2} className="d-flex align-items-end justify-content-center">
          <Button className="w-75" variant="primary">Submit Plan</Button>
        </Col>
      </Row>
      <Row>
        <CoursePlanner />
      </Row>
    </Container>
  )
}

export default App

import React from 'react'
import {
  Container, Row, Col, Button
} from 'react-bootstrap'
import CoursePlanner from './CoursePlanner'

/* eslint-disable react/prop-types */

function App () {
  return (
    <Container fluid>
      <Row>
        <Col xs={4} lg={2} classname="align-middle" align='center' display='fluid'>
          <h3>Name: Jess Adham</h3>
        </Col>
        <Col xs={4} lg={8} align="center" className="mt-3">
          <h1>MakeMyDegree</h1>
        </Col>
        <Col xs={4} lg={2}>
          <p></p>
          <Button variant="primary">Submit Plan</Button>{' '}
        </Col>
      </Row>
      <Row>
        <CoursePlanner />
      </Row>
    </Container>
  )
}

export default App

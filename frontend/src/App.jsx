import React from 'react'
import {
  Container, Row, Col
} from 'react-bootstrap'
import CoursePlanner from './CoursePlanner'

/* eslint-disable react/prop-types */

function App () {
  return (
    <Container fluid>
      <Row>
        <Col align="center" className="mt-3">
          <h1>MakeMyDegree</h1>
        </Col>
      </Row>
      <Row>
        <CoursePlanner />
      </Row>
    </Container>
  )
}

export default App

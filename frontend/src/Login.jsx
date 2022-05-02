import React, { useEffect, useState } from 'react'
import {
  Row,
  Col,
  Container,
  Button,
  Form
} from 'react-bootstrap'
import axios from 'axios'

/* eslint-disable react/prop-types */

function Login (props) {
  const [userName, setUserName] = useState()
  const [password, setPassword] = useState()
  const [userDegree, setUserDegree] = useState()
  const [degrees, setDegrees] = useState([])

  useEffect(() => {
    axios.get('http://localhost:8000/api/degrees').then(res => {
      const newDegrees = res.data
      setDegrees(newDegrees)
    })
  }, [])

  const handleSubmit = (event) => {
    event.preventDefault()

    axios.post('http://localhost:8000/api/login', {
      user_name: userName,
      password: password,
      degree: userDegree
    }).then(res => {
      if (res.data.status === 'success') {
        props.setUserID(res.data.user_id)
      } else {
        alert('Invalid password')
      }
    })
  }

  return (
    <Container className="d-flex justify-content-center align-items-center vh-100">
      <Row>
        <Col>
          <Row>
            <Col className="d-flex justify-content-center">
              <h1>MakeMyDegree</h1>
            </Col>
          </Row>
          <Row>
            <Col className="d-flex justify-content-center">
              <Form onSubmit={handleSubmit}>
                <Form.Group className="m-2">
                  <Form.Label>Username</Form.Label>
                  <Form.Control
                    type="text"
                    placeholder="Enter username"
                    onChange={(e) => setUserName(e.target.value)}
                  />
                </Form.Group>
                <Form.Group className="m-2">
                  <Form.Label>Password</Form.Label>
                  <Form.Control
                    type="password"
                    placeholder="Enter password"
                    onChange={(e) => setPassword(e.target.value)}
                  />
                </Form.Group>
                <Form.Group className="m-2">
                  <Form.Label>Degree</Form.Label>
                  <Form.Select onChange={(e) => setUserDegree(e.target.value)}>
                    <option>Select a degree</option>
                    {degrees.map(degree => (
                      <option key={degree.degree_id} value={degree.degree_id}>{degree.degree_name}, {degree.degree_type}, {degree.term}</option>
                    ))}
                  </Form.Select>
                </Form.Group>
                <Row>
                  <Col className="d-flex justify-content-center">
                    <Button variant="primary" type="submit" className="m-2 w-75">Submit</Button>
                  </Col>
                </Row>
              </Form>
            </Col>
          </Row>
        </Col>
      </Row>
    </Container>
  )
}

export default Login

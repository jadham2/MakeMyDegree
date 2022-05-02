import React, { useEffect, useState } from 'react'
import {
  Row,
  Col,
  Button,
  Form
} from 'react-bootstrap'
import axios from 'axios'
import logo from './app_logo.png'
import { keyframes } from '@emotion/react'
import styled from '@emotion/styled'

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
  const Gradient = keyframes`
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
  `
  const MyStyle = styled.div`
    background: linear-gradient(-45deg, #EE7752, #E73C7E, #23A6D5, #23D5AB);
    background-size: 400% 400%;
    animation: ${Gradient} 10s ease infinite;
    height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
  `
  const bounce = keyframes`
    from, 20%, 53%, 80%, to {transform: translate3d(0,0,0);}
    40%, 43% {transform: translate3d(0, -10px, 0);}
    70% {transform: translate3d(0, -5px, 0);}
    90% {transform: translate3d(0,-1px,0);}
  `
  const BounceStyle = styled.h1`animation: ${bounce} 2s ease infinite;`

  return (
    <MyStyle>
      <Row>
        <Col className="d-flex justify-content-center">
          <img src={logo} alt="Logo" />
        </Col>
        <Col>
          <Row>
            <Col className="d-flex justify-content-center">
              <BounceStyle>MakeMyDegree</BounceStyle>
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
    </MyStyle>
  )
}

export default Login

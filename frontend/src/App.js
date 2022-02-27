import { Container, Row, Col, Card } from 'react-bootstrap';
import { DragDropContext, Droppable, Draggable } from 'react-beautiful-dnd';
import VerticalDragList from './vertical';
import MultipleDragList from './mult_vertical';
import reorder from './mult_vertical';
import courses from './courses.js';

function ClassList() {
  return (
    <Droppable droppableId="courseList">
      {(provided) => (
        <Card border="primary" className="m-3" {...provided.droppableProps} ref={provided.innerRef}>
          <Card.Body>
            {courses.map(({id, name}, index) => (
              <CourseCard key={id} id={id} name={name} index={index} />
            ))}
          </Card.Body>
          {provided.placeholder}
        </Card>
      )}
    </Droppable>
  );
}

function CourseCard(props) {
  const {
    id,
    index,
    name
    } = props;

  return (
    <Draggable key={id} draggableId={id} index={index}>
      {(provided) => (
        <Card ref={provided.innerRef} {...provided.draggableProps} {...provided.dragHandleProps}>
          <Card.Body>
            {name}
          </Card.Body>
        </Card>
      )}
    </Draggable>
  );
}

function App() {
    return (
      <Container fluid>
        <Row>
          <Col xs={12} md={8}>
            <MultipleDragList />
          </Col>
          <Col xs={6} md={4}>
            <VerticalDragList />
          </Col>
        </Row>
      </Container>
    );
}

export default App;
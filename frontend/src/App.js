import { Container, Row, Col, Card } from 'react-bootstrap';
import { DragDropContext, Droppable, Draggable } from 'react-beautiful-dnd';
import VerticalDragList from './vertical-dnd.component';
import MultipleDragList from './multiple-list-dnd.component';

const courses = [
  {
    id: 'ECE40400',
    name: 'Introduction to Computer Security',
  },
  {
    id: 'ECE20001',
    name: 'Linear Circuit Analysis I'
  },
  {
    id: 'ECE27000',
    name: 'Digital Systems Design'
  }
]


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
          <Col>
            <VerticalDragList />
          </Col>
          <Col xs={6}>
            <MultipleDragList />
          </Col>
          <Col>
            3 of 3
          </Col>
        </Row>
      </Container>
    );
}

export default App;
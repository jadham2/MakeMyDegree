import { Container, Row, Col, Card } from 'react-bootstrap';
import { DragDropContext, Droppable, Draggable } from 'react-beautiful-dnd';

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
        <DragDropContext>
        <Col>
          <ClassList />
        </Col>
        <Col>
          2 of 2
        </Col>
        <Col>
          3 of 2
        </Col>
        </DragDropContext>
      </Row>
    </Container>
  );
}

export default App;

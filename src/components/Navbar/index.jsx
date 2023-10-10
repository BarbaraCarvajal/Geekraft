import { Navbar as BSNavbar, Nav } from 'react-bootstrap';
import { Link } from 'react-router-dom';
import 'font-awesome/css/font-awesome.min.css'; 
import './Navbar.css';

const Navbar = () => {
  return (
    <BSNavbar bg="light" expand="lg">
      <BSNavbar.Brand as={Link} to="/">Geekraft</BSNavbar.Brand>
      
      <BSNavbar.Toggle aria-controls="basic-navbar-nav" />

      <BSNavbar.Collapse id="basic-navbar-nav">
        <Nav className="ml-auto">
          <Nav.Link as={Link} to="/productos">Productos</Nav.Link>
          <Nav.Link as={Link} to="/blog">Blog</Nav.Link>
          <Nav.Link as={Link} to="/favoritos">
            <i className="fa fa-heart"></i>
          </Nav.Link>
          <Nav.Link as={Link} to="/carrito">
            <i className="fa fa-shopping-cart"></i>
          </Nav.Link>
          <Nav.Link as={Link} to="/usuario">
            <i className="fa fa-user"></i>
          </Nav.Link>
        </Nav>
      </BSNavbar.Collapse>
    </BSNavbar>
  );
};

export default Navbar;

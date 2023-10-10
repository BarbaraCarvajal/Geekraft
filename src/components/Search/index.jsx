import { Button, Form, FormControl } from "react-bootstrap";

const Search = () => {
  return (
    <>
      <Form inline>
        <FormControl type="text" placeholder="buscar..." className="mr-sm-2" />
        <Button variant="outline-success">Buscar producto</Button>
      </Form>
    </>
  );
};

export default Search;

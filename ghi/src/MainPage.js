import { Link } from "react-router-dom";
import { Button } from "react-bootstrap";

function MainPage() {
  return (
    <div className="px-4 py-5 my-5 text-center">
      <h1 className="display-5 fw-bold">Scrum & Coke</h1>
      <div className="col-lg-6 mx-auto">
        <p className="lead mb-4">
          Welcome to your ideal solution for team and task management.
        </p>
        <Link to="/users/new">
          <Button className="Signup" variant="outline-light" size="lg">
            Signup
          </Button>
        </Link>
        <Link to="/users/login">
          <Button className="Login" variant="outline-light" size="lg">
            Login
          </Button>
        </Link>
      </div>
    </div>
  );
}

export default MainPage;

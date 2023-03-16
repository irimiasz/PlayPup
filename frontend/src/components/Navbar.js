import { NavLink } from "react-router-dom";

const Navbar = () => {
    return ( 
        <nav>
            <div className="nav-wrapper">
                <a href="" className="brand-logo">Pets logo {/* eslint-disable-line */}</a>
                <ul id="nav-mobile" className="right hide-on-med-and-down">
                    <li><NavLink to="/">Home</NavLink></li>
                    <li><NavLink to="/register">Register</NavLink></li>
                </ul>
            </div>
        </nav>
     );
}
 
export default Navbar;
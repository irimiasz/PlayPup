import { Outlet } from "react-router-dom";
import Navbar from "./Navbar";

const RootComponent = () => {
    return ( 
        <div>
            <Navbar />
            <div className="container">
                <Outlet />
            </div>
        </div>
     );
}
 
export default RootComponent;
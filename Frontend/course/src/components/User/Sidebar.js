import { Link } from "react-router-dom";
import { useState, useEffect } from "react";
import axios from 'axios';
const baseURL = "http://127.0.0.1:8000/api";


function Sidebar(){
    const [notifData, setNotifData] = useState([]);
    const studentId = localStorage.getItem('studentId');

    useEffect(()=>{
        // Fetch Courses
        try{
            axios.get(baseURL+'/student/fetch-all-notifications/'+studentId)
            .then((res)=>{
                console.log(res);
                setNotifData(res.data);
            });
        }catch(error){
            console.log(error);
        }
    },[]);

    return (
        <div className="card">
                        <Link to="/student-dashboard" className="list-group-item list-group-item-action"><h5 className="card-header">Student Dashboard</h5></Link>
                        <div className="list-group list-group-flush">
                        
                        <Link to="/student-dashboard" className="list-group-item list-group-item-action">Student Dashboard</Link>
                        <Link to="/my-courses" className="list-group-item list-group-item-action">My Courses</Link>
                        <Link to="/my-teachers" className="list-group-item list-group-item-action">My Teachers</Link>
                        <Link to="/favorite-courses" className="list-group-item list-group-item-action">Favorite Courses</Link>
                        <Link to="/my-assignments" className="list-group-item list-group-item-action">Assignments<span className="float-end badge bg-danger mt-1">{notifData.length}</span></Link>
                        <Link to="/profile-setting" className="list-group-item list-group-item-action">Profile Setting</Link>
                        <Link to="/update-password" className="list-group-item list-group-item-action">Update Password</Link>
                        <Link to="/student-logout" className="list-group-item list-group-item-action text-danger">Logout</Link>

                    </div>
                    </div>
    )
}

export default Sidebar;
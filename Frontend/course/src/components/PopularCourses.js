import { Link } from "react-router-dom";
import { useEffect, useState } from "react";
import axios from 'axios';
const baseURL = "http://127.0.0.1:8000/api";



function PopularCourses() {
  const [courseData, setCourseData] = useState([]);
 

// Fetch courses when page load
  useEffect(()=>{
      try{
          axios.get(baseURL+'/popular-courses/?all=4')
          .then((res)=>{
              setCourseData(res.data);
          })
        }catch(error){
          console.log(error)
        }
 
  }, []);
    return (
      <div className="container mt-3">
      <h3 className="pb-1 mb-5">Popular Courses</h3>
      <div className="row mb-4">
        {courseData && courseData.map((row,index)=>
          <div className="col-md-3">
      <div className="card">
      <Link to={`/detail/${row.course.id}`}><img src={row.course.featured_img} className="card-img-top" alt={row.course.title}/></Link>
      <div className="card-body">
        <h5 className="card-title"><Link to={`/detail/${row.course.id}`}>{row.course.title}</Link></h5>
      </div>
      <div className="card-footer">
       <div className="title"><span>Rating: {row.rating}/5</span>
       <span className="float-end">Views: {row.course.course_views}</span></div>
      </div>
    </div>
    </div>
    )}
    </div>
  
  { /* End Latest Courses */ }
  {/* Pagination Start */}
  <nav aria-label="Page navigation example mt-5">
  <ul className="pagination justify-content-center">
    <li className="page-item"><a className="page-link" href="#">Previous</a></li>
    <li className="page-item"><a className="page-link" href="#">1</a></li>
    <li className="page-item"><a className="page-link" href="#">2</a></li>
    <li className="page-item"><a className="page-link" href="#">3</a></li>
    <li className="page-item"><a className="page-link" href="#">Next</a></li>
  </ul>
</nav>
  {/* Pagination End */}
  </div>
    )
}

export default PopularCourses;
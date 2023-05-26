import { Link } from "react-router-dom";
import { useEffect, useState } from "react";
import axios from 'axios';
const baseURL = "http://127.0.0.1:8000/api";

function Category(){
  const [categoryData, setCategoryData] = useState([]);

  useEffect(()=>{
    try{
        axios.get(baseURL+'/category/')
        .then((res)=>{
            setCategoryData(res.data);
        })
      }catch(error){
        console.log(error)
      }
    
}, []);
  useEffect(() => {
    document.title='All Categories';
});
    return (
        <div className="container mt-3">
        { /* Latest Courses */ }
        <h3 className="pb-1 mb-4">All Categories</h3>
    <div className="row mb-4">
    {categoryData && categoryData.map((row, index)=>
        <div className="col-md-3 mb-4">
    <div className="card">
    <div className="card-body">
      <h5 className="card-title"><Link to={`/course/${row.index}/${row.title}`}>{row.title} ({row.total_courses})</Link></h5>
      <p className="card-text">{row.description}</p>
    </div>
  </div>
  </div>
  )}
  </div>
  
  { /* End Latest Courses */ }
  {/* Pagination Start */}
  {/* <nav aria-label="Page navigation example mt-5">
  <ul className="pagination justify-content-center">
    <li className="page-item"><a className="page-link" href="#">Previous</a></li>
    <li className="page-item"><a className="page-link" href="#">1</a></li>
    <li className="page-item"><a className="page-link" href="#">2</a></li>
    <li className="page-item"><a className="page-link" href="#">3</a></li>
    <li className="page-item"><a className="page-link" href="#">Next</a></li>
  </ul>
</nav> */}
  {/* Pagination End */}
  </div>
    )
}

export default Category;
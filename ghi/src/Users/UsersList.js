import React, { useState, useEffect } from 'react';


function UsersList({ users, getUsers }){
  console.log(users)
  const deleteUser = async (id) => {
    const response = await fetch(`http://localhost:8080/users/${id}/`, {
      method: "delete",
    })
  if (response.ok) {
    return getUsers()
  }
  }
  if (users === undefined) {
     return null
  }

  return (
    <>
      <table className="table table-striped align-middle mt-5">
        <thead>
          <tr>
            <th>Email</th>
            <th>Full name</th>
            <th>Employee number</th> 
            <th>Delete this user</th> 
          </tr>
        </thead>
        <tbody>
          {users.map(user => {
            return (
              <tr key={user.id}>
                <td>{ user.email }</td>
                <td>{ user.full_name }</td>
                <td>{ user.employee_number }</td>
                <td>
                  <button type="button" className="btn btn-danger" value={user.employee_number} onClick={() => deleteUser(user.employee_number)}>Delete User</button> 
                </td>
              </tr>
            );
          })}
        </tbody>
      </table>      
    </>
    );
}

export default UsersList;
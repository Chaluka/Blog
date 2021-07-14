import React from "react";

function Post(props) {
  return (
    <div>
      <h1>{props.heading}</h1>
      <h3>{props.category}</h3>
      <p>{props.content}</p>
    </div>
  );
}

export default Post;

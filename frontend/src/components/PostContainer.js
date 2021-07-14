import React from "react";
import Post from "./PostComponent";

class PostContainer extends React.Component {
  constructor() {
    super();
    this.state = {
      posts: [
        {
          heading: "default",
          category: "DEFLT",
          content: "default",
        },
      ],
    };
  }

  componentDidMount() {
    fetch("/api/view/")
      .then((response) => response.json())
      .then((data) => {
        this.setState({
          posts: data,
        });
      });
  }

  render() {
    console.log(this.state.posts);
    let components = this.state.posts.map((post) => {
      return (
        <Post
          heading={post.heading}
          category={post.category}
          content={post.content}
        />
      );
    });
    return (
      <div>
        <h1>posts</h1>
        {components}
      </div>
    );
    // return <div className="c">done</div>;
  }
}

export default PostContainer;
// category: "CPLUS"
// content: "I dont know . you tell me boss"
// created_at: "2021-07-14T05:43:38.457596Z"
// heading: "How to practice C++"

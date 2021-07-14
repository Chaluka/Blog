import React, { Component } from "react";
import { Grid, Button, ButtonGroup, Typography } from "@material-ui/core";
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link,
  Redirect,
} from "react-router-dom";

import CreatePostPage from "./CreatePostPage";
import PostContainer from "./PostContainer";

export default class HomePage extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <Router>
        <Switch>
          <Route exact path="/">
            <div>
              <h1>Home Page</h1>
              <PostContainer />
            </div>
          </Route>
          <Route path="/create" component={CreatePostPage} />
        </Switch>
      </Router>
    );
  }
}

import React, { Suspense, lazy } from "react"
import { Route, Switch } from "react-router-dom"
import { RouteLoader } from "../UI"
import * as urls from "../urls"

const ThreadsRoute = lazy(() => import("../ThreadsRoute"))
const UserRoute = lazy(() => import("../UserRoute"))

const sluggable = {"id": ":id", "slug": ":slug"}

const AppRoutes: React.FC = () => (
  <Suspense fallback={<RouteLoader />}>
    <Switch>
      <Route path={urls.user(sluggable)} component={UserRoute} />
      <Route path="/" component={ThreadsRoute} />
    </Switch>
  </Suspense>
)

export default AppRoutes
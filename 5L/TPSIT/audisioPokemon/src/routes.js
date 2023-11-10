import Dashboard from "views/Dashboard.js";
import Card from "views/Card.js";
import Gcc from "views/Gcc";

var routes = [
  {
    path: "/dashboard",
    name: "Dashboard",
    icon: "tim-icons icon-chart-pie-36",
    component: <Dashboard />,
    layout: "/admin",
  },
  
  {
    path: "/typography",
    name: "Set n.3",
    icon: "tim-icons icon-wallet-43",
    component: <Card />,
    layout: "/admin",
  },

  {
    path: "/gcc",
    name: "Carte Collezionabili",
    icon: "tim-icons icon-single-copy-04",
    component: <Gcc />,
    layout: "/admin",
  }
];
export default routes;

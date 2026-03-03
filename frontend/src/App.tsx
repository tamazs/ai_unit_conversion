import {createBrowserRouter, type RouteObject, RouterProvider} from "react-router-dom";
import Home from "./pages/Home";
import TopPanel from "./pages/TopPanel.tsx";
import CelsiusFahrenheit from "./pages/CelsiusFahrenheit.tsx";
import KgLbs from "./pages/KgLbs.tsx";
import KmhMih from "./pages/KmhMih.tsx";

const routes : RouteObject[] = [
    {
        path: "/",
        element: <TopPanel/>,
        children: [
            {
                path: "/",
                element: <Home/>
            },
            {
                path: "celsius_fahrenheit",
                element: <CelsiusFahrenheit/>
            },
            {
                path: "kg_lbs",
                element: <KgLbs/>
            },
            {
                path: "kmh_mih",
                element: <KmhMih/>
            }
        ]
    }
]

function App() {
    return <RouterProvider router={createBrowserRouter(routes)}/>
}

export default App
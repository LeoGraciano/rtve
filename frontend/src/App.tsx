import {
  BrowserRouter,
  Route,
  Routes
} from "react-router-dom";
import NavBar from './components/NavBar';
import Categories from "./pages/Categories";
import Expenditure from "./pages/Expenditure";
import Home from "./pages/Home";

export default function App(){

  return(
    <BrowserRouter>
      <div className="w-full min-h-screen bg-gray-900">
        <NavBar/>
        <div className="pt-7 flex justify-center px-4">
          <main className="my-10 w-full md:max-w-2xl">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/despesas/*" element={<Expenditure />} />
          <Route path="/catalogos/*" element={<Categories />} />
        </Routes>
          
          </main>
        </div>

      </div>
    </BrowserRouter>
    )
}
import { BiFoodMenu, BiHomeAlt2 } from "react-icons/bi";
import { PiHandCoinsLight } from "react-icons/pi";
import { Link } from 'react-router-dom';
export default function NavBar(){
    return (
        <nav className="w-full fixed bg-slate-50 z-50">
            <div className="py-4 mx-4 flex flex-row gap-4">
                <Link to="/"><span className="flex flex-row gap-1 items-baseline"><BiHomeAlt2/>Home</span></Link>
                <Link to="/despesas"><span className="flex flex-row gap-1 items-baseline"><PiHandCoinsLight/>Despesas</span></Link>
                <Link to="/catalogos"><span className="flex flex-row gap-1 items-baseline"><BiFoodMenu/>Catalogo</span></Link>
            </div>
        </nav>
    )
}
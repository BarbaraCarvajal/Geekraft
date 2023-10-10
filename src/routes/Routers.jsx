import { Route, Routes } from "react-router-dom"
import Productos from "../pages/Productos"
import Favoritos from "../pages/Favoritos"
import Login from "../pages/Login"
import Perfil from "../pages/Perfil"
import CarritoCompra from "../pages/CarritoCompra"
import Producto from "../pages/Producto"
import Blog from "../pages/Blog"

const Routers = () => {
  return (
    <Routes>
      <Route path="/productos" element={<Productos/>} />
      <Route path="productos/:id" element={<Producto/>} />
      <Route path="/favoritos" element= {<Favoritos/>}/>
      <Route path="/login" element= {<Login/>}/>
      <Route path="/perfil" element= {<Perfil/>}/>
      <Route path="/carrito" element= {<CarritoCompra/>}/>
      <Route path="/blog" element= {<Blog/>}/>

    </Routes>
  )
}

export default Routers
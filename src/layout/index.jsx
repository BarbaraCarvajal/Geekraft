import Footer from "../components/Footer";
import Navbar from "../components/Navbar";
import Search from "../components/Search";
import Routers from "../routes/Routers";

const Layout = () => {
  return (
    <>
      <Navbar />
      <Search />
      <main>
        <Routers />
      </main>
      <Footer />
    </>
  )
}

export default Layout;
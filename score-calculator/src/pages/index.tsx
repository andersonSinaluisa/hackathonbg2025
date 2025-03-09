import { Input } from "../components/input"
import { Button } from "../components/button"
import { Home, User, BarChart3 } from "lucide-react"

export default function CreditScoreCalculator() {
    return (
        <div className="flex flex-col min-h-screen">
            {/* Header */}
            <header className="bg-[#e6007e] py-4 px-6">
                <div className="max-w-7xl mx-auto">
                    <img
                        src="/placeholder.svg"
                        alt="Banco Guayaquil"
                        width={200}
                        height={40}
                        className="h-10 w-auto"
                    />
                </div>
            </header>

            <div className="flex flex-1">
                {/* Sidebar */}
                <aside className="w-64 border-r p-6 flex flex-col">
                    <nav className="space-y-6">
                        <a href="#" className="flex items-center text-[#e6007e] font-medium">
                            <Home className="mr-2 h-5 w-5 text-[#e6007e]" />
                            <span>Inicio</span>
                        </a>
                        <a href="#" className="flex items-center text-[#e6007e] font-medium">
                            <User className="mr-2 h-5 w-5 text-[#e6007e]" />
                            <span>Mi Perfil</span>
                        </a>
                        <a href="#" className="flex items-center text-[#e6007e] font-medium">
                            <BarChart3 className="mr-2 h-5 w-5 text-[#e6007e]" />
                            <span>Historial de Scores</span>
                        </a>
                    </nav>
                    <div className="mt-auto pt-6 border-t space-y-4">
                        <a href="#" className="block text-[#e6007e]">
                            Preguntas Frecuentes
                        </a>
                        <a href="#" className="block text-[#e6007e]">
                            Reportar un error
                        </a>
                        <a href="#" className="block text-[#e6007e]">
                            Ayuda
                        </a>
                    </div>
                </aside>

                {/* Main Content */}
                <main className="flex-1 p-8">
                    <div className="max-w-6xl mx-auto">
                        <div className="flex flex-col md:flex-row gap-8">
                            {/* Form Section */}
                            <div className="flex-1">
                                <h1 className="text-3xl font-bold mb-2">Calcula tu Score de credito No convecional</h1>
                                <p className="text-gray-600 mb-8">Ingresa tus redes sociales</p>

                                <div className="space-y-6">
                                    <div>
                                        <label htmlFor="cedula" className="block mb-2">
                                            Cedula
                                        </label>
                                        <Input id="cedula" placeholder="Cedula" className="w-full" />
                                    </div>

                                    <div>
                                        <label htmlFor="twitter" className="block mb-2">
                                            Twitter
                                        </label>
                                        <Input id="twitter" placeholder="nombre de usuario" className="w-full" />
                                    </div>

                                    <div>
                                        <label htmlFor="youtube" className="block mb-2">
                                            Youtube
                                        </label>
                                        <Input id="youtube" placeholder="nombre de usuario" className="w-full" />
                                    </div>

                                    <div>
                                        <label htmlFor="tiktok" className="block mb-2">
                                            TikTok
                                        </label>
                                        <Input id="tiktok" placeholder="nombre de usuario" className="w-full" />
                                    </div>

                                    <div>
                                        <label htmlFor="facebook" className="block mb-2">
                                            Facebook
                                        </label>
                                        <Input id="facebook" placeholder="nombre de usuario" className="w-full" />
                                    </div>
                                </div>
                            </div>

                            {/* Score Section */}
                            <div className="w-full md:w-96">
                                <div className="bg-[#f8d0df] rounded-lg p-6 mb-8">
                                    <h2 className="text-xl font-semibold mb-2">Credit Score</h2>
                                    <div className="text-[#e6007e] text-7xl font-bold text-center my-4">720</div>
                                    <div className="text-center mb-6">Excellent</div>
                                    <Button className="w-full bg-[#e6007e] hover:bg-[#c4006b]">Recalcular</Button>
                                </div>

                                <div>
                                    <h3 className="text-xl font-semibold mb-4">Este score concidera lo siguiente:</h3>
                                    <ul className="space-y-2">
                                        <li>Tu Actividad en redes sociales</li>
                                        <li>Pago de servicios basicos</li>
                                        <li>Datos demograficos</li>
                                        <li>Bienes o posesines</li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                    </div>
                </main>
            </div>
        </div>
    )
}


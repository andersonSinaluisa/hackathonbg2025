from abc import ABC, abstractmethod

class RepositoryCNEL(ABC):
    
    
    @abstractmethod
    def create(self, 
               codigoCuentaAnterior,
                codigoCuentaNuevo,
                cuenAnterior,
                cuenNuevo,
                cuentaContrato,
                cedulaRuc,
                idUnAnterior,
                idUnNueva,
                fechaRegistro,
                unidadNegocio,
                codUnidadNegocio,
                siglasUnidadNegocio,
                interesCondonadoJson,
                mensajeCondonacion,
                correoRegistrado,
                deuda,
                fechaVencimiento,
                planillasVencidas):
        pass
    
    @abstractmethod
    def find_by_dni(self, dni):
        pass
    
    
    @abstractmethod
    def find_all(self):
        pass
    
    
    @abstractmethod
    def update(self, 
               codigoCuentaAnterior,
                codigoCuentaNuevo,
                cuenAnterior,
                cuenNuevo,
                cuentaContrato,
                cedulaRuc,
                idUnAnterior,
                idUnNueva,
                fechaRegistro,
                unidadNegocio,
                codUnidadNegocio,
                siglasUnidadNegocio,
                interesCondonadoJson,
                mensajeCondonacion,
                correoRegistrado,
                deuda,
                fechaVencimiento,
                planillasVencidas):
        pass
    
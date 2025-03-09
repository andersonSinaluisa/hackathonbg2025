

from core.repository.cnel_repository import RepositoryCNEL
from core.model.cnel import Cnel


class CneRepositoryImpl(RepositoryCNEL):
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
        return Cnel.objects.create(codigoCuentaAnterior=codigoCuentaAnterior,
                                    codigoCuentaNuevo=codigoCuentaNuevo,
                                    cuenAnterior=cuenAnterior,
                                    cuenNuevo=cuenNuevo,
                                    cuentaContrato=cuentaContrato,
                                    cedulaRuc=cedulaRuc,
                                    idUnAnterior=idUnAnterior,
                                    idUnNueva=idUnNueva,
                                    fechaRegistro=fechaRegistro,
                                    unidadNegocio=unidadNegocio,
                                    codUnidadNegocio=codUnidadNegocio,
                                    siglasUnidadNegocio=siglasUnidadNegocio,
                                    interesCondonadoJson=interesCondonadoJson,
                                    mensajeCondonacion=mensajeCondonacion,
                                    correoRegistrado=correoRegistrado,
                                    deuda=deuda,
                                    fechaVencimiento=fechaVencimiento,
                                    planillasVencidas=planillasVencidas)
        
    
    def find_by_dni(self, dni):
        return Cnel.objects.filter(cedulaRuc=dni)
    
    
    def find_all(self):
        return Cnel.objects.all()
    
    
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
        cnel = Cnel.objects.get(cedulaRuc=cedulaRuc)
        cnel.codigoCuentaAnterior = codigoCuentaAnterior
        cnel.codigoCuentaNuevo = codigoCuentaNuevo
        cnel.cuenAnterior = cuenAnterior
        cnel.cuenNuevo = cuenNuevo
        cnel.cuentaContrato = cuentaContrato
        cnel.idUnAnterior = idUnAnterior
        cnel.idUnNueva = idUnNueva
        cnel.fechaRegistro = fechaRegistro
        cnel.unidadNegocio = unidadNegocio
        cnel.codUnidadNegocio = codUnidadNegocio
        cnel.siglasUnidadNegocio = siglasUnidadNegocio
        cnel.interesCondonadoJson = interesCondonadoJson
        cnel.mensajeCondonacion = mensajeCondonacion
        cnel.correoRegistrado = correoRegistrado
        cnel.deuda = deuda
        cnel.fechaVencimiento = fechaVencimiento
        cnel.planillasVencidas = planillasVencidas
        cnel.save()
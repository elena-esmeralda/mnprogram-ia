from zeep import Client

def consultar_expedientes():
    client = Client("https://cloud-s16.mnprogram.net/25.3.3.1_3/API/ClientesService.asmx?WSDL")
    
    result = client.service.GetExpedientes(
        instancia="11405",         # ✅ tu ID real de instancia
        operador="Supervisor",     # ✅ operador válido creado en MNprogram
        passMD5="84dcbe9b584ccbc1919e27e3b475805d",  # ✅ contraseña en MD5 del operador
        numEmpresa=2,              # ✅ tu número de empresa real
        token="9f6d6a5b-a2e9-49b0-9fd8-fdf184fe8df4"  # ✅ token real (si es necesario)
    )
    
    return str(result)

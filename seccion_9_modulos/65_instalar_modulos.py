# instalar un modulo
# pip install camelcase

#listar paquetes
# pip list

import camelcase


camel = camelcase.CamelCase()

texto = "mi nombre es miguel"

print(camel.hump(texto))

#desinstalar un paquete
#pip uninstall camelcase
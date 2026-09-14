# Guia de fabricacion y control de calidad

## Antes de imprimir

1. Abra `cad/native/ojiva-alcedo-atthis-v1.f3d` en Fusion 360 y confirme que es la revision liberada.
2. Compare la longitud y los diametros con el fuselaje real. El STL v1 medido tiene 200 mm de altura de envolvente; el informe describe otro prototipo de 134.5 mm. No escale de forma automática sin resolver la discrepancia.
3. Revise la malla con un verificador de laminador. El STL es binario y contiene 12,948 triangulos; este repositorio no declara aun una verificacion de estanqueidad de malla.

## Impresion de prototipo

El informe fuente documenta un prototipo en PLA. No proporciona perfil de laminado suficiente para reproducibilidad, por lo que los siguientes parametros deben registrarse por quien fabrique una unidad:

- Laminador, version y unidades.
- Altura de capa, boquilla, perimetros, tapas y relleno.
- Orientacion, soportes, temperatura de boquilla/cama y velocidad.
- Material, lote y masa final.

La orientacion, el numero de perimetros y la union con el fuselaje afectan directamente la resistencia. Haga una prueba de ajuste en seco antes de integrar la pieza.

## Inspeccion

- Mida longitud total, diametro maximo y diametro/interferencia de la base.
- Examine paredes, punta, transiciones y base en busca de separacion de capas, huecos o grietas.
- Compruebe el ajuste con el fuselaje sin forzar la pieza.
- Registre masa, fotos y revision del archivo en un registro de fabricacion.

## Integracion y seguridad

No se incluyen instrucciones de propulsion ni de lanzamiento. Antes de usar una pieza en un vehiculo, evalúe la estabilidad completa, retencion, sistema de recuperacion, cargas esperadas, reglamentacion local y el protocolo de seguridad del sitio de prueba. Una pieza impresa en PLA puede cambiar sus propiedades con temperatura, envejecimiento y orientacion de capas.

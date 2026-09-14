# Bio-geometria espacial: Diseno y fabricacion de ojiva Alcedo atthis

Proyecto de hardware abierto de SpaceNL para una ojiva biomimetica de coheteria experimental, inspirada en la morfologia del pico del martin pescador comun (*Alcedo atthis*).

**Estado:** prototipo de investigacion v1.0. Este repositorio esta preparado para la autocertificacion OSHWA, pero **todavia no esta certificado** ni tiene un UID de OSHWA. No debe usarse el logotipo de certificacion hasta recibir el identificador oficial.

## Que contiene

| Recurso | Ubicacion | Uso |
| --- | --- | --- |
| Modelo CAD editable | `cad/native/ojiva-alcedo-atthis-v1.f3d` | Fuente nativa de Autodesk Fusion 360 |
| Malla de fabricacion | `cad/mesh/ojiva-alcedo-atthis-v1.stl` | Exportacion para laminador e impresion 3D |
| Guia de fabricacion | `docs/manufacturing/BUILD.md` | Preparacion, impresion, revision y montaje |
| Lista de materiales | `docs/manufacturing/BOM.md` | Insumos y equipo necesarios |
| Evidencia de simulacion | `docs/simulation/RESULTADOS_PRELIMINARES.md` | Capturas y limites de interpretacion |
| Documento de investigacion | `docs/research/` | Fuente DOCX y PDF del estudio presentado |
| Expediente OSHWA | `docs/oshwa/` | Lista de verificacion y datos pendientes de solicitud |

## Datos de la version v1.0

- Geometria: ojiva biomimetica con base de acople integrada.
- Archivo STL: 12,948 triangulos binarios.
- Envolvente medida en el STL: aproximadamente 50.47 x 52.10 x 200.00 mm.
- Material de prototipo documentado: PLA, grosor indicado de 1.75 mm.
- CAD de origen: Autodesk Fusion 360.

> **Control de configuracion importante.** El informe fuente describe un prototipo de 134.5 mm de largo y base de 50.2 mm, mientras que el STL incluido mide 200 mm de largo en su envolvente. Esta diferencia no se ha resuelto; antes de fabricar o certificar, confirme que el STL corresponde a la revision CAD que se pretende liberar y verifique sus unidades en Fusion 360 o el laminador.

## Alcance y validacion

La investigacion reporta resultados estructurales preliminares y continuidad geometrica. No contiene una comparacion cuantitativa reproducible de coeficiente de arrastre (Cd), ni resultados CFD, tunel de viento o vuelos instrumentados que permitan afirmar una mejora aerodinamica frente a una ojiva convencional. Consulte [Resultados preliminares](docs/simulation/RESULTADOS_PRELIMINARES.md) antes de reutilizar cualquier afirmacion de desempeno.

Esta pieza es un prototipo de investigacion. No es un componente certificado para vuelo ni una instruccion de propulsion. Su integracion, pruebas y operacion deben realizarse solo dentro de las normas aplicables, con evaluacion de estabilidad, recuperacion y seguridad por personal competente.

## Inicio rapido

1. Abra el archivo `.f3d` para inspeccionar el modelo fuente y confirmar la revision y las unidades.
2. Importe el `.stl` en su laminador usando milimetros; mida largo y diametro antes de imprimir.
3. Siga la [guia de fabricacion](docs/manufacturing/BUILD.md) y complete los controles dimensionales.
4. Documente cualquier variante y publique sus cambios bajo la licencia de hardware correspondiente.

## Licencias

- **Hardware y archivos de diseno:** [CERN-OHL-W-2.0](LICENSES_CERN-OHL-W-2.0.txt).
- **Documentacion, fotografias y graficos originales de este repositorio:** [CC-BY-SA-4.0](LICENSES_CC-BY-SA-4.0.txt).
- **Marca:** los nombres y logotipos de SpaceNL no se conceden por estas licencias. No hay logotipo ni marca de certificacion OSHWA en este repositorio.

Al reutilizar, conserve los avisos de atribucion y licencias. Revise [Licencias y atribucion](docs/oshwa/LICENSES_Y_ATRIBUCION.md) antes de publicar una derivacion.

## Autoria

Investigacion original: Suri Paola Frausto Galindo y America Aidee Segovia Martinez. Asesor reportado: Fernando Alonso Villalobos. Repositorio y documentacion abierta: SpaceNL.

## Contribuir

Las mejoras deben incluir el archivo fuente editable, un cambio de version, instrucciones de reproduccion y resultados verificables. Consulte [CONTRIBUTING.md](CONTRIBUTING.md).

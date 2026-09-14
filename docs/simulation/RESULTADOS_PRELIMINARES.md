# Evidencia de simulacion estructural preliminar

Las capturas en `media/simulation/` proceden de Autodesk Fusion 360 y se preservan como evidencia visual del estudio fuente. No se han proporcionado el archivo de estudio, material exacto, cargas, restricciones, malla ni reportes exportados; por ello los valores son **indicativos de las capturas**, no un caso reproducible.

## Resultados visibles

| Evidencia | Lectura visible | Interpretacion permitida |
| --- | --- | --- |
| `01-static-von-mises-1.png` | Von Mises maximo 1.008 MPa | Resultado de un estudio estatico mostrado; faltan condiciones de carga y material para validar el factor de seguridad. |
| `07-static-displacement.png` | Desplazamiento total maximo 0.01 mm | Resultado estatico mostrado; no debe extrapolarse a condiciones de vuelo. |
| `08-static-von-mises-2.png` | Von Mises maximo 0.347 MPa | Segundo resultado mostrado con diferentes condiciones no documentadas. |
| `02` a `06` | Formas modales normalizadas | Son visualizaciones de modos. Las escalas de desplazamiento normalizado no representan deformacion real. La captura `05` muestra 1487.508 en la interfaz, pero sin unidades o configuracion exportada no se registra como frecuencia validada. |

## Lo que no esta demostrado aun

- Reduccion de Cd frente a cono, parabola u ojiva tangente.
- Comportamiento en CFD reproducible.
- Resistencia con material, orientacion y cargas de vuelo definidas.
- Respuesta modal con frecuencias y amortiguamiento validados.
- Desempeno en tunel de viento o vuelo instrumentado.

## Para convertir este expediente en evidencia reproducible

Publique el archivo de simulacion, propiedades mecanicas del filamento, contactos, restricciones, magnitud y direccion de cargas, malla y estudio de convergencia. Para una afirmacion aerodinamica, anada geometria de referencia, configuracion CFD completa y datos comparativos de Cd con incertidumbre.

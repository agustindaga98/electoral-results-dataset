# Electoral Results Dataset 🗳️

Object-oriented Python implementation for processing and 
analyzing US county-level electoral results.

## Overview
Implementation of two classes — `ElectoralResult` and 
`ElectoralResultsDataset` — to load, query and export 
electoral data from a CSV file. Includes time complexity 
analysis for each method.

## Features
- Load electoral results from CSV
- Filter results by state and year
- Aggregate votes by candidate
- Determine state winner
- Count counties won per party
- Export filtered results to CSV

## Tools
- Python 3 (no external libraries)

## Time Complexity
| Method | Complexity |
|--------|-----------|
| `size()` | O(1) |
| `state_results()` | O(N) |
| `votes_by_candidate()` | O(N×C) |
| `state_winner()` | O(N×C) |
| `counties_won_by_party()` | O(N) |
| `export_state()` | O(N) |

## Files
- `electoral_result.py` — ElectoralResult class
- `electoral_dataset.py` — ElectoralResultsDataset class

## Data
Dataset provided by the course instructor. Not publicly available.

## Context
Academic project developed in a postgraduate program 
in Management, Analytics & AI.

# Dataset de Resultados Electorales 🗳️

Implementación orientada a objetos en Python para procesar 
y analizar resultados electorales a nivel de condado en EEUU.

## Descripción
Implementación de dos clases — `ResultadoElectoral` y 
`DataSetResultadosElectorales` — para cargar, consultar y exportar 
datos electorales desde un archivo CSV. Incluye análisis de 
complejidad temporal para cada método.

## Funcionalidades
- Carga de resultados electorales desde CSV
- Filtrado de resultados por estado y año
- Agregación de votos por candidato
- Determinación del ganador por estado
- Conteo de condados ganados por partido
- Exportación de resultados filtrados a CSV

## Herramientas
- Python 3 (sin librerías externas)

## Complejidad Temporal
| Método | Complejidad |
|--------|-------------|
| `tamano()` | O(1) |
| `resultados_del_estado()` | O(N) |
| `votos_por_candidato()` | O(N×C) |
| `ganador_estado()` | O(N×C) |
| `condados_ganados_por_partido()` | O(N) |
| `exportar_estado()` | O(N) |

## Archivos
- `resultado_electoral.py` — Clase ResultadoElectoral
- `dataset.py` — Clase DataSetResultadosElectorales

## Datos
Dataset provisto por el docente de la materia. No disponible públicamente.

## Contexto
Proyecto académico desarrollado en el marco de un posgrado 
en Management, Analytics & AI.

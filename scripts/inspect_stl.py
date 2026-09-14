"""Inspeccion basica y reproducible para STL binario, sin dependencias externas."""
from __future__ import annotations

import argparse
import struct
from pathlib import Path


def inspect(path: Path) -> None:
    data = path.read_bytes()
    if len(data) < 84:
        raise ValueError("Archivo demasiado corto para STL binario")
    count = struct.unpack_from("<I", data, 80)[0]
    expected = 84 + count * 50
    if len(data) != expected:
        raise ValueError(f"Tamano {len(data)} no coincide con {count} triangulos ({expected})")

    minimum = [float("inf")] * 3
    maximum = [float("-inf")] * 3
    for index in range(count):
        offset = 84 + index * 50 + 12  # omite normal
        for vertex in range(3):
            x, y, z = struct.unpack_from("<3f", data, offset + vertex * 12)
            for axis, value in enumerate((x, y, z)):
                minimum[axis] = min(minimum[axis], value)
                maximum[axis] = max(maximum[axis], value)

    extents = [hi - lo for lo, hi in zip(minimum, maximum)]
    print(f"Archivo: {path}")
    print(f"Triangulos: {count}")
    print(f"Limites: {minimum} a {maximum}")
    print(f"Envolvente: {extents}")
    print("Nota: STL no almacena unidades; confirme la escala en CAD o laminador.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("stl", type=Path)
    inspect(parser.parse_args().stl)

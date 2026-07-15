from skyfield.api import load

ts = load.timescale()
eph = load("de440s.bsp")

t = ts.now()

sun = eph["sun"]

planetas = [
    "mercury barycenter",
    "venus barycenter",
    "earth barycenter",
    "mars barycenter",
    "jupiter barycenter",
    "saturn barycenter",
    "uranus barycenter",
    "neptune barycenter",
]

print("="*60)
print("POSICIONES HELIOCÉNTRICAS")
print("="*60)

for nombre in planetas:
    r = sun.at(t).observe(eph[nombre]).position.km
    print(f"{nombre:20s} "
          f"x={r[0]:14.3f} "
          f"y={r[1]:14.3f} "
          f"z={r[2]:14.3f}")

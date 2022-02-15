from pathlib import Path

p = Path.cwd()

print(p.parents[0] / '.env')

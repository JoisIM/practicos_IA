import numpy as np
import pandas as pd
def generar_datos(personas):
    estaturas = []
    pesos = []

    for _ in range(personas):
        estatura = np.random.uniform(1.00,2.00)
        peso = np.random.uniform()

        if estatura < 1.60:
            peso = np.random.uniform(10, 70)
        elif estatura >1.60:
            peso = np.random.uniform(60, 100)
        
        estaturas.append(estatura)
        pesos.append(peso)
    
    return pd.DataFrame({'estatura': estaturas, 'peso': pesos})

# Generar los datos y guardarlos en un DataFrame
data = generar_datos(100)

# Mostrar los primeros 5 ejemplos
print(data)
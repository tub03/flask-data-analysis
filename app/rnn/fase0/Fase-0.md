La fase 0 representa los guardados del modelo, los primeros "guardados" de entrenamiento
en el que tenemos un modelo creado con 'ADAM'

```model.compile(optimizer='adam', loss='mean_squared_error')```
Y se entrena con el optimizer
```model.compile(optimizer=optimizer, loss='mean_squared_error')```
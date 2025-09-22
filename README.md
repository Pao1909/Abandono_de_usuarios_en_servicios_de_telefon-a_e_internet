# 📲🌐 Abandono de usuarios en servicios de telefonía e internet
Pronóstico de tasa de cancelación de clientes para un operador de telecomunicaciones.

## 📄 Descripción del proyecto
Al operador de telecomunicaciones Interconnect le gustaría poder pronosticar su tasa de cancelación de clientes. Si se descubre que un usuario o usuaria planea irse, se le ofrecerán códigos promocionales y opciones de planes especiales. El equipo de marketing de Interconnect ha recopilado algunos de los datos personales de sus clientes, incluyendo información sobre sus planes y contratos.
Servicios de Interconnect.

Interconnect proporciona principalmente dos tipos de servicios:

Comunicación por teléfono fijo. El teléfono se puede conectar a varias líneas de manera simultánea.
Internet. La red se puede configurar a través de una línea telefónica (DSL, línea de abonado digital) o a través de un cable de fibra óptica.
Algunos otros servicios que ofrece la empresa incluyen:

Seguridad en Internet: software antivirus (Protección De Dispositivo) y un bloqueador de sitios web maliciosos (SeguridadEnLínea).
Una línea de soporte técnico (Soporte Técnico).
Almacenamiento de archivos en la nube y backup de datos (Backup Online).
Streaming de TV (Streaming TV) y directorio de películas (Streaming Películas)
La clientela puede elegir entre un pago mensual o firmar un contrato de 1 o 2 años. Puede utilizar varios métodos de pago y recibir una factura electrónica después de una transacción.

## 🎯 Objetivos del proyecto
Este proyecto tiene tres objetivos principales:

- Analizar los datos disponibles para identificar los factores clave que influyen en la tasa de cancelación de clientes del operador Interconnect.
- Desarrollar modelos de aprendizaje automático capaces de predecir con precisión la probabilidad de abandono de clientes.
- Proponer estrategias promocionales y de retención basadas en los resultados del modelo, con el fin de reducir la pérdida de clientes y fortalecer su fidelización.

## 🛠 Etapas de finalización del proyecto
Este proyecto se desarrollará en cuatro fases:

1. 🔧 Preprocesamiento de datos: Depuración, transformación y estandarización de los datos para asegurar su calidad y facilitar un análisis efectivo.
2. 🔍 Análisis exploratorio de datos (EDA): Exploración de patrones, tendencias y relaciones entre variables para identificar los principales factores asociados a la cancelación de clientes.
3. 🤖 Modelado de aprendizaje automático: Desarrollo y evaluación de modelos de clasificación que permitan predecir con precisión la probabilidad de abandono por parte de los clientes.
4. 📝 Informe final y recomendaciones: Presentación de los resultados del proyecto y propuesta de estrategias promocionales y de retención basadas en los factores clave identificados.

## 📊 Descripción de los datos

Los datos consisten en archivos obtenidos de diferentes fuentes:

- `contract.csv` — información del contrato;
- `personal.csv` — datos personales del cliente;
- `internet.csv` — información sobre los servicios de Internet;
- `phone.csv` — información sobre los servicios telefónicos.

En cada archivo, la columna `customerID` (ID de cliente) contiene un código único asignado a cada cliente. La información del contrato es válida a partir del 1 de febrero de 2020.
  
## 📚 Librerías 
- Pandas
- NumPy
- matplotlib
- seaborn
- functools
- Scikit-learn
- SciPy
- lightgbm
- xgboost
- catboost

## ⚖️ Licencia
Este proyecto está bajo la licencia Creative Commons Attribution-NonCommercial 4.0 International Public License (CC BY-NC 4.0). Eres libre de usar, compartir y adaptar este trabajo para fines no comerciales, siempre que se dé el crédito adecuado. Para más detalles, consulta el archivo [LICENCIA](LICENCIA.txt) o visita [Creative Commons](https://creativecommons.org/licenses/by-nc/4.0/).


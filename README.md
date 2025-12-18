# Spotify Songs 2024 Dashboard

## 1. Pregunta analítica

**¿Qué artistas y canciones concentran más streams en Spotify (según datos actualizados a 2024) y cómo se relacionan esos streams con su presencia en playlists y en TikTok?**

El objetivo es entender, de forma simple, quién domina los streams en Spotify y cómo se relacionan las reproducciones con la exposición en playlists y en otra plataforma clave de descubrimiento musical (TikTok).

---

## 2. Fuentes de datos utilizadas

Se utiliza el dataset público **“Most Streamed Spotify Songs 2024”**, disponible en Kaggle.

El dataset incluye, entre otras, las siguientes variables:

- Track (nombre de la canción)
- Artist
- Release Date
- All Time Rank
- Track Score
- Spotify Streams
- Spotify Playlist Count
- Spotify Playlist Reach
- Spotify Popularity
- TikTok Posts
- TikTok Views
- Otros campos como Shazam Counts, YouTube Views, etc.

En este repositorio, el archivo original se espera en:

`data/raw/Most Streamed Spotify Songs 2024.csv`

*(Por temas de licencia, el archivo puede no estar incluido; en ese caso, se debe descargar manualmente desde Kaggle.)*

---

## 3. Proceso de limpieza y transformación de los datos

El proceso de preparación se implementó en **Python** en el script:

`src/prepare_spotify_2024.py`

Los pasos principales son:

1. **Carga del CSV crudo**  
   Lectura del archivo `Most Streamed Spotify Songs 2024.csv` con el encoding adecuado (`latin1`).

2. **Selección de columnas relevantes**  
   Se seleccionan columnas enfocadas en la pregunta analítica:
   - Track, Artist, Release Date, All Time Rank, Track Score
   - Spotify Streams, Spotify Playlist Count, Spotify Playlist Reach, Spotify Popularity
   - TikTok Posts, TikTok Views

3. **Renombrado de columnas**  
   Para trabajar más cómodo en español:
   - `Track` → `cancion`
   - `Artist` → `artista`
   - `Spotify Streams` → `spotify_streams_raw`
   - `Spotify Playlist Count` → `spotify_playlist_count_raw`
   - `TikTok Posts` → `tiktok_posts_raw`
   - `TikTok Views` → `tiktok_views_raw`
   - etc.

4. **Conversión de texto a números**  
   Algunas columnas con números vienen como texto con separadores de miles (ej: `"1,234,567"`).  
   Se limpian y convierten a numéricas:
   - `spotify_streams`
   - `spotify_playlist_count`
   - `tiktok_views`

5. **Fecha de lanzamiento y año (opcional)**  
   Se transforma `fecha_lanzamiento` a tipo fecha y se crea la columna `anio_lanzamiento`.

6. **Guardado del dataset procesado**  
   El resultado se guarda en:

   `data/processed/spotify_2024_clean.csv`

Este archivo es el que se utiliza como base en Power BI para construir el panel.

---

## 4. Decisiones de diseño del panel de analítica

El panel fue construido en **Power BI** y publicado de forma pública.

Las decisiones principales de diseño fueron:

1. **Fila de KPIs (visión general)**
   - `Total Streams` (suma total de streams en Spotify).
   - `Nº de canciones` presentes en el dataset.
   - `Nº de artistas` únicos.
   - Arriba se incluye también un cuadro de texto con la **pregunta analítica** para guiar la lectura.

2. **¿Quién domina los streams?**
   - **Gráfico de barras** “Top 10 artistas por streams”.
   - Permite identificar rápidamente qué artistas concentran la mayor cantidad de reproducciones totales.

3. **Relación con playlists**
   - **Gráfico de dispersión** “Playlist Count vs Total Streams por canción”.
   - Eje X: número de playlists en las que aparece la canción.
   - Eje Y: streams totales en Spotify.
   - Cada punto representa una canción.
   - Busca responder si estar en más playlists se asocia con tener más streams.

4. **Relación con TikTok**
   - **Gráfico de dispersión** “TikTok Views vs Total Streams por canción”.
   - Eje X: visualizaciones en TikTok.
   - Eje Y: streams totales.
   - Cada punto corresponde a una canción.
   - Permite explorar la relación entre visibilidad en TikTok y streams en Spotify.

5. **Detalle de canciones**
   - **Tabla de detalle** con columnas como:
     - Canción, artista, Total Streams, número de playlists, TikTok Views, popularidad, etc.
   - Ordenada por streams, para analizar casos específicos después de ver las tendencias generales.

El flujo del dashboard está pensado así:
1) KPIs → contexto general  
2) Barras → quién domina los streams  
3) Scatter playlists → relación exposición vs streams  
4) Scatter TikTok → impacto de otra plataforma  
5) Tabla → detalle a nivel de canción  

---

## 5. Cómo reproducir el análisis

1. Clonar este repositorio:

   ```bash
   git clone https://github.com/SebVargas23/spotify-songs-2024-dashboard.git
   cd spotify-songs-2024-dashboard

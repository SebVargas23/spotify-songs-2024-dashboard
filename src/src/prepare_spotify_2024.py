import pandas as pd
from pathlib import Path

RAW_PATH = Path("data/raw/Most Streamed Spotify Songs 2024.csv")
OUT_PATH = Path("data/processed/spotify_2024_clean.csv")

def to_number(series):
    """
    Convierte textos tipo '1,234,567' a número.
    Si no se puede convertir, devuelve NaN.
    """
    return (
        series.astype(str)
        .str.strip()
        .str.replace(",", "", regex=False)
        .pipe(pd.to_numeric, errors="coerce")
    )

def main():
    # 1. Cargar datos crudos
    df = pd.read_csv(RAW_PATH, encoding="latin1")

    # 2. Seleccionar columnas relevantes
    cols = [
        "Track",
        "Artist",
        "Release Date",
        "All Time Rank",
        "Track Score",
        "Spotify Streams",
        "Spotify Playlist Count",
        "Spotify Playlist Reach",
        "Spotify Popularity",
        "TikTok Posts",
        "TikTok Views",
    ]
    df = df[cols]

    # 3. Renombrar columnas a español
    df = df.rename(
        columns={
            "Track": "cancion",
            "Artist": "artista",
            "Release Date": "fecha_lanzamiento",
            "All Time Rank": "rank_global",
            "Track Score": "track_score",
            "Spotify Streams": "spotify_streams_raw",
            "Spotify Playlist Count": "spotify_playlist_count_raw",
            "Spotify Playlist Reach": "spotify_playlist_reach",
            "Spotify Popularity": "spotify_popularity",
            "TikTok Posts": "tiktok_posts_raw",
            "TikTok Views": "tiktok_views_raw",
        }
    )

    # 4. Convertir campos texto → número
    df["spotify_streams"] = to_number(df["spotify_streams_raw"])
    df["spotify_playlist_count"] = to_number(df["spotify_playlist_count_raw"])
    df["tiktok_views"] = to_number(df["tiktok_views_raw"])

    # 5. Fecha y año de lanzamiento (opcional)
    df["fecha_lanzamiento"] = pd.to_datetime(
        df["fecha_lanzamiento"], errors="coerce"
    )
    df["anio_lanzamiento"] = df["fecha_lanzamiento"].dt.year

    # 6. Guardar dataset procesado
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUT_PATH, index=False)
    print(f"Archivo procesado guardado en: {OUT_PATH}")

if __name__ == "__main__":
    main()

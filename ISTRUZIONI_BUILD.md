# Lusor - App Android

## Metodo 1: GitHub Actions (Consigliato)

1. Crea un repository su GitHub (es. `lusor-app`)
2. Carica tutti i file di questa cartella
3. Vai su Actions → seleziona "Build APK"
4. Clicca "Run workflow"
5. Dopo ~30 min scarica l'APK dagli artifact

## Metodo 2: Docker (Locale)

```bash
# Dalla cartella del progetto
docker run --rm -v ${PWD}:/app -w /app \
  kivy/buildozer:latest \
  android debug

# L'APK si trova in: bin/Lusor-1.0.0-arm64-v8a-debug.apk
```

## Metodo 3: Linux / WSL con Buildozer diretto

Su Ubuntu/Debian (o WSL su Windows):

```bash
# Installa dipendenze
sudo apt-get update
sudo apt-get install -y python3-pip python3-dev libltdl-dev \
  libssl-dev libffi-dev zlib1g-dev git openjdk-17-jdk
pip install --upgrade pip buildozer cython

# Build
cd revisione\ 9\ -\ apk/
buildozer android debug

# L'APK si trova in: bin/Lusor-1.0.0-arm64-v8a-debug.apk
```

## Installazione

Dopo aver ottenuto il file `.apk`:
1. Trasferiscilo sul tuo smartphone Android
2. Tocca il file per installarlo
3. Se richiesto, abilita "Installa da fonti sconosciute"
4. Apri l'app "Lusor"

## Note

- La prima build richiede ~30 minuti (scarica Android SDK, NDK, ecc.)
- L'app funziona su Android 8.0+ (API 26)
- La fotocamera richiede il permesso CAMERA

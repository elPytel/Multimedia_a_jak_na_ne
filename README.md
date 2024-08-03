# Multimédia a jak na ně

## Instalace závislostí

### Linux
Při spuštění `.ipynb` souboru v Jupyter Notebooku, se automaticky nainstalují závislosti ze souboru `requirements.txt`. 

> [!warning] 
> Pokud nelze některé moduly nainstalovat, je nutné nainstalovat `apt` závislosti!

Pokud pracuje na `Linux`, můžete použít skript `install.sh` pro instalaci závislostí.
```bash
./install.sh
```

### Windows

Stáněte si FFmpeg. Lze tak učinit například zde: [FFmpeg](https://ffmpeg.org/download.html), nebo pomocí [UniGetUI](https://www.marticliment.com/unigetui/).

> [!warning]
> Pokud se při spuštění instalace Python závislostí v Jupyter notebooku vyskytne chyba `Microsoft Visual C++ 14.0 or greater is required`, je nutné nainstalovat `Microsoft Visual C++ 14.0` nebo novější (zabere 15+GB).
> - [Microsoft C++ Build Tools](https://visualstudio.microsoft.com/cs/visual-cpp-build-tools/)
> - [stackoverflow](https://stackoverflow.com/questions/64261546/how-to-solve-error-microsoft-visual-c-14-0-or-greater-is-required-when-inst)

## Připravené Jupyter Notebooky

- [Obrazové formáty](./image.ipynb)
- [Audio formáty](./audio.ipynb)
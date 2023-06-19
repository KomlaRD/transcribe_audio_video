# Python script to transcribe audio and video using whisper

Check out more information on [whisper](https://github.com/openai/whisper) [here](https://github.com/openai/whisper)

## Instruction to install anaconda

You need to have anaconda installed to proceed with the following steps.
This will ensure you can create and activate the conda environment.

Follow the link below to install Anaconda.

[Anaconda](https://www.anaconda.com/download/)

## Create a conda environment using the yaml file provided

```bash
conda env create -f environment.yml
```

## Activate environment

```bash
conda activate transcribe
```

## Instruction file (ins.json)

- Provide root path containing videos or audios as a value of **"root_path"**.

- Suggested video directory can be **Videos** and that of audio files can be **Audios**.

## How to use script

### Video script

```bash
python transcription_video.py
```

### Audio script

```bash
python transcription_audio.py
```

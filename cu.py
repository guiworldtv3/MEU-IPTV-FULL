import streamlink
import moviepy.editor as mp
import subprocess
import os
import time

# URL do stream
url = "https://5a7d54e35f9d2.streamlock.net/morromendanha1/morromendanha1.stream/chunklist_w182959856.m3u8"

# Tempo de captura de cada frame (em segundos)
capture_time = 1/30

# Número de frames a serem capturados
num_frames = 200

# FPS da timelapse
fps = 30

# Iniciar o stream
streams = streamlink.streams(url)
stream = streams["best"]

# Variável para armazenar o path dos arquivos de frame
filenames = []

# Iniciar a captura de frames
for i in range(num_frames):
    filename = "frame_{}.png".format(i)
    filenames.append(filename)
    subprocess.run(["ffmpeg", "-i", stream.url, "-vframes", "1", "-r", str(fps), filename], check=True)
    time.sleep(capture_time)

# Criar o vídeo a partir dos frames capturados
clip = mp.ImageSequenceClip(filenames, fps=fps)
clip.write_videofile("timelapse.mp4", preset='ultrafast')

# Limpar os arquivos de frame
for filename in filenames:
    os.remove(filename)

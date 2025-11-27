from gtts import gTTS
import tkinter as tk
import random
import uuid
import pygame
import os

# === pygame 初期化 ===
pygame.mixer.init()

# === 反応パターン ===
responses = {
    "反応的": ["I see.", "I understand.", "Yeah.", "Sounds good.", "Nice.", "Go on."],
    "積極的": ["Don’t worry.", "It's okay.", "Slow pace is fine.", "No hurry."]
}

# === 音声再生関数 ===
def speak(text):
    print("Agent says:", text)
    filename = f"tmp_{uuid.uuid4()}.mp3"

    # gTTSで音声生成
    tts = gTTS(text=text, lang='en')
    tts.save(filename)

    # pygameで再生
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

    # 再生完了まで待機
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)  # CPU負荷を下げる

    os.remove(filename)

# === ランダムに音声を再生 ===
def speak_random(category):
    speak(random.choice(responses[category]))

# === Tkinter GUI ===
root = tk.Tk()
root.title("共感エージェント")

for category in responses.keys():
    tk.Button(
        root,
        text=category + "（ランダム）",
        command=lambda c=category: speak_random(c),
        width=30,
        height=2
    ).pack(pady=5)

root.mainloop()





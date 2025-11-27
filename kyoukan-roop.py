from gtts import gTTS
import tkinter as tk
import uuid
import pygame
import os
import threading

# === pygame 初期化 ===
pygame.mixer.init()

# === 反応パターン ===
responses = {
    "反応的": ["I see.", "I understand.", "Yeah.", "Sounds good.", "Nice.", "Go on."],
    "積極的": ["Don’t worry.", "It's okay.", "Slow pace is fine.", "No hurry."]
}

# === 各カテゴリの再生位置を保持 ===
indices = {key: 0 for key in responses.keys()}

# === 音声再生処理（スレッド内で実行） ===
def speak(text):
    def run():
        print("Agent says:", text)
        filename = f"tmp_{uuid.uuid4()}.mp3"

        tts = gTTS(text=text, lang='en')
        tts.save(filename)

        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()

        # 再生完了待ち
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

        os.remove(filename)

    threading.Thread(target=run, daemon=True).start()

# === 順番に読み上げ ===
def speak_next(category):
    idx = indices[category]  # 今の番号
    text = responses[category][idx]

    speak(text)

    # 次の番号（ループ）
    indices[category] = (idx + 1) % len(responses[category])


# === GUI ===
root = tk.Tk()
root.title("共感エージェント")

for category in responses.keys():
    tk.Button(
        root,
        text=category + "（順番）",
        command=lambda c=category: speak_next(c),
        width=30,
        height=2
    ).pack(pady=5)

root.mainloop()


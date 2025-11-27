import pyttsx3  # テキストの読み上げ、音声出力
import tkinter as tk

# ブロークンイングリッシュの発話フレーズ
phrases = {
    "NNSの意見について": "nice good, good item.",
    "ピストルの話": "Gun very hot, shoot shoot.",
    "赤と白のパラシュートの話": "parachute open, help call and shadow.",
    "化粧用鏡の話": "big sun shine, shine help help call.",
    "3.8L水の話": "drink fast, very dry, need.",
    "薄手の長袖シャツの話": "sun burn my arm, shirt good.",
    "悩んでいたら（1）": "slow choose ok.",
    "悩んでいたら（2）": "Go ,go go!"
}

def speak(text):  # 音声合成と出力
    print("Agent says:", text)
    engine = pyttsx3.init()  # 毎回初期化
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()
    engine.stop()

# --- GUI ---
root = tk.Tk()
root.title("Broken English Agent")

for label, phrase in phrases.items():
    button = tk.Button(root, text=label, command=lambda t=phrase: speak(t),
                       width=30, height=2)
    button.pack(pady=5)

root.mainloop()
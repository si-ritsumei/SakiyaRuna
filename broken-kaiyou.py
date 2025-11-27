import pyttsx3  # テキストの読み上げ、音声出力
import tkinter as tk

# ブロークンイングリッシュの発話フレーズ
phrases = {
    "NNSの意見について": "nice good, good item.",
    "地図の話": "Ocean is big big, very big.",
    "サメスプレーの話": "I’m very, horror shark, eat people shark.",
    "ミラーの話": "Mirror shine! Shine help help call.",
    "ロープの話": "rope pull pull thing, people, boat.",
    "プラスチック板の話": "Plastic rain bye bye.",
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

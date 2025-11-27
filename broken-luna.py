import pyttsx3  # テキストの読み上げ、音声出力
import tkinter as tk

# ブロークンイングリッシュの発話フレーズ
phrases = {
    "NNSの意見について": "nice good, good item.",
    "FMレシーバーの話": "radio noise, big sound.",
    "酸素の話": "Air fast, no breathe, die, die.",
    "暖房装置の話": "hot, hot my body warm.",
    "水の話": "water need , because people life.",
    "パラシュートの話": "parachute open, help call and shadow.",
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
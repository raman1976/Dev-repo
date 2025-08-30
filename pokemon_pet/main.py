import tkinter as tk
from PIL import Image, ImageTk
import os
import argparse
import time
import threading

class PokemonPet:
    def __init__(self, root):
        self.root = root
        self.root.title("Pokemon Pet")
        self.root.geometry("200x200")

        self.canvas = tk.Canvas(root, width=100, height=100)
        self.canvas.pack(pady=20)

        self.image_path = os.path.dirname(os.path.realpath(__file__))
        self.happy_img = ImageTk.PhotoImage(Image.open(os.path.join(self.image_path, "happy.png")))
        self.sad_img = ImageTk.PhotoImage(Image.open(os.path.join(self.image_path, "sad.png")))
        self.neutral_img = ImageTk.PhotoImage(Image.open(os.path.join(self.image_path, "neutral.png")))

        self.pet_image = self.canvas.create_image(50, 50, image=self.neutral_img)
        self.canvas.tag_bind(self.pet_image, "<Button-1>", self.feed_pet)

        self.sad_timer = None
        self.reset_sad_timer()

    def feed_pet(self, event):
        self.canvas.itemconfig(self.pet_image, image=self.happy_img)
        self.reset_sad_timer()

    def make_sad(self):
        self.canvas.itemconfig(self.pet_image, image=self.sad_img)

    def reset_sad_timer(self):
        if self.sad_timer:
            self.root.after_cancel(self.sad_timer)
        self.sad_timer = self.root.after(60000, self.make_sad) # 60 seconds

class PokemonPetHeadless:
    def __init__(self):
        self.state = "neutral"
        self.last_fed = time.time()
        print("Pet is neutral.")

    def feed_pet(self):
        self.state = "happy"
        self.last_fed = time.time()
        print("Pet is happy!")

    def update(self):
        if self.state == "happy" and time.time() - self.last_fed > 5:
            self.state = "neutral"
            print("Pet is neutral.")
        elif time.time() - self.last_fed > 60:
            self.state = "sad"
            print("Pet is sad.")

    def run(self):
        def check_state():
            while True:
                self.update()
                time.sleep(1)

        thread = threading.Thread(target=check_state, daemon=True)
        thread.start()

        while True:
            command = input("Enter 'feed' to feed the pet: ")
            if command == "feed":
                self.feed_pet()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", default="gui", choices=["gui", "headless"])
    args = parser.parse_args()

    if args.mode == "gui":
        try:
            root = tk.Tk()
            app = PokemonPet(root)
            root.mainloop()
        except tk.TclError as e:
            print(f"Could not start GUI: {e}")
            print("Please run in headless mode using --mode headless")
    else:
        app = PokemonPetHeadless()
        app.run()
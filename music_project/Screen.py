import tkinter as tk
from tkinter import ttk, Label, filedialog
from PIL import Image, ImageTk
import pygame.mixer as mixer
from moviepy.editor import VideoFileClip
import os
from mutagen.id3 import ID3

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title('MUSIC PLAYER')
        self.root.geometry('800x600')

        # Set background color using a valid color name or hexadecimal code
        self.root.configure(background='powder blue')  

        # Initialize Pygame mixer
        mixer.init()

        # Create GUI elements
        self.create_widgets()

        # Playlist of music files and corresponding video files
        self.playlist = []
        self.current_song_index = 0

        # Flag to track if video frame is visible
        self.video_frame_visible = False

    def create_widgets(self):
        # Load background image
        background_image = Image.open('music5.jpg')
        self.background_photo = ImageTk.PhotoImage(background_image)
        self.background_photo_label = Label(self.root, image=self.background_photo, bg='powder blue')
        self.background_photo_label.place(relx=0.5, rely=0.5, anchor='center', y=12, width=700, height=500)

        # Label for status
        self.label1 = Label(self.root, text='Let\'s play it.', bg="black", font=('Helvetica', 20), fg='white')
        self.label1.pack(side=tk.BOTTOM, fill=tk.X)

        # Label for current song
        self.current_song_label = Label(self.root, text='', bg="powder blue", font=('Helvetica', 14, 'bold'), wraplength=600, width=50, anchor='center')
        self.current_song_label.place(relx=0.5, rely=0.89, anchor='center')  # Centered placement

        # Frame for video display
        self.video_frame = Label(self.root, bg='black')
        # Initially hide the video frame
        self.video_frame.place_forget()

        # Buttons frame
        button_frame = ttk.Frame(self.root)
        button_frame.pack(pady=20)

        # Define custom button style
        style = ttk.Style()
        style.configure('Custom.TButton', font=('Helvetica', 16, 'bold'), background='green')

        # Previous Button
        self.prev_button = ttk.Button(button_frame, text='⏮️', style='Custom.TButton', command=self.play_previous)
        self.prev_button.pack(side=tk.LEFT, padx=15)

        # Play/Pause Button
        self.play_button = ttk.Button(button_frame, text='▶️', style='Custom.TButton', command=self.play_pause)
        self.play_button.pack(side=tk.LEFT, padx=15)

        # Next Button
        self.next_button = ttk.Button(button_frame, text='⏭️', style='Custom.TButton', command=self.play_next)
        self.next_button.pack(side=tk.LEFT, padx=15)

    def select_music_directory(self):
        # Prompt user to select a directory containing music files
        selected_dir = filedialog.askdirectory()
        if selected_dir:
            self.load_music_files(selected_dir)

    def load_music_files(self, directory):
        # Load all music files from the selected directory into the playlist
        self.playlist = []
        for filename in os.listdir(directory):
            if filename.endswith('.mp3'):
                music_path = os.path.join(directory, filename)
                video_path = os.path.join(directory, filename.replace('.mp3', '.mp4'))
                self.playlist.append({"music": music_path, "video": video_path})

        # Start playing the first song in the playlist if it's not empty
        if self.playlist:
            self.play_song()

    def play_song(self):
        song_info = self.playlist[self.current_song_index]
        music_path = song_info["music"]
        video_path = song_info["video"]

        mixer.music.stop()  # Stop any currently playing music
        mixer.music.load(music_path)  # Load and play music
        mixer.music.play()

        self.label1.config(text='MUSIC IS PLAYING.....')
        self.play_button.config(text='⏸️')  # Change button to pause icon

        # Hide the background image
        self.background_photo_label.place_forget()

        # Read ID3 tags to get song information
        id3 = ID3(music_path)
        song_title = id3.get('TIT2', [''])[0]
        artist = id3.get('TPE1', [''])[0]
        album = id3.get('TALB', [''])[0]
        current_song_info = f'{song_title} - {artist} ({album})' if song_title else os.path.basename(music_path)
        self.current_song_label.config(text=current_song_info)

        # Show the video frame
        self.video_frame.place(relx=0.5, rely=0.5, anchor='center', y=10, width=600, height=400)
        self.video_frame_visible = True

        # Start video playback
        self.play_video(video_path)

    def play_video(self, video_path):
        try:
            video_clip = VideoFileClip(video_path)

            def update_frame(frame_number=0):
                try:
                    frame = video_clip.get_frame(frame_number / video_clip.fps)
                    frame_image = Image.fromarray(frame)
                    frame_photo = ImageTk.PhotoImage(frame_image)

                    # Update video frame label with new frame
                    self.video_frame.config(image=frame_photo)
                    self.video_frame.image = frame_photo  # Keep reference to avoid garbage collection

                    # Schedule next frame update
                    if mixer.music.get_busy() and frame_number < video_clip.fps * video_clip.duration:
                        self.root.after(int(1000 / video_clip.fps), update_frame, frame_number + 1)

                except Exception as e:
                    print(f"Error updating video frame: {e}")
                    video_clip.close()  # Close video clip on error

            # Initial frame update
            update_frame()

        except Exception as e:
            print(f"Error playing video: {e}")

    def play_pause(self):
        if mixer.music.get_busy():
            mixer.music.pause()
            self.label1.config(text='MUSIC PAUSED')
            self.play_button.config(text='▶️')  # Change button back to play icon
        else:
            self.play_song()

    def play_previous(self):
        if self.current_song_index > 0:
            self.current_song_index -= 1
        else:
            self.current_song_index = len(self.playlist) - 1
        self.play_song()

    def play_next(self):
        if self.current_song_index < len(self.playlist) - 1:
            self.current_song_index += 1
        else:
            self.current_song_index = 0
        self.play_song()

if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayer(root)

    # Add a button to select music directory
    select_dir_button = ttk.Button(root, text='Choose Any Folder', command=app.select_music_directory)
    select_dir_button.pack(pady=11)

    root.mainloop()

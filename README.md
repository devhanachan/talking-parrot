# 🦜 Parrot Bot (Python Version)

Parrot Bot is a Discord bot written in Python using `discord.py` and `edge-tts`. It listens to user messages and repeats them in a voice channel using a high-pitched, sped-up "parrot" voice effect.

> **Note:** This is a complete rewrite of the original TypeScript version, migrated to Python for better audio processing capabilities using `pydub`.

## ✨ Features

- **Text-to-Speech (TTS):** Converts user text messages into speech using Microsoft Edge TTS (`edge-tts`).
- **Parrot Voice Effect:** Processes audio to sound like a parrot (high pitch + sped up + echo) using `pydub` and `ffmpeg`.
- **Auto-Join Voice:** Automatically joins the user's voice channel when they send a message.
- **Slash Commands:** Supports modern Discord slash commands (`/join`, `/ping`, etc.).
- **Modular Design:** Built with `discord.ext.commands.Cog` for easy scalability.

## 🛠️ Tech Stack

- **Python 3.10+**
- **discord.py** (Interaction & Bot logic)
- **edge-tts** (Text-to-Speech engine)
- **pydub** (Audio manipulation)
- **FFmpeg** (Required for audio processing)

## 🚀 Getting Started

### Prerequisites

1.  **Python 3.10 or higher**
2.  **FFmpeg** installed and added to your system PATH.
    - [Download FFmpeg](https://ffmpeg.org/download.html)
3.  **Discord Bot Token** from [Discord Developer Portal](https://discord.com/developers/applications).

### Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/devhanachan/Parrot-bot-py.git
    cd Parrot-bot-py
    ```

2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3.  Create a `.env` file in the root directory:
    ```env
    DC_TK=your_discord_bot_token_here
    GUILDID=your_debug_server_id
    DEBUG_ROOM=your_debug_channel_id
    ```

4.  Run the bot:
    ```bash
    python main.py
    ```

## 📂 Project Structure

```
.
├── cogs/
│   ├── commands/       # Slash commands (join, ping, clear)
│   └── events/         # Event listeners (on_ready, on_message)
├── sound_effect/       # Directory for storing generated audio files
├── speaker_demo.py     # TTS & Audio effect processing logic
├── main.py             # Entry point
└── README.md
```

## 🤝 Contributing

We welcome contributions! Whether it's fixing bugs, improving the parrot voice effect, or adding new commands.

### Current Issues / To-Do List
- [ ] **Queue System:** The TTS playback currently overlaps if multiple users spam messages. A proper queue system is needed in `cogs/events/on_message.py`.
- [ ] **UI View Fix:** The `UIButtonspeakTest` in `cogs/commands/voice_.py` is currently commented out because the timeout deletion logic isn't working properly.
- [ ] **Error Handling:** Better error messages when FFmpeg is missing or TTS fails.

### How to Contribute
1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/amazing-feature`).
3.  Commit your changes (`git commit -m 'Add some amazing feature'`).
4.  Push to the branch (`git push origin feature/amazing-feature`).
5.  Open a Pull Request.

## 📝 License

Distributed under the MIT License. See `LICENSE` for more information.

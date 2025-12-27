import os
import asyncio
import edge_tts
from pydub import AudioSegment
import uuid

def _pitch_shift(seg: AudioSegment, octaves: float) -> AudioSegment:
    new_sample_rate = int(seg.frame_rate * (2.0 ** octaves))
    pitched = seg._spawn(seg.raw_data, overrides={"frame_rate": new_sample_rate})
    return pitched.set_frame_rate(seg.frame_rate)

def _parrotify(seg: AudioSegment) -> AudioSegment:
    seg = seg.high_pass_filter(350).low_pass_filter(5500)
    seg = _pitch_shift(seg, octaves=0.20)
    echo = seg - 10 
    seg = seg.overlay(echo, position=70).overlay(echo, position=140)
    return seg

async def generate_parrot_voice(text: str, filename: str = "output.mp3", voice: str = "en-US-AriaNeural") -> str:
    output_dir = "sound_effect"
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    final_output_path = os.path.join(output_dir, filename)
    temp_filename = os.path.join(output_dir, f"temp_{uuid.uuid4().hex}.mp3")
    
    try:
        communicate = edge_tts.Communicate(
            text=text,
            voice=voice,
            rate="+5%",
            pitch="+5Hz"
        )
        await communicate.save(temp_filename)
        
        def process_audio():
            audio = AudioSegment.from_file(temp_filename)
            processed_audio = _parrotify(audio)
            processed_audio.export(final_output_path, format="mp3")
            
        await asyncio.to_thread(process_audio)
        
        return final_output_path

    except Exception as e:
        print(f"Error generating TTS: {e}")
        return None
        
    finally:
        if os.path.exists(temp_filename):
            os.remove(temp_filename)

if __name__ == "__main__":
    async def test():
        print("Generating...")
        path = await generate_parrot_voice("Hello, I am a speaking parrot.", "test_parrot.mp3")
        print(f"Done! Saved to: {path}")
        
    asyncio.run(test())

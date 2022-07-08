from pathlib import Path
from tqdm import tqdm
import matplotlib.pyplot as plt
import numpy as np
import ffmpeg

from .utils import read_file, select_BBH

Zs = np.arange(1, 1_000) / 10_000

DATA_PATH = Path(__file__).parent.parent / 'jacopo' / 'data'

def plot_and_save(plotting_func):
    plotting_func()
    this_folder = Path()
    plt.savefig(
        this_folder / (str(plotting_func.__name__).split(sep='.')[0] + '.pdf'), 
        bbox_inches='tight', 
        pad_inches = 0
    )
    plt.close()

def make_vid_varying_metallicity(
    plot_frame: callable,
    vid_name: str, 
    framerate: int = 2,
    frame_title: callable = lambda data : f', {len(data)} mergers',
    data_path: Path = DATA_PATH,
    selector: callable = select_BBH,
    ):
    
    this_folder = Path().resolve()
    frames_folder = this_folder / f'frames_{vid_name}'
    
    if not frames_folder.exists():
        frames_folder.mkdir()
    
    for i, Z in tqdm(enumerate(Zs)):
        try:
            data = selector(read_file(DATA_PATH / f'Z_{Z:.4f}mergers.out'))
        except FileNotFoundError:
            continue

        plot_frame(data)

        plt.title(f'Z={float(Z):.4f}' + frame_title(data))
        
        plt.savefig(frames_folder / f'{i:04}.png')
        plt.close()
    
    (
        ffmpeg
        .input(str(frames_folder/'*.png'), pattern_type='glob', framerate=framerate)
        .output(str(this_folder / f'{vid_name}.mp4'))
        .run()
    )
    
    for img in frames_folder.iterdir():
        img.unlink()
    frames_folder.rmdir()

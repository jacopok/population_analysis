from pathlib import Path
from tqdm import tqdm
import matplotlib.pyplot as plt
import numpy as np
import ffmpeg
from functools import partial, update_wrapper

cmap = plt.get_cmap('plasma')

colors = {
    'BBH': cmap(.2),
    'BNS': cmap(.5),
    'NSBH': cmap(.8),
}

from .utils import read_file, select_BBH

Zs = np.arange(1, 1_000) / 10_000

DATA_PATH = Path(__file__).parent.parent / 'jacopo' / 'data'

temp_filenames = {f'{Z:.4f}': DATA_PATH / f'Z_{Z:.4f}mergers.out' for Z in Zs}
FILENAMES = {Z: f for Z, f in temp_filenames.items() if f.exists()}

def plot_and_save(plotting_func, name_addon: str = ''):
    plotting_func()
    this_folder = Path()
    plt.savefig(
        this_folder / (str(plotting_func.__name__).split(sep='.')[0] + name_addon + '.pdf'), 
        bbox_inches='tight', 
        pad_inches = 0
    )
    plt.close()

def make_vid_varying_metallicity(
    plot_frame: callable,
    vid_name: str, 
    framerate: int = 2,
    frame_title: callable = lambda data : f', {len(data)} mergers',
    filenames: dict[str, Path] = FILENAMES,
    selector: callable = select_BBH,
    ):
    
    this_folder = Path().resolve()
    frames_folder = this_folder / f'frames_{vid_name}'
    
    if not frames_folder.exists():
        frames_folder.mkdir()
    
    for i, (Z, filename) in tqdm(enumerate(filenames.items())):
        try:
            data = selector(read_file(filename))
        except FileNotFoundError:
            continue

        plot_frame(data)

        plt.title(f'Z={Z}' + frame_title(data))
        
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
    
def plot_at_metallicity(plotting_func, selector=select_BBH, Z='0.0001'):
    partial_func = partial(plotting_func, data=selector(read_file(FILENAMES[Z])))
    update_wrapper(partial_func, plotting_func)
    plt.title(f'Z={Z}')
    plot_and_save(partial_func, f'_Z={Z}')

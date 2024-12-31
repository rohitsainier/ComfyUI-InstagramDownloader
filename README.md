# Instagram Downloader for ComfyUI

A ComfyUI custom node package that allows downloading and organizing Instagram content directly in your ComfyUI workflows.

## Features

- Download photos and videos from Instagram profiles
- Organize media into separate folders
- Clean up temporary files
- Easy integration with ComfyUI workflows

## Installation

### Via ComfyUI Manager

1. Open ComfyUI Manager
2. Search for "Instagram Downloader"
3. Click Install

### Manual Installation

1. Clone this repository into your `ComfyUI/custom_nodes` directory:

```bash
cd custom_nodes
git clone https://github.com/rohitsainier/ComfyUI-InstagramDownloader
```

2. Install dependencies:

```bash
cd instagram_downloader_comfyui
pip install -r requirements.txt
```

## Usage

### Nodes

1. **Instagram Downloader**

   - Input: Instagram username
   - Output: Download path
   - Downloads content from specified Instagram profile

2. **Media Organizer**

   - Input: Download path
   - Output: Organized media paths
   - Separates content into images and videos folders

3. **Cleanup**
   - Input: Directory path
   - Output: Status message
   - Cleans up temporary files

### Example Workflow

1. Add Instagram Downloader node
2. Connect it to Media Organizer node
3. Optionally connect to Cleanup node
4. Configure username and download path
5. Run workflow

## License

MIT License

## Credits

Created by Rohit Saini

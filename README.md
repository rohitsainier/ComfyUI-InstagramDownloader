# Instagram Downloader for ComfyUI

A ComfyUI custom node package that allows downloading and organizing Instagram content directly in your ComfyUI workflows.
<img width="1383" alt="Screenshot 2025-01-01 at 10 28 10 PM" src="https://github.com/user-attachments/assets/732d66e1-c6c7-4a8e-9e3c-9df6237ac127" />
<img width="1325" alt="Screenshot 2025-01-01 at 10 39 16 PM" src="https://github.com/user-attachments/assets/80f9b6f8-d018-43d4-9dab-b3f2150603f5" />


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
cd ComfyUI-InstagramDownloader
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

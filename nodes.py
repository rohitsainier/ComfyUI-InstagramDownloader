import os
import shutil
import instaloader
from typing import Dict, Any, Tuple

try:
    import folder_paths
except ImportError:
    class FolderPaths:
        def get_output_directory(self):
            return os.path.join(os.path.dirname(__file__), "output")
    folder_paths = FolderPaths()


class InstagramDownloaderNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "username": ("STRING", {"default": "", "multiline": False}),
                "download_path": ("STRING", {"default": "downloads"}),
                "profile_pic_only": ("BOOLEAN", {"default": False}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("download_path",)
    FUNCTION = "download_profile"
    CATEGORY = "instagram"

    def download_profile(self, username: str, download_path: str, profile_pic_only: bool = False) -> Tuple[str]:
        try:
            # Create download directory
            full_path = os.path.join(
                folder_paths.get_output_directory(), download_path, username)
            os.makedirs(full_path, exist_ok=True)

            # Initialize downloader
            loader = instaloader.Instaloader(
                dirname_pattern=full_path,
                download_pictures=True,
                download_videos=True,
                download_video_thumbnails=False,
                save_metadata=False
            )

            # Download profile content
            profile = instaloader.Profile.from_username(
                loader.context, username)
            loader.download_profile(profile, profile_pic_only=profile_pic_only)

            return (full_path,)

        except Exception as e:
            raise RuntimeError(f"Download failed: {str(e)}")


class MediaOrganizerNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "input_path": ("STRING", {"default": ""}),
            }
        }

    RETURN_TYPES = ("STRING", "STRING", "INT", "INT")
    RETURN_NAMES = ("images_path", "videos_path", "image_count", "video_count")
    FUNCTION = "organize_media"
    CATEGORY = "instagram"

    def organize_media(self, input_path: str) -> Tuple[str, str, int, int]:
        try:
            # Create media directories
            images_path = os.path.join(input_path, "images")
            videos_path = os.path.join(input_path, "videos")
            os.makedirs(images_path, exist_ok=True)
            os.makedirs(videos_path, exist_ok=True)

            # Track counts
            image_count = 0
            video_count = 0

            # Organize files
            for filename in os.listdir(input_path):
                source_path = os.path.join(input_path, filename)

                if os.path.isfile(source_path):
                    if filename.endswith((".jpg", ".png")):
                        shutil.move(source_path, os.path.join(
                            images_path, filename))
                        image_count += 1
                    elif filename.endswith(".mp4"):
                        shutil.move(source_path, os.path.join(
                            videos_path, filename))
                        video_count += 1

            return (images_path, videos_path, image_count, video_count)

        except Exception as e:
            raise RuntimeError(f"Organization failed: {str(e)}")


NODE_CLASS_MAPPINGS = {
    "InstagramDownloader": InstagramDownloaderNode,
    "MediaOrganizer": MediaOrganizerNode,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "InstagramDownloader": "Instagram Downloader",
    "MediaOrganizer": "Media Organizer",
}

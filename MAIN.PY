import os
import shutil
import re

def cleanup_gifs_folders_and_videos():
    """
    Detect and delete:
    1. Folders with .gifs extension in C:\Users\harip\ALL TEST
    2. Video files in D:\downloads that have the same base name as the .gifs folders
    """
    target_directory = r"C:\Users\harip\ALL TEST"
    downloads_directory = r"D:\downloads"
    
    if not os.path.exists(target_directory):
        print(f"❌ Directory not found: {target_directory}")
        return 0, 0
    
    if not os.path.exists(downloads_directory):
        print(f"❌ Downloads directory not found: {downloads_directory}")
        return 0, 0
    
    try:
        # Get all items in the target directory
        all_items = os.listdir(target_directory)
        
        # Filter only folders that end with .gifs
        gifs_folders = []
        for item in all_items:
            item_path = os.path.join(target_directory, item)
            if os.path.isdir(item_path) and item.endswith('.gifs'):
                gifs_folders.append(item)
        
        # Get video files from downloads directory that match the .gifs folder names
        video_files_to_delete = []
        
        for folder in gifs_folders:
            # Remove the .gifs extension to get the base name
            base_name = folder[:-5]  # Remove ".gifs" from the end
            
            # Look for video files in downloads that start with this base name
            try:
                download_files = os.listdir(downloads_directory)
                for file in download_files:
                    file_path = os.path.join(downloads_directory, file)
                    if os.path.isfile(file_path):
                        # Check if file starts with the base name (video files often have additional info like [id])
                        if file.startswith(base_name):
                            video_files_to_delete.append(file)
            except Exception as e:
                print(f"⚠️  Error scanning downloads for {base_name}: {e}")
        
        # Count and display results
        folder_count = len(gifs_folders)
        video_count = len(video_files_to_delete)
        
        if folder_count == 0 and video_count == 0:
            print("✅ No .gifs folders or matching video files found to delete.")
            return 0, 0
        
        if folder_count > 0:
            print(f"📁 Found {folder_count} .gifs folder(s):")
            for i, folder in enumerate(gifs_folders, 1):
                print(f"  {i}. {folder}")
        
        if video_count > 0:
            print(f"🎬 Found {video_count} matching video file(s) in downloads:")
            for i, video_file in enumerate(video_files_to_delete, 1):
                print(f"  {i}. {video_file}")
        
        # Ask for confirmation before deletion
        if folder_count > 0 or video_count > 0:
            print(f"\n⚠️  WARNING: This will permanently delete:")
            if folder_count > 0:
                print(f"   - {folder_count} .gifs folder(s) and all their contents")
            if video_count > 0:
                print(f"   - {video_count} video file(s) from downloads")
            
            confirmation = input("\nType 'YES' to confirm deletion, or anything else to cancel: ").strip()
            
            if confirmation.upper() == 'YES':
                deleted_folders = 0
                deleted_videos = 0
                
                # Delete .gifs folders
                for folder in gifs_folders:
                    folder_path = os.path.join(target_directory, folder)
                    try:
                        shutil.rmtree(folder_path)
                        print(f"✅ Deleted folder: {folder}")
                        deleted_folders += 1
                    except Exception as e:
                        print(f"❌ Failed to delete folder {folder}: {e}")
                
                # Delete matching video files
                for video_file in video_files_to_delete:
                    video_path = os.path.join(downloads_directory, video_file)
                    try:
                        os.remove(video_path)
                        print(f"✅ Deleted video: {video_file}")
                        deleted_videos += 1
                    except Exception as e:
                        print(f"❌ Failed to delete video {video_file}: {e}")
                
                print(f"\n🎉 Cleanup completed!")
                print(f"📁 Folders deleted: {deleted_folders}")
                print(f"🎬 Videos deleted: {deleted_videos}")
                return deleted_folders, deleted_videos
            else:
                print("❌ Deletion cancelled by user.")
                return 0, 0
        else:
            print("✅ Nothing to delete.")
            return 0, 0
            
    except Exception as e:
        print(f"❌ Error during cleanup: {e}")
        return 0, 0

# --- Main Program Execution ---
if __name__ == "__main__":
    
    print("🧹 .GIFS FOLDER & VIDEO CLEANUP TOOL")
    print("=" * 50)
    
    # Run the cleanup function
    deleted_folders, deleted_videos = cleanup_gifs_folders_and_videos()
    
    print(f"\n{'='*50}")
    print("📊 CLEANUP SUMMARY")
    print(f"{'='*50}")
    print(f"📁 Folders deleted: {deleted_folders}")
    print(f"🎬 Videos deleted: {deleted_videos}")
    print("🎉 Cleanup completed!")

import os
import shutil

def cleanup_gifs_folders():
  
    target_directory = r"C:\Users\harip\ALL TEST"
    
    if not os.path.exists(target_directory):
        print(f"❌ Directory not found: {target_directory}")
        return 0
    
    try:
        # Get all items in the directory
        all_items = os.listdir(target_directory)
        
        # Filter only folders that end with .gifs
        gifs_folders = []
        for item in all_items:
            item_path = os.path.join(target_directory, item)
            if os.path.isdir(item_path) and item.endswith('.gifs'):
                gifs_folders.append(item)
        
        # Count and display results
        folder_count = len(gifs_folders)
        
        if folder_count == 0:
            print("✅ No .gifs folders found to delete.")
            return 0
        
        print(f"📁 Found {folder_count} .gifs folder(s):")
        for i, folder in enumerate(gifs_folders, 1):
            print(f"  {i}. {folder}")
        
        # Ask for confirmation before deletion
        print(f"\n⚠️  WARNING: This will permanently delete {folder_count} .gifs folder(s) and all their contents!")
        confirmation = input("Type 'YES' to confirm deletion, or anything else to cancel: ").strip()
        
        if confirmation.upper() == 'YES':
            deleted_count = 0
            for folder in gifs_folders:
                folder_path = os.path.join(target_directory, folder)
                try:
                    shutil.rmtree(folder_path)
                    print(f"✅ Deleted: {folder}")
                    deleted_count += 1
                except Exception as e:
                    print(f"❌ Failed to delete {folder}: {e}")
            
            print(f"\n🎉 Successfully deleted {deleted_count} out of {folder_count} .gifs folder(s)")
            return deleted_count
        else:
            print("❌ Deletion cancelled by user.")
            return 0
            
    except Exception as e:
        print(f"❌ Error during cleanup: {e}")
        return 0

# --- Main Program Execution ---
if __name__ == "__main__":
    
    print("🧹 .GIFS FOLDER CLEANUP TOOL")
    print("=" * 50)
    
    # Run the cleanup function
    deleted_count = cleanup_gifs_folders()
    
    print(f"\n{'='*50}")
    print("📊 CLEANUP SUMMARY")
    print(f"{'='*50}")
    print(f"🗑️  Folders deleted: {deleted_count}")
    print("🎉 Cleanup completed!")

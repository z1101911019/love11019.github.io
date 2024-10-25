import os
import datetime

def auto_push():
    try:
        # Add all changes
        os.system('git add .')
        
        # Create commit message with timestamp
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        commit_message = f"Auto update: {timestamp}"
        os.system(f'git commit -m "{commit_message}"')
        
        # Push to GitHub
        os.system('git push')
        print(f"Successfully pushed to GitHub at {timestamp}")
    
    except Exception as e:
        print(f"Error occurred: {str(e)}")

if __name__ == "__main__":
    auto_push()
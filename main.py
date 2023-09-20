import os
def show_notification(title,message):
    script = f'display notification "{message}" with title "{title}"'
    os.system(f'osascript -e \'{script}\'')
if __name__ == "__main__":
    title = "HACK ALERT !"
    message = "YOUR COMPUTER HAS BEEN HACKED !"

    show_notification(title,message)

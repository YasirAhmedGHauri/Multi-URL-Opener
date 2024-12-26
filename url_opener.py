import webbrowser

def open_urls(file_path):
    try:
        with open(file_path, 'r') as file:
            urls = [url.strip() for url in file if url.strip()]
        
        for url in urls:
            if not url.startswith(('http://', 'https://')):
                url = 'http://' + url
            
            webbrowser.open(url)
        
        print(f"Opened {len(urls)} URLs successfully!")
    
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# When in the same folder, just use the filename
urls_file = 'urls.txt'
open_urls(urls_file)
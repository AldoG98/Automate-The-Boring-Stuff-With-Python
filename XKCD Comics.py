import os
import requests
from bs4 import BeautifulSoup

def download_xkcd_comics(start_url="https://xkcd.com/"):
    """
    Downloads all XKCD comics starting from the given URL by following the 'prev' links.
    
    Comics are saved in a folder named 'xkcd'. The process stops when there are no more
    previous comics (i.e., when the URL ends with '#').
    """
    # Create a directory to save comics.
    os.makedirs("xkcd", exist_ok=True)
    
    url = start_url

    while not url.endswith("#"):
        print(f"Downloading page {url}...")
        try:
            res = requests.get(url)
            res.raise_for_status()
        except requests.RequestException as e:
            print(f"❌ Failed to download page: {e}")
            break
        
        soup = BeautifulSoup(res.text, "html.parser")

        # Find the comic image URL.
        comic_elem = soup.select("#comic img")
        if comic_elem == []:
            print("❌ Could not find comic image on this page.")
        else:
            comic_url = "https:" + comic_elem[0].get("src")
            print(f"Downloading image {comic_url}...")
            try:
                res = requests.get(comic_url)
                res.raise_for_status()
            except requests.RequestException as e:
                print(f"❌ Failed to download image: {e}")
                continue

            # Save the image to the 'xkcd' folder.
            image_file = os.path.join("xkcd", os.path.basename(comic_url))
            with open(image_file, "wb") as image:
                image.write(res.content)
            print(f"✅ Saved {image_file}")

        # Get the 'prev' button's URL.
        prev_link = soup.select("a[rel='prev']")
        if prev_link:
            url = "https://xkcd.com" + prev_link[0].get("href")
        else:
            print("❌ No 'prev' link found. Stopping.")
            break

    print("\n🎉 All available XKCD comics have been downloaded!")

if __name__ == "__main__":
    download_xkcd_comics()

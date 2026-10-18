import json
import urllib.request

JSON_URL = "https://raw.githubusercontent.com/vijay-iptv/JSON/refs/heads/main/pishow.json"
OUTPUT_FILE = "playlist.m3u"


def fetch_json(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req) as response:
        return json.loads(response.read().decode("utf-8"))


def generate_m3u(channels, output_file):
    lines = ["#EXTM3U"]
    for ch in channels:
        name = ch.get("name", "Unknown")
        logo = ch.get("logo_url", "")
        stream = ch.get("stream_url", "")
        language = ch.get("language_name", "")
        ch_id = ch.get("id", "")
        if not stream:
            continue
        lines.append(
            f'#EXTINF:-1 tvg-id="{ch_id}" tvg-name="{name}" '
            f'tvg-logo="{logo}" group-title="{language}",{name}'
        )
        lines.append(stream)
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"✅ Playlist তৈরি হয়েছে: {output_file}")


def main():
    print("⏳ JSON fetch করা হচ্ছে...")
    channels = fetch_json(JSON_URL)
    print(f"✅ {len(channels)} টি channel পাওয়া গেছে।")
    generate_m3u(channels, OUTPUT_FILE)


if __name__ == "__main__":
    main()

# MultiFetch
# S.To Batch Downloader

A simple Python script to batch download videos from [s.to](https://s.to). Currently, the script supports downloading from the `s.to/series/stream/series` URL format.

### Prerequisites
Before you can run the script, you'll need Python 3.6 or higher installed. You can download it from [here](https://www.python.org/downloads/).

Additionally, you may need the following Python libraries:

- `requests`
- `beautifulsoup4`
- `yt-dlp`
- `wget`
- `selenium`

Install the necessary dependencies using `pip`:

```bash
pip install -r requirements.txt
```


## Usage
1. Download the latest Release
3. use the:

### Batch Downloader
```
python main.py [URL]
```
## To-Do List

- [ ] **Episode Selection**: Allow users to select specific episodes instead of downloading the entire series.
- [ ] **Alternative Source Option**: Currently, the tool only works with `voe.sx`. Add support for alternative streaming sources.
- [ ] **More Website Support**: Expand compatibility beyond `s.to` to support other streaming websites.



import Downloader
import sys

def main():
    args = sys.argv #saving the cli arguments into args

    try:
        args[1]     #try if args has a value at index 1
    except IndexError:
        print("Please use a parameter. Use -h for Help") #if not, tells the user to specify an argument
        quit()

    if args[1] == "-h":     #if the first user argument is "-h" call the help function
        Downloader.help()
    else:
        URL = args[1]       #if the first user argument is the <URL> call the download function
        Downloader.list_dl(URL)

def help():
    print("Version v1.0")
    print("")
    print("______________")
    print("Arguments:")
    print("-h shows this help")
    print("<URL> just the URL will download all the available episodes to download")
    print("______________")
    print("")


if __name__ == "__main__":
    main()
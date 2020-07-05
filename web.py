import webbrowser
site=str(input("Enter the website url:"))
visit="http://{}".format(site)
webbrowser.open(visit)
"""
plotStats() method to collect statistics for the track data.

Author: Kunal Singh 
Email: pykunalsingh@gmail.com
"""

def plotStats(fileName):
    # read in a playlist
    with open(fileName, 'rb') as fp:
        plist = plistlib.load(fp)
    
    # get the tracks from the playlist
    tracks = plist['Tracks']
    # create lists of songs rating and track durations
    ratings = []
    durations = []

    # iterate through the tracks
    for trackId, track in tracks.items():
        try:
            ratings.append(track['Album Rating'])
            durations.append(track['Total Time'])
        except:
            pass
    # ensure that vaild data was collected
    if ratings == [] or durations == []:
        print("No valid Album Rating/Total Time data in %s."%fileName)
        return


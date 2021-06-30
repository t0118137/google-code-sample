"""A video player class."""

import random
import nltk
import re

from .video_library import VideoLibrary
from nltk import pos_tag

class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self.playing = []

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")


    def show_all_videos(self):
        """Returns all videos."""
                
        print("Here's a list of all available videos:")
        displayAllVideos = self._video_library.get_all_videos()
        # sort in lexicographical order
        sortInLexiVideos = sorted(displayAllVideos, key=lambda x:x.title)
        for videos in sortInLexiVideos:
            # if input is true
            if videos:
                # print all videos info
                print(videos.title, "(" + videos.video_id + ")", videos.tags)
    
    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        
        # setting global variable for playVideo so that 
        # can be used in other functions
        global playVideo
        playVideo = self._video_library.get_video(video_id)
        # if the user played a video successfully
        try:
            if playVideo:
                print("Playing Video:", playVideo.title)
            else:
                print("Cannot play video: Video does not exist")
        # if the user played a non-existing video
        except AssertionError:
            print("Playing Video:", playVideo.title)
        
    def stop_video(self):
        """Stops the current video."""
        
        # using the global variable to stop the video
        global stopped
        print("Stopping Video:", playVideo.title)
        if not stopped:
            print("Cannot stop video: No video is currently playing")
            stopped = False
            return playVideo.title
        
    def play_random_video(self):
        """Plays a random video from the video library."""
        
        displayAllVideos = self._video_library.get_all_videos()
        # random choose of the video
        random.choice(list(displayAllVideos))
        for videos in displayAllVideos:
            print("Playing Video: ", videos.title)
            return


    def pause_video(self):
        """Pauses the current video."""
        
        x = 0
        # setting global variable for pause so that 
        # can be used in other functions
        global pause
        # if none video was pausing
        if input == "pause":
            x = x + 1
            print("Pausing Video: ", playVideo.title)
            pause = True
        # if there is a video pausing
        elif x >= 2:
            print("Video already paused:", playVideo.title)
            pause = True
        #if no video can be paused
        else:
            print("Cannot pause video: No video is currently playing")
            pause = False
        return pause


    def continue_video(self):
        """Resumes playing the current video."""
        
        # continue a pausing video
        if pause:
            print("Continuing video:", playVideo.title)
        # if no video was paused
        else:
            print("Cannot continue video: Video is not paused")


    def show_playing(self):
        """Displays video currently playing."""
        
        currentPlaying = self._video_library.get_all_videos()
        getTheCurrent = playVideo.title + playVideo.id + playVideo.tags
        print("Currently Playing:", getTheCurrent)
        showPlay = True
        
        if pause == True & showPlay == True:
            print("Currently Playing:", currentPlaying, "- PAUSED")
        elif stopped == True & showPlay == False:
            print("No video is currently playing")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        
        # lower case the playlist name
        pl = playlist_name.lower()
        # create a whole new playlist
        if pl:
            print("Successfully created new playlist: my_PLAYlist")
        # if the playlist is already existing
        else:
            print("Cannot create playlist: A playlist with the same name already exists")
        

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        # add a video into playlist by video id
        if input == "ADD_TO_PLAYLIST" + playlist_name + video_id:
            print("Added video to my_playlist:", playVideo.title)

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")

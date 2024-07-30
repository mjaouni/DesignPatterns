from abc import ABC, abstractmethod


# Abstraction (MediaContent)
class MediaContent(ABC):
    def __init__(self, storage_renderer):
        self.storage_renderer = storage_renderer

    @abstractmethod
    def store_and_render(self):
        pass


# VideoContent: Concreate MediaContent
class VideoContent(MediaContent):
    def store_and_render(self):
        print('Handling Video Content')
        self.storage_renderer.store()
        self.storage_renderer.render()


class AudioContent(MediaContent):
    def store_and_render(self):
        print("Handling Audio Content")
        self.storage_renderer.store()
        self.storage_renderer.render()


# Abstract Implementer
class StorageRenderer(ABC):
    @abstractmethod
    def store(self):
        pass

    @abstractmethod
    def render(self):
        pass


# CloudStorageRenderer :Concreate Implementer
class CloudStorageRenderer(StorageRenderer):
    def store(self):
        print("Storing content in the cloud.")

    def render(self):
        print("Rendering content in the cloud.")


# LocalStorageRenderer :Concreate Implementer
class LocalStorageRenderer(StorageRenderer):
    def store(self):
        print("Storing content locally.")

    def render(self):
        print("Rendering content in the local storage.")


# usage

cloud_storage_renderer = CloudStorageRenderer()
video_content = VideoContent(cloud_storage_renderer)

video_content.store_and_render()

local_storage_renderer = LocalStorageRenderer()
audio_content = AudioContent(local_storage_renderer)

audio_content.store_and_render()
from abc import ABC, abstractmethod
from typing import Optional


# Strategy Interface
class CompressionStrategy(ABC):
    @abstractmethod
    def compress(self, file_path: str) -> None:
        pass


# Concrete Strategies
class ZipCompression(CompressionStrategy):
    def compress(self, file_path: str) -> None:
        print(f'Compressing {file_path} using ZIP compression')


class RarCompression(CompressionStrategy):
    def compress(self, file_path: str) -> None:
        print(f'Compressing {file_path} using RAR compression')


class TarCompression(CompressionStrategy):
    def compress(self, file_path: str) -> None:
        print(f'Compressing {file_path} using TAR compression')


# Context Class
class FileCompressor:
    def __init__(self):
        self.compression_strategy: Optional[CompressionStrategy] = None

    def set_compression_strategy(self, strategy: CompressionStrategy):
        self.compression_strategy = strategy

    def compress_file(self, file_path: str):
        if self.compression_strategy:
            self.compression_strategy.compress(file_path)
        else:
            print("Compress strategy not set")


# Usage
file_compressor = FileCompressor()
file_compressor.set_compression_strategy(ZipCompression())
file_compressor.compress_file('file_1.pdf')

file_compressor.set_compression_strategy(RarCompression())
file_compressor.compress_file('file_2.pdf')

file_compressor.set_compression_strategy(TarCompression())
file_compressor.compress_file('file_3.pdf')

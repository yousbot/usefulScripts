
import sys
import gzip
import bz2
import lzma
import zipfile
import tarfile
import os
from pyunpack import Archive

def convert_bytes(num):
    for unit in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return f"{num:3.1f} {unit}"
        num /= 1024.0

def get_file_format(file_path):
    return os.path.splitext(file_path)[1].lower()

def simulate_zip_decompression(zip_file_path):
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        return sum(info.file_size for info in zip_ref.infolist())

def simulate_tar_decompression(tar_file_path):
    with tarfile.open(tar_file_path, 'r') as tar_ref:
        return sum(info.size for info in tar_ref)

def simulate_other_decompression(file_path):
    print('Format not supported !')
    return None

def simulate_decompression(file_path):
    total_size = 0
    file_format = get_file_format(file_path)
    
    decompressors = {
        '.gz': gzip.open,
        '.bz2': bz2.open,
        '.xz': lzma.open,
        '.zip': simulate_zip_decompression,
        '.tar': simulate_tar_decompression,
        '.7z': simulate_other_decompression,
        '.ear': simulate_other_decompression,
        '.rar': simulate_other_decompression
    }
    
    decompressor = decompressors.get(file_format)
    
    if decompressor in [gzip.open, bz2.open, lzma.open]:
        with decompressor(file_path, 'rb') as f:
            while True:
                chunk = f.read(1024)
                if not chunk:
                    break
                total_size += len(chunk)
        return total_size
    elif decompressor:
        return decompressor(file_path)
    else:
        print("Unsupported or unknown file format.")
        return None

if __name__ == "__main__":
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        uncompressed_size = simulate_decompression(file_path)
        if uncompressed_size is not None:
            human_readable_size = convert_bytes(uncompressed_size)
            print(f"Simulated uncompressed size: {human_readable_size}")
    else:
        print("Usage: python script.py <File_Path>")

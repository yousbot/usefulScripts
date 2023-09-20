import gzip
import sys

def convert_bytes(num):
    for unit in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return f"{num:3.1f} {unit}"
        num /= 1024.0

def simulate_gzip_decompression(gzip_file_path):
    total_size = 0
    with gzip.open(gzip_file_path, 'rb') as f:
        while True:
            chunk = f.read(1024)  # Read only 1KB at a time
            if not chunk:  # Break loop when EOF is reached
                break
            total_size += len(chunk)
    return total_size

if __name__ == "__main__":
    if len(sys.argv) > 1:
        gzip_file_path = sys.argv[1]
        uncompressed_size = simulate_gzip_decompression(gzip_file_path)
        human_readable_size = convert_bytes(uncompressed_size)
        print(f"Simulated uncompressed size: {human_readable_size}")
    else:
        print("Please provide the path to the gzip file as an argument.")

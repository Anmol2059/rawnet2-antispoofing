import os

# Get the size of the .npy file in bytes
size_bytes = os.path.getsize('cache_train_LA_Raw_audio.npy')

# Convert the size to megabytes
size_mb = size_bytes / (1024 * 1024)

# Print the size
print(f"Size of the .npy file: {size_mb} MB")
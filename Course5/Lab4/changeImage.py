#!/usr/bin/env python3

from PIL import Image
import os


def convert_tiff_to_jpeg(input_dir, output_dir, size):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for file_name in os.listdir(input_dir):
        if file_name.lower().endswith('.tiff') or file_name.lower().endswith('.tif'):
            # Open the TIFF image
            with Image.open(os.path.join(input_dir, file_name)) as img:
                # Convert RGBA (4-channel) to RGB (3-channel) if necessary
                output_file = os.path.splitext(file_name)[0] + '.jpeg'
                try:
                    img.resize(size).convert('RGB').save(os.path.join(output_dir, output_file), 'JPEG')
                except Exception as e:
                    print(e)
                # if img.mode == 'RGBA':
                #     img = img.convert('RGB')
                #     print(f"Converted {file_name} from RGBA to RGB format.")
                #
                # # Resize the image
                # img_resized = img.resize(size)
                #
                # # Create the output file name
                # output_file_name = os.path.splitext(file_name)[0] + '.jpeg'

                # Save as JPEG in the output directory
                # try:
                #     img_resized.save(os.path.join(output_dir, output_file_name), 'JPEG')
                # except Exception as e:
                    print(e)

                print(f"Converted {file_name} with size {size}")


# Example usage



def main():
    input_directory = './data/images'
    output_directory = './data/images'
    new_image_size = (600, 400)
    # Convert images to different sizes
    # sizes = [(800, 600), (1024, 768), (1280, 720)]  # Add your desired sizes here
    convert_tiff_to_jpeg(input_directory, output_directory, new_image_size)


if __name__ == '__main__':
    main()

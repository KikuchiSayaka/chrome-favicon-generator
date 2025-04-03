# Favicon Generator for Chrome Extensions

This Python script resizes a source image into standard favicon sizes commonly used in Chrome extensions and saves them in PNG format.

## Features

- Automatically detects the user's Downloads folder across Windows, macOS, and Linux
- Outputs 16x16, 32x32, 48x48, and 128x128 pixel PNG files
- Simple command-line usage
- Requires only one dependency: Pillow

## Requirements

- Python 3.x
- Pillow (Python Imaging Library)

Install Pillow with:

```bash
pip install pillow
```

## Usage

Place the source image (e.g., sample.jpg) in your system’s Downloads folder.

Run the script:

```bash
python favicon_generator.py
```

When prompted, enter the filename of the source image (e.g., sample.jpg).

The resized favicons will be saved to your Downloads folder.

## Output Sizes

- favicon16x16.png – 16×16 pixels
- favicon32x32.png – 32×32 pixels
- favicon48x48.png – 48×48 pixels
- favicon128x128.png – 128×128 pixels

All images are saved in PNG format using high-quality resizing (LANCZOS).

## License

This project is licensed under the MIT License. See the LICENSE file for details.

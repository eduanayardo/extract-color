# Color Palette Extraction from Image

This Python script extracts the dominant color palette from an image and displays it along with color information in various formats (RGB, Hex, and CMYK). The script uses the K-Means clustering algorithm from scikit-learn to identify the most prominent colors.

## Usage

1. Ensure you have the required Python libraries installed: Pillow (PIL), NumPy, Matplotlib, and scikit-learn.
   ```bash
   pip install Pillow numpy matplotlib scikit-learn

2. Replace "`photo.jpg`" with the path to your desired image in the following line:
   ```phyton
   img = Image.open(`photo.jpg`)
3. Run the script:
   ```phyton
   python color_palette_extraction.py
4. The script will display the following:
  - The original image.
  - The extracted color palette in a visual format.
  - Detailed color information, including RGB, Hexadecimal, and CMYK values.

## Functionality
- The rgb_to_cmyk function is used to convert RGB values to CMYK values.
- The image is loaded, and its pixel matrix is flattened for analysis.
- The script identifies a specified number of dominant colors using K-Means clustering.
- The dominant colors are presented in both hexadecimal and RGB formats.
- CMYK values are calculated and displayed alongside RGB and Hex values.

## Screenshots
  Original code
  Link: https://twitter.com/clcoding/status/1711620072001901050
  ![image](https://github.com/eduanayardo/extract-color/assets/868883/dcb23d11-64b7-427d-9450-9bd38047ac3e)

  Result
  ![image](https://github.com/eduanayardo/extract-color/assets/868883/9f97260b-0107-4815-83f8-175d800d5654)

## Author
- [clcoding](https://twitter.com/clcoding)

## Contributors
- [Eduanayardo](https://github.com/eduanayardo)


Feel free to customize and use this script to analyze and visualize color palettes in images.

*Note: Please ensure that you have the necessary image (`photo.jpg` in this example) available or replace it with the path to your preferred image.*

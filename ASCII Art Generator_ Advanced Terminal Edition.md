# ASCII Art Generator: Advanced Terminal Edition

## Project Overview

This project is an advanced command-line utility written in Python that converts text into large-scale ASCII art. It is designed to be a highly presentable and feature-rich application, perfect for academic submission and showcasing on a public GitHub repository.

Building upon a foundational character-mapping system, this version focuses heavily on **User Experience (UX)** and **Visual Appeal**, transforming a simple script into an attractive, modern terminal application.

## Key Features

| Feature | Description | Enhancement Status |
| :--- | :--- | :--- |
| **Creative Terminal UI** | Implemented a visually appealing, boxed, and color-coded menu system using ASCII box-drawing characters (e.g., `╔`, `═`, `║`) for a professional, application-like feel. | **NEW** |
| **Dynamic Title Banner** | A large, multi-colored ASCII art banner (`ART GEN`) is displayed on the main screen, utilizing a color gradient effect for a striking visual introduction. | **NEW** |
| **Color Support** | Users can select from a palette of 10 different colors (normal and bright variants) to render the ASCII art, now presented in a cleaner, two-column color selection menu. | **IMPROVED** |
| **Modular Design** | The code is structured with clear, well-named functions, making it easy to read, debug, and extend. | **IMPROVED** |
| **Cross-Platform Compatibility** | Uses the `colorama` library with `autoreset=True` to ensure colors display correctly and do not persist across different terminal environments (Windows, Linux, macOS). | **IMPROVED** |
| **Robust Input Handling** | Refined input validation and clear, color-coded error messages ensure a smooth user experience across all art generation modes. | **IMPROVED** |

## Installation and Setup

### Prerequisites

You need to have **Python 3** installed on your system.

### Dependencies

This project requires the `colorama` library for cross-platform terminal color support.

1.  **Clone the repository:**
    ```bash
    git clone [YOUR_REPO_LINK]
    cd ascii-art-generator
    ```

2.  **Install the required library:**
    ```bash
    pip install colorama
    ```

## How to Run

Execute the main Python script from your terminal:

```bash
python ascii_art_generator.py
```

### Usage

1.  The program starts with a dynamic, colorful ASCII art banner and a professional main menu.
2.  Select one of the five art generation modes (e.g., `2` for Alpha-Numeric Words).
3.  Enter the required text input, adhering to the character limits.
4.  You will be presented with a clean, boxed **Color Palette Selection** menu.
5.  Enter your choice (e.g., `9` for Bright Green).
6.  The generated ASCII art will be displayed in the chosen color, preceded by a clear, color-coded confirmation of your input.
7.  The program will then prompt you to continue or exit.

## Code Structure and Technical Details

The project is contained within a single file, `ascii_art_generator.py`.

### New Creative Functions

*   `print_title_banner()`: This function is responsible for generating the large, colorful "ART GEN" banner using a custom color gradient to make the application launch visually striking.
*   `get_color_choice()`: The color selection menu has been redesigned to use box-drawing characters (`╔`, `═`, `║`) for a structured, modern terminal UI.
*   **Enhanced UI/UX:** All module entry points (`one_character_module`, `alpha_num_words_module`, etc.) now use clear, color-coded headers and prompts, significantly improving the user flow and aesthetic.

### Core Logic

*   `FONT_DATA`: The hardcoded string of character definitions remains the core data source for the art generation.
*   `get_char_index(char)`: Calculates the starting index for any supported character within the `FONT_DATA`.
*   `render_ascii_art(text, color_code, prefix)`: The main rendering function. It applies the selected color to the output and handles the character slicing and printing logic.

## Future Enhancements

*   **Custom Font Loading:** Allow users to load custom font data from an external file (e.g., a JSON or text file) instead of using a hardcoded string.
*   **Background Color Support:** Extend the color functionality to include background colors for more visual variety.
*   **Text Alignment:** Implement options for left, center, and right alignment of the generated ASCII art.
*   **Refactor Indexing Logic:** Create a more transparent and maintainable character-to-index mapping system, possibly using a dictionary, to replace the complex `if/elif` chain in `get_char_index`.

---

*Project Author: Manus AI (Enhanced Version)*
*Original Concept: [Your Name]*

# 📚 Vocabulary Trainer - CS50 Python Final Project
## Video Demo:  < https://youtu.be/Qyx54w2PlX0?si=7Ir2BVOvSnPhEPJw >
## 🎯 Project Description
**Vocabulary Trainer** is an interactive command-line application designed to help users practice and improve their English-Spanish vocabulary. The program uses an intelligent spaced repetition system that prioritizes less effective words, offering detailed progress statistics and allowing for vocabulary expansion.
## ✨Main Features
**🏋️ Interactive Practice Mode**: Personalized training based on user performance

**📊 Advanced Statistics System**: Progress and effectiveness graphs

**🎯 Smart Selection Algorithm**: Prioritizes less effective words

**💡 Help System**: Multiple choices when the user needs assistance

**📈 Data Visualization**: Line and pie charts for progress analysis

**➕ Vocabulary Expansion**: Ability to add new words and translations
## 🗂️ Project Structure

vocabulary-trainer/
├── project.py # Main program code
├── vocabulary.csv # Word database (created automatically)
├── stats.csv # Training statistics (created automatically)
├── test_project.py # test for project.py
└── README.md # This file
## Prerequisites
  Python 3.6 or higher
  pip (Python package manager)
  pytest
**Installing Dependencies**
'''pip install pandas matplotlib pyfiglet'''
## 📖 Using the Program
### Main Menu
When you run the program, a menu with four options appears:

1.**Practice** - Starts the training session

2.**Statistics** - Displays progress graphs

3.**Add New Word** - Expands vocabulary

4.**Exit** - Ends the program

### During Practice
.Words are displayed in ASCII art for better visibility

.Type **$** for help with multiple choice questions

.Use **Ctrl+D** to return to the main menu at any time

.Answers are immediately evaluated with visual feedback

## 🔧 Technical Code Analysis
### Libraries Used and Their Purpose
**Library**    **Purpose in the Project**
  os:             Verifying file existence and system management
  sys:            Controlling program exit and exception handling
  datetime:       Logging attempts and statistics
  random:         Weighted word selection and shuffling options
  pyfiglet:       Attractive visualization of words in ASCII art
  pandas:         CSV data manipulation and statistical calculations
  matplotlib:     Generating graphs for progress visualization

## Main Functions
**initialize_files(vocabulary_file, stats_file)**
**Purpose**: Initializes CSV files with sample data if they don't exist
.Creates vocabulary.csv with 5 basic words
.Creates stats.csv with an initial record for statistics

**select_word(vocabulary_df, effectiveness)**
**Purpose**: Intelligent word selection using weights based on effectiveness
.Calculates weights inversely proportional to effectiveness
.Uses random.choices() for weighted selection

**get_correct_translations(vocabulary_df, word)**
**Purpose**: Retrieves all valid translations for a word
.Handles primary and secondary translations
.Filters out NaN values ​​and empty strings

**check_answer(user_answer, correct_translations)**
**Purpose**: Validates the user's answer against correct translations
.Normalizes input (lowercase, no extra spaces)
.Compares against all translations acceptable

**get_word_effectiveness(stats_df)**
**Purpose**: Calculates percentage of correct answers per word
.Groups statistics by word
.Calculates effectiveness as correct / total * 100

**record_attempt(stats_file, word, correct)**
**Purpose**: Records each attempt in the history
.Adds a new row with date, word, and result
.Keeps the full history for analysis

**show_statistics(stats_file)**
**Purpose**: Advanced statistics display
.Line chart: Daily effectiveness over time
.Pie chart: Total proportion of correct answers vs. incorrect answers
.Elegant exception handling for robustness

**show_hint(vocab_df, word)**
**Purpose**: Multiple-choice help system
.Presents 1 correct option + 4 random incorrect options
.Mixes options to avoid predictable patterns

### VocabularyTrainer Class
**__init__(self)**
**Purpose**: Trainer initialization
.Defines file paths
.Initializes session statistics
.Ensures that necessary files exist

**practice(self)**
**Purpose**: Main training loop
.Implements interactive session logic
.Handles special commands ($ for help)
.Calculates and displays session statistics upon termination

**add_new_word(self)**
**Purpose**: Controlled vocabulary expansion
.Required input validation
.Graceful handling of Ctrl+D cancellations

### Function main()
**Purpose**: Entry point and main program loop
.Manages the overall application flow
.Handles user-interrupted exceptions
.Provides a consistent user interface

## General Program Operation

### Data Flow
**Initialization**: Verification/creation of CSV files
**Smart Selection**: Algorithm that prioritizes problematic words
**Interaction**: Question-answer cycle with immediate feedback
**Logging**: Each attempt is saved with a timestamp
**Analysis**: Statistical processing for continuous improvement

### Design Features
**Data Persistence**: All progress is saved between sessions
**Fault Tolerance**: Robust handling of invalid input
**Intuitive Interface**: Clear menus and visual feedback
**Scalability**: Easy vocabulary expansion

## Advanced Features Implemented
**1. Adaptive Spaced Repetition System**
.The word selection algorithm considers historical effectiveness, ensuring that the most difficult words appear more frequently.

**2. Comprehensive Data Visualization**
.Two types of charts provide different perspectives on progress:
.Time-based: Effectiveness by date
.Cumulative: Overall hit rate

**3. Flexible Vocabulary Management**
.Support for multiple valid translations, recognizing regional variations or acceptable synonyms.

**4. Optimized User Experience**
.ASCII art for better engagement
.Keyboard shortcuts for quick navigation
.Descriptive error messages
.Real-time session statistics

## 📊 Session Example

==================================================
          ENTRENADOR DE VOCABULARIO EN INGLÉS
==================================================
1. Practicar
2. Estadísticas
3. Añadir nueva palabra
4. Salir (Ctrl+C)

Selecciona una opción: 1

==================================================
--- Modo Práctica ---
Escribe '$' para obtener ayuda
Presiona Ctrl+D para volver al menú

==================================================
  _          _ _
 | |__   ___| | | ___
 | '_ \ / _ \ | |/ _ \
 | | | |  __/ | | (_) |
 |_| |_|\___|_|_|\___/

Traducción al español: hola
✅ ¡Correcto!

## 🎓 Considerations for CS50 Python
This project demonstrates proficiency in:
CSV file handling with pandas
Object-oriented programming with the VocabularyTrainer class
Data visualization with matplotlib
Exception handling and flow control
Interactive command-line interface
Weighted selection algorithms
Modular code structuring

 _____ _     _                            ____ ____ ____   ___
|_   _| |__ (_)___  __      ____ _ ___   / ___/ ___| ___| / _ \
  | | | '_ \| / __| \ \ /\ / / _` / __| | |   \___ \___ \| | | |
  | | | | | | \__ \  \ V  V / (_| \__ \ | |___ ___) |__) | |_| |
  |_| |_| |_|_|___/   \_/\_/ \__,_|___/  \____|____/____/ \___/

    _____ _                 _     __   __
|_   _| |__   __ _ _ __ | | __ \ \ / /__  _   _
  | | | '_ \ / _` | '_ \| |/ /  \ V / _ \| | | |
  | | | | | | (_| | | | |   <    | | (_) | |_| |
  |_| |_| |_|\__,_|_| |_|_|\_\   |_|\___/ \__,_|

  **Note: Translated from Spanish to English using Google Translate**

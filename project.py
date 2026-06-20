#
# Library
#
import os
import sys
from datetime import datetime
import random
from pyfiglet import Figlet
import pandas as pd
import matplotlib.pyplot as plt

#
# Auxiliary Functions
#

def initialize_files(vocabulary_file, stats_file):
    """Creates the "vocabularies" and "stats" files if they don't exist.
    It also includes some initial data so they aren't empty."""
    if not os.path.exists(vocabulary_file):
        df = pd.DataFrame({
            "english": ["hello", "goodbye", "computer", "house", "water"],
            "spanish": ["hola", "adiós", "computadora", "casa", "agua"],
            "spanish2" : ["", "hasta luego", "ordenador", "hogar", ""]
        })
        df.to_csv(vocabulary_file, index=False)

    if not os.path.exists(stats_file):
        df = pd.DataFrame({
        "date": [datetime.now().strftime("%Y-%m-%d")],
        "word": ["hello"],
        "correct": [True]
        })
        df.to_csv(stats_file, index=False)

def select_word(vocabulary_df, effectiveness):
    """Select words based on the effectiveness shown by the user."""
    weights =[]
    for word in vocabulary_df["english"]:
        if word in effectiveness:
            weight = 1 - effectiveness[word]
        else:
            weight= 1
        weights.append(weight)
    selected_word =random.choices(vocabulary_df["english"].tolist(), weights=weights)[0]
    return selected_word
def get_correct_translations(vocabulary_df, word):
    """Gets the correct translations for the displayed word."""
    row = vocabulary_df[vocabulary_df["english"] == word].iloc[0]
    translations = [row["spanish"]]
    if pd.notna(row["spanish2"]) and row["spanish2"] != "":
        translations.append(row["spanish2"])
    return translations

def check_answer(user_answer, correct_translations):
    """Check if the answer entered by the user is correct"""
    user_answer=user_answer.lower().strip()
    list_correct_translations= [c_t.lower().strip() for c_t in correct_translations]
    return user_answer in list_correct_translations

def get_word_effectiveness(stats_df):
    """Calculate the effectiveness of each word"""
    effectiveness ={}
    for word in stats_df["word"].unique():
            word_stats_df = stats_df[stats_df["word"] ==word]
            total = len(word_stats_df)
            correct= word_stats_df["correct"].sum()
            effectiveness[word]= correct / total if total > 0 else 0
    return effectiveness

def record_attempt(stats_file, word, correct):
    """Logs each user attempt to the stats file"""
    stats_df = pd.read_csv(stats_file)
    today =datetime.now().strftime("%Y-%m-%d")

    new_record= pd.DataFrame({
        "date" : [today],
        "word": [word],
        "correct": [correct]
    })

    stats_df =pd.concat([stats_df, new_record], ignore_index=True)
    stats_df.to_csv(stats_file, index=False)

def show_statistics(stats_file):
    """Display graphs using data saved in the stats file using the record_attempt function.
       A line graph for a time trend and a pie chart for total effectiveness."""
    try:
        stats_df=pd.read_csv(stats_file)
        stats_df["date"] = pd.to_datetime(stats_df["date"])
        daily_stats = stats_df.groupby("date").agg({
            "correct": ["count", "sum"]}).reset_index()
        daily_stats.columns = ["date", "total", "correct"]
        daily_stats["effectiveness"] = (daily_stats["correct"] / daily_stats["total"]) * 100

        plt.figure(figsize=(12, 5))
        plt.subplot(1, 2, 1)
        plt.plot(daily_stats["date"], daily_stats["effectiveness"], marker='o', linewidth=2)
        plt.title("Efectividad Diaria")
        plt.xlabel("Fecha")
        plt.ylabel("Efectividad (%)")
        plt.ylim(0, 105)
        plt.grid(True)
        plt.xticks(rotation=45)

        plt.subplot(1, 2, 2)
        total_correct = stats_df["correct"].sum()
        total_incorrect = len(stats_df) - total_correct

        labels=['Correctas', 'Incorrectas']
        sizes=[total_correct, total_incorrect]
        colors =['#66b3ff', '#ff6666']
        plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
        plt.axis('equal')
        plt.title("Efectividad Total")

        plt.tight_layout()
        plt.show(block= False)
        input("Presiona cualquier tecla para volver al menu")
        plt.close()
    except Exception as e:
        print(f"Error al mostrar estadísticas: {e}")
        input("Presiona cualquier tecla para volver al menu")

def add_word_to_vocabulary(vocabulary_file, english, spanish, spanish2=""):
    """Offers the user the option to add new words"""
    df= pd.read_csv(vocabulary_file)
    new_word= pd.DataFrame({"english": [english],"spanish": [spanish], "spanish2": [spanish2]})
    df = pd.concat([df, new_word], ignore_index=True)
    df.to_csv(vocabulary_file, index=False)

def show_hint(vocab_df, word):
    """Shows the user five Spanish words that contain the correct answer."""
    correct_translations= get_correct_translations(vocab_df, word)
    all_spanish =vocab_df["spanish"].tolist()
    if "spanish2" in vocab_df.columns:
        all_spanish.extend(vocab_df["spanish2"].dropna().tolist())
    all_spanish= list(set(all_spanish))
    for correct in correct_translations:
        if correct in all_spanish:
            all_spanish.remove(correct)

    incorrect_options= random.sample(all_spanish, min(4, len(all_spanish)))
    options= correct_translations[:1] + incorrect_options
    random.shuffle(options)
    print("\nOpciones:")
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")

    return options

#
# Vocabulary Class
#

class VocabularyTrainer:
    def __init__(self):
        self.vocabulary_file= "vocabulary.csv"
        self.stats_file= "stats.csv"
        self.session_stats= {"correct": 0, "incorrect": 0}
        self.figlet =Figlet()
        initialize_files(self.vocabulary_file, self.stats_file)

    def load_vocabulary(self):
        return pd.read_csv(self.vocabulary_file)

    def load_stats(self):
        return pd.read_csv(self.stats_file)

    def practice(self):
        """It shows the user a word in English and the user must enter the correct translation into Spanish."""
        print("\n" + "="*50)
        print("\n--- Modo Práctica ---")
        print("Escribe '$' para obtener ayuda")
        print("Presiona Ctrl+D para volver al menú")

        self.session_stats= {"correct": 0, "incorrect": 0}
        vocab_df= self.load_vocabulary()
        effectiveness = get_word_effectiveness(self.load_stats())

        try:
            while True:
                word = select_word(vocab_df, effectiveness)
                correct_translations = get_correct_translations(vocab_df, word)

                print("\n" + "="*50)
                ascii_art= self.figlet.renderText(word)
                print(ascii_art)

                while True:
                        user_answer = input("Traducción al español: ").strip()

                        if user_answer == "$":
                            options= show_hint(vocab_df, word)
                            user_answer= input("Traducción al español: ").strip()
                        is_correct= check_answer(user_answer, correct_translations)

                        if is_correct:
                            print("✅ ¡Correcto!")
                        else:
                            print(f"❌ Incorrecto. La respuesta correcta es: {', '.join(correct_translations)}")

                        record_attempt(self.stats_file, word, is_correct)

                        if is_correct:
                            self.session_stats["correct"] += 1
                        else:
                            self.session_stats["incorrect"] += 1
                        break

        except (EOFError, KeyboardInterrupt):
                print("\nVolviendo al menú principal...")

        # Display session statistics
        total =self.session_stats["correct"] + self.session_stats["incorrect"]
        if total > 0:
            effectiveness =(self.session_stats["correct"] / total) * 100
            print(f"\n--- Efectividad de la sesión: {effectiveness:.1f}% ---")
            print(f"Correctas: {self.session_stats['correct']}")
            print(f"Incorrectas: {self.session_stats['incorrect']}")

    def show_statistics(self):
        """Method to display statistics"""
        show_statistics(self.stats_file)

    def add_new_word(self):
        """Method to add new words to the vocabulary"""
        print("\n" + "="*50)
        print("\n--- Añadir Nueva Palabra ---")

        try:
            while True:
                english = input("Palabra en inglés: ").strip()
                if english:
                    break
                print("La palabra en inglés es obligatoria.")

            while True:
                spanish =input("Traducción al español: ").strip()
                if spanish:
                    break
                print("Al menos una traducción al español es obligatoria.")

            spanish2 =input("Segunda traducción al español (opcional): ").strip()

            add_word_to_vocabulary(self.vocabulary_file, english, spanish, spanish2)
            print("✅ Palabra añadida correctamente.")

        except (EOFError, KeyboardInterrupt):
            print("\nOperación cancelada.")

#
# Function main
#

def main():
    trainer= VocabularyTrainer()

    while True:
        try:
            print("\n" + "="*50)
            print("          ENTRENADOR DE VOCABULARIO EN INGLÉS")
            print("="*50)
            print("1. Practicar")
            print("2. Estadísticas")
            print("3. Añadir nueva palabra")
            print("4. Salir (Ctrl+C)")

            option = input("\nSelecciona una opción: ").strip()

            if option== "1":
                trainer.practice()
            elif option =="2":
                trainer.show_statistics()
            elif option =="3":
                trainer.add_new_word()
            elif option== "4":
                sys.exit("¡Hasta luego!")
            else:
                print("Opción no válida. Por favor selecciona 1, 2, 3 o 4.")

        except EOFError:
            continue
        except KeyboardInterrupt:
            sys.exit("\n ¡Hasta luego!")

if __name__ == "__main__":
    main()

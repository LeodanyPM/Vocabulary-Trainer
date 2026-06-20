import pytest
import pandas as pd
import os
from datetime import datetime
from project import check_answer, get_correct_translations, select_word, get_word_effectiveness

# FIXTURES FOR TEST DATA
@pytest.fixture
def sample_vocabulary_df():
    """Fixture that provides a sample vocabulary DataFrame"""
    return pd.DataFrame({
        "english": ["hello", "goodbye", "computer"],
        "spanish": ["hola", "adiós", "computadora"],
        "spanish2": ["", "hasta luego", "ordenador"]})

@pytest.fixture
def sample_stats_df():
    """Fixture that provides a DataFrame of sample statistics"""
    return pd.DataFrame({
        "date": ["2024-01-01", "2024-01-01", "2024-01-02"],
        "word": ["hello", "hello", "goodbye"],
        "correct": [True, False, True]})

# Tests for check_answer
def test_check_answer(sample_vocabulary_df):
    #Test that check_answer identifies correct answers
    correct_translations = get_correct_translations(sample_vocabulary_df, "hello")
    spanish2_translations=get_correct_translations(sample_vocabulary_df, "computer")
    assert check_answer("hola", correct_translations)== True
    assert check_answer("  hola  ", correct_translations) ==True  # with spaces
    assert check_answer("HOLA", correct_translations) ==True      # capital letters
    assert check_answer("ordenador", spanish2_translations) ==True
    #Test that check_answer identifies incorrect answers
    assert check_answer("adios", correct_translations)== False
    assert check_answer("computadora", correct_translations) == False

# Test for get_correct_translations
def test_get_translations(sample_vocabulary_df):
    #Try getting translations when there is only one option
    translations =get_correct_translations(sample_vocabulary_df, "hello")
    assert len(translations) ==1
    assert "hola" in translations
    #Try getting translations when there are multiple options
    translations2= get_correct_translations(sample_vocabulary_df, "goodbye")
    assert len(translations2) == 2
    assert "adiós" in translations2
    assert "hasta luego" in translations2

# Test for get_word_effectiveness
def test_get_word_effectiveness(sample_stats_df):
    #Try the basic effectiveness calculation
    effectiveness = get_word_effectiveness(sample_stats_df)
    assert effectiveness["hello"] == 0.5  # 1 correcta de 2 intentos
    assert effectiveness["goodbye"]== 1.0  # 1 correcta de 1 intento
    #Test the calculation with an empty DataFrame
    empty_df =pd.DataFrame({"word": [], "correct": []})
    effectiveness_empty = get_word_effectiveness(empty_df)
    assert effectiveness_empty== {}

# Tests for select_word
def test_select_word(sample_vocabulary_df):
    #Test that select_word returns a valid word
    effectiveness ={"hello": 0.5, "goodbye": 0.8}
    selected_word = select_word(sample_vocabulary_df, effectiveness)
    assert selected_word in sample_vocabulary_df["english"].tolist()
    #Test selection when there is no effectiveness data
    effectiveness ={}
    selected_word= select_word(sample_vocabulary_df, effectiveness)
    assert selected_word in sample_vocabulary_df["english"].tolist()


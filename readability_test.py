from readability import char_counts, word_counts, sent_counts, ari_calc


def test_no_chars():
    ret= char_counts("")
    assert ret== 0

def test_special_char():
    ret= char_counts('"@#$%^&*()_-=+;:[]{}|\/')  
    assert ret== 0  

def test_nchars():
    ret= char_counts("The sky seems cloudy today it may rain 1234")
    assert ret== 35

def test_no_words():
    ret= word_counts("hello")
    assert ret== 0

def test_nwords():
    ret= word_counts("hi hello how are you") 
    assert ret== 4

def test_nsent():
    ret=sent_counts("Oh my god!you again. where were you?")  

def test_no_sent():
    ret= sent_counts("hi hello")
    assert ret== 0  

        
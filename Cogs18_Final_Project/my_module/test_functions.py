import functions

def test_is_question():
    assert callable(is_question)
    assert isinstance(is_question('abc'), bool)
    assert is_question('what?') == True

def test_remove_punc():
    assert callable(remove_punctuation)
    assert isinstance(remove_punctuation('a'), str)
    assert remove_punctuation("Hey! It's Mel!") == "Hey Its Mel"

def test_prepare_text():
    assert callable(prepare_text)
    assert isinstance(prepare_text('One two three.'), list)
    assert prepare_text('Hi! Also, howdy.') == ['hi', 'also', 'howdy']

def test_respond_echo():
    assert callable(respond_echo)
    assert isinstance(respond_echo('ha', 2, ' '), str)
    assert respond_echo('meow', 3, '~') == 'meow~meow~meow~'
    assert respond_echo(None, 2, '') == None

def test_selector():
    assert callable(selector)
    assert selector(['in', 'words'], ['words'], ['yes']) == 'yes'
    assert selector(['in', 'words'], ['out'], ['yes']) == None

def test_string_concatenator():
    assert callable(string_concatenator)
    assert isinstance(string_concatenator('hello', 'world', ' '), str)
    assert string_concatenator('hello', 'world', ' ') == 'hello world'

def test_list_to_string():
    assert callable(list_to_string)
    assert isinstance(list_to_string(['a', 'b'], '|'), str)
    assert list_to_string(['a', 'b'], '|') == 'a|b'

def test_end_chat():
    assert callable(end_chat)
    assert isinstance(end_chat(['a', 'b']), bool)
    assert end_chat(['quit']) == True

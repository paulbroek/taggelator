import pandas as pd
import wordninja # converting text without spaces to words
import copy

def read_file(file_name = "hashtag.csv"):
	return pd.read_csv(file_name, sep = ',')

"""
	Data cleaning
"""

"""
	Conversion methods, going from phrases to words, from words to categories
"""

def tag_to_words(tag):
	"""
		Description:	Takes in a hashtag, and extracts as many words as possible, returns most probable combination of words
		In:				STRING tag
		Out:			LIST[string]
		Examples: 		#bewegenopwerkplek --> 	['bewegen', 'op', 'werkplek']
						"2wheelnation" --> 		['2' ,'wheel', 'nation']
	"""
	vec = []

	vec = wordninja.split(tag)

	return vec

"""
	Test methods
"""

def test_random_tag_to_words(df, n=10):
	"""
		Description: 	For n tags, show the results of tag_to_words() in a 'result' column
	"""

	df_sample = copy.deepcopy(df.sample(n))
	df_sample['result'] = df_sample.tag.apply(tag_to_words)

	return df_sample


if __name__ == "__main__":

	"""
		File handling
	"""

	df = read_file()
	assert(len(df) > 0)



	
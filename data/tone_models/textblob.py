import re
import pandas as pd
from textblob import TextBlob
from tqdm import tqdm
tqdm.pandas()

main_df = pd.read_csv('friends.csv')

def clean_text(text):
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

main_df["cleaned_text"] = main_df["text"].progress_apply(clean_text)

def get_sentiment(dialogue):
    blob = TextBlob(dialogue)
    return blob.sentiment.polarity, blob.sentiment.subjectivity

main_df[['polarity', 'subjectivity']] = main_df['cleaned_text'].apply(lambda x: pd.Series(get_sentiment(x)))
sentiment_by_character = main_df.groupby('speaker')[['polarity', 'subjectivity']].mean().reset_index()

min_dialogue_threshold = 500
dialogue_count_by_character = main_df.groupby("speaker").size().reset_index(name = "dialogue_count")
main_characters = dialogue_count_by_character[dialogue_count_by_character["dialogue_count"] >= min_dialogue_threshold]["speaker"]
sentiment_main_characters = sentiment_by_character[sentiment_by_character["speaker"].isin(main_characters)]
sentiment_main_characters = sentiment_main_characters.sort_values(by = "polarity", ascending = False).reset_index(drop = True)
main_cast = ["Chandler Bing", "Joey Tribbiani", "Monica Geller", "Phoebe Buffay", "Rachel Green", "Ross Geller"]
sentiment_main_cast = sentiment_main_characters[sentiment_main_characters["speaker"].isin(main_cast)]

sentiment_main_cast.to_csv('textblob_sentiment.csv', index = False)

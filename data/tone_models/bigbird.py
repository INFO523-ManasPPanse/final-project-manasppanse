import re
import pandas as pd
from transformers import pipeline
from tqdm import tqdm

main_df = pd.read_csv('friends.csv')

def clean_text(text):
    if pd.isnull(text) or text.strip() == "":
        return None
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text if len(text) > 0 else None

main_df["cleaned_text"] = main_df["text"].apply(clean_text)

main_df = main_df.dropna(subset = ["cleaned_text"]).reset_index(drop=True)

bigbird_pipe = pipeline(
    'sentiment-analysis',
    model='google/bigbird-roberta-base',
    tokenizer='google/bigbird-roberta-base'
)

tqdm.pandas(desc = "Progress for BigBird Processing")

def analyze_sentiment(text):
    try:
        result = bigbird_pipe(text, truncation=True)
        if result and len(result) > 0:
            return result[0]  # Return the first result
    except Exception as e:
        print(f"Error processing text: {text[:30]}... -> {str(e)}")
    return None

main_df['bigbird_sentiment'] = main_df['cleaned_text'].progress_apply(analyze_sentiment)

main_df = main_df.dropna(subset = ["bigbird_sentiment"]).reset_index(drop = True)

print("Unique Sentiment Labels in Output :", main_df['bigbird_sentiment'].apply(lambda x: x['label']).unique())

main_df['bigbird_label'] = main_df['bigbird_sentiment'].apply(lambda x: x['label'])
main_df['bigbird_score'] = main_df['bigbird_sentiment'].apply(lambda x: x['score'])

label_mapping = {
    'LABEL_1': 1,
    'LABEL_0': -1,
    'POSITIVE': 1,
    'NEGATIVE': -1
}

main_df['bigbird_polarity'] = main_df['bigbird_label'].map(label_mapping) * main_df['bigbird_score']

main_df = main_df.dropna(subset = ["bigbird_polarity"])

sentiment_by_character = main_df.groupby('speaker')['bigbird_polarity'].mean().reset_index()
main_cast = ["Chandler Bing", "Joey Tribbiani", "Monica Geller", "Phoebe Buffay", "Rachel Green", "Ross Geller"]
sentiment_main_cast = sentiment_by_character[sentiment_by_character['speaker'].isin(main_cast)]
sentiment_main_cast = sentiment_main_cast.sort_values(by = 'bigbird_polarity', ascending = False).reset_index(drop = True)

sentiment_main_cast.to_csv('bigbird_main_cast_sentiment.csv', index = False)

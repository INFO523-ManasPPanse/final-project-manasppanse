


# Data

1.  `friends.csv` - Contains dialogues from all 10 seasons, with details like speaker, season, episode, scene, and the dialogue itself.

2.  `friends_emotions.csv` - Contains emotional labels for dialogues, used for sentiment analysis.

3.  `friends_info.csv` - Provides metadata like IMDb ratings and viewership statistics.

## Codebook for `friends.csv`

| Variable Name | Datatype | Description |
| --- | --- | --- |
| text | object | This columns contains all the dialogues spoken by all characters. |
| speaker | object | This columns contains the name of the character that spoke uttered that dialogue. |
| season | int64 | The season number in which the dialogue was spoken. |
| episode | int64 | The episode number in which the dialogue was spoken. |
| scene | int64 | The scene number in which the dialogue was spoken. |
| utterance | int64 | The utterance count basically indicates which dialogue came after which if there are multiple dialogues uttered in a scene. |

## Codebook for `friends_emotions.csv`

| Variable Name | Datatype | Description |
| --- | --- | --- |
| season | int64 | The season number in which the dialogue was spoken. |
| episode | int64 | The episode number in which the dialogue was spoken. |
| scene | int64 | The scene number in which the dialogue was spoken. |
| utterance | int64 | The utterance number basically indicates which dialogue came after which if there are multiple dialogues uttered in a scene. |
| emotion | object | This column contains the emotional label assigned to a particular dialogue spoken. |

## Codebook for `friends_info.csv`

| Variable Name | Datatype | Description |
| --- | --- | --- |
| season | int64 | The season number in which the dialogue was spoken. |
| episode | int64 | The episode number in which the dialogue was spoken. |
| title | object | This column contains the title of an the episode. |
| directed_by | object | This column contains the name of the director of an episode. |
| written_by | object | This column contains the name(s) of the writer(s) of an episode. |
| air_date | object | This column contains the data on which an episode aired on national TV. |
| us_views_millions | float64 | This columns contains the number of viewers who watched the episode live. |
| imdb_rating | float64 | This column contains the rating of an episode that's on the IMDb website. |

## Tone Models & Tone Model Outputs

`tone_models` - This directory contains the code for the models that were used to perform sentiment analysis on the `text` column in the `friends.csv` dataset.

1.  `textblob.py` - This python script performs the analysis using `TextBlob`.
2.  `bigbird.py` - This python script performs the analysis using `BigBird`.

`tone_model_outputs` - This directory contains the results obtained after performing sentiment analysis on the `text` column in the `friends.csv` dataset using the above mentioned models.

## Presentation

`presentation` - This directory contains the custom `background.jpg` for the title slide, as well as the custom theme file `theme.scss` for the rest of the slides of the presentation.
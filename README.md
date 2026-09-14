# Rebuilding the Social Engine

Exploratory Data Analysis (EDA) for the **Social Engine** reconstruction project.
This Phase 1 analysis restores two deliberately corrupted datasets and examines
posting activity, platform distribution, engagement, content, sentiment, and
user demographics.

## Project Contents

| File | Description |
| --- | --- |
| `vortex.ipynb` | Reproducible cleaning and EDA notebook |
| `Social_Engine_Posts_Corrupted.csv` | Raw, intentionally corrupted posts data |
| `Social_Engine_Users.csv` | User profile data |
| `Social_Engine_Phase1_EDA_Report (1).pdf` | Formal Phase 1 EDA report |
| `main.py` | Minimal Python entry point placeholder |
| `pyproject.toml` | Project metadata and dependencies |

## Dataset Summary

- **Posts:** 12,360 raw rows; 9,677 rows retained after cleaning (78.3%).
- **Users:** 1,500 users with no duplicate rows.
- **Time period:** 2024-2025 for posts; user account creation dates are concentrated in 2023.
- **Referential integrity:** Every `user_id` referenced by a post exists in the users table.

## Cleaning Performed

The notebook loads the raw CSV files and applies the Phase 1 cleaning rules:

- Removes exact duplicate post rows: 360 rows.
- Removes missing or non-numeric `likes`: 1,814 rows.
- Removes negative `likes`: 509 rows.
- Replaces missing `platform` values with `Unknown`.
- Replaces missing `text_content` values with `No content`.
- Parses timestamps from ISO datetime, day-month-year, and Unix epoch formats.
- Splits user `location` into city and country for geographic analysis.
- Uses a placeholder for missing user country values so those users are retained.
- Leaves mojibake and HTML entities flagged in free text; they do not affect numeric or temporal EDA.

`shares` and `comments` contain no missing or negative values in the supplied data.
Rows with unusable likes are dropped rather than imputed because fabricating
engagement values would change the analysis.

## Analysis Included

### Posts

- Posting volume by hour, day of week, month, and year
- Post volume by platform
- Distributions of likes, shares, and comments
- Average engagement by platform
- Correlation between engagement metrics
- Top words in post text using tokenization and stopword removal
- VADER sentiment classification into positive, neutral, and negative posts
- Average engagement by sentiment category

### Users

- Top countries and languages
- Follower-count distribution and highest-follower users
- Account creation timeline

## Key Findings

1. **The midnight peak is a data-quality warning.** Midnight contains 3,127 posts,
	more than twice the volume of any other hour. This likely reflects timestamps
	defaulted or truncated during corruption recovery, not genuine user behavior.
2. **No platform dominates.** Facebook, YouTube, Reddit, Twitter, and Instagram
	each contribute roughly one-sixth of posts. Recovered `Unknown` platforms still
	account for 14.8% of the cleaned data.
3. **Engagement is unusually uniform.** Likes, shares, and comments are close to
	uniformly distributed within fixed caps: 5,000 likes, 2,000 shares, and 1,000
	comments. Their means are approximately their medians.
4. **Engagement metrics are independent in this dataset.** The correlations among
	likes, shares, and comments are all effectively zero (`|r| < 0.03`).
5. **The user base is globally balanced.** The USA is the largest country group
	with 203 of 1,500 users (13.5%), and no language or follower tier dominates.
6. **Text requires further cleanup.** Mojibake and HTML entities remain in free
	text and should be corrected before treating keyword or sentiment results as
	production-quality signals.

## Getting Started

The notebook is intended to be run from the project root in Jupyter or VS Code.
Python 3.12 or newer is required.

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirments.txt
python3 -m pip install jupyter
```

Open `vortex.ipynb`, select the virtual environment as the kernel, and run the
cells from top to bottom. The first setup cells download the NLTK resources used
by keyword extraction and VADER sentiment analysis (`stopwords`, `punkt`, and
`vader_lexicon`).

The project also includes a `pyproject.toml` and `uv.lock` for environments that
use `uv`:

```bash
uv sync
uv run jupyter notebook vortex.ipynb
```

## Reproducibility Notes

- Keep the CSV files beside the notebook; its paths are relative to the project root.
- Run cells in order because later plots use columns created during cleaning.
- Treat the midnight timestamp concentration as a known limitation.
- Treat country-level results cautiously because missing countries use a placeholder.
- Sentiment and keyword analysis should be rerun after repairing encoding artifacts
  and HTML entities in the text field.

## Team

**Team:** `404_error`
**Team leader:** Nishant Goel
**Team member:** Bhavya Gupta
